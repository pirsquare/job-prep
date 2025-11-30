
## Worki
The application that powers OnVoard

## Table of Contents
  1. [Provisioning Servers](#provisioning-servers)
  1. [Setting up frontend](#setting-up-frontend)
  1. [Getting Started with Development and Testing](#getting-started-with-development-and-testing)
  1. [Setting up Titan Server](#setting-up-titan-server)
  1. [Utility Commands](#ulitity-commands)
  1. [Management Commands](#management-commands)
  1. [Post Migrate Tasks](#post-migrate-tasks)
  1. [Compatibility](#compatibility)

## Provisioning Servers
Required System Dependencies:
```shell
dnf config-manager --set-enabled crb
dnf -y install epel-release

dnf -y check-update
dnf -y install dnf-utils
dnf -y install python3 python3-pip python3-devel python3-virtualenv

mkdir /opt/python-envs && cd /opt/python-envs
pip install virtualenvwrapper

envtext="export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=/opt/python-envs
source /usr/local/bin/virtualenvwrapper.sh"
echo "$envtext" > /etc/profile.d/virtualenv.sh
source /etc/profile

mkvirtualenv onvoard
workon onvoard

# install system dependencies
dnf -y install psmisc wget lua-devel openssl-devel python-devel python-setuptools \
gcc gcc-c++ make libffi-devel mercurial postgresql postgresql-devel libjpeg-devel python-yaml

# install ffmpeg
dnf -y install --nogpgcheck https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-$(rpm -E %rhel).noarch.rpm
dnf -y install --nogpgcheck https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-$(rpm -E %rhel).noarch.rpm
dnf -y install ffmpeg ffmpeg-devel

# install fasttext
dnf -y install gcc gcc-c++ kernel-devel
dnf -y install python-devel libxslt-devel libffi-devel
pip install fasttext==0.9.2

mkdir /opt/fasttext
cd /opt/fasttext
wget -O lid.176.ftz https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz
chmod 755 /opt/fasttext/lid.176.ftz
```

## Setting up frontend
For frontend, we will do all grunt tasks (building/compiling) with our local workstation. As such, you need to ensure that `nodejs` is installed in your desktop. For dev, you will upload bundled static files to server via sftp. For deploy, you will use build static assets and run collectstatic before uploading static files to gcs directly from your local workstation.

Build code (dev)
```shell
# console
cd frontend/console
npm start
```

Build code (deploy)
```shell
# build assets for frontend
cd frontend/console
npm run build

# go back worki directory
cd ../..

# run collect static.
# Keep in mind that you need to install pip requirements in local workstation
set DJANGO_SETTINGS_MODULE=backend.settings.collectstatic
python manage.py collectstatic --no-input --clear

# we're not committing static assets to git and will use aws to sync r2 staging directly
# Exclude "--delete" flag because it is causing issue for r2
aws s3 sync frontend/console/assets s3://onvoard-staging/worki/console/assets --profile=r2 --endpoint-url=https://28d93d58bd8a04d5d9e70484c9170005.r2.cloudflarestorage.com

# sync directly if static files is still missing. Might happen with staging
aws s3 sync frontend/console/assets s3://onvoard/worki/console/assets --profile=r2 --endpoint-url=https://28d93d58bd8a04d5d9e70484c9170005.r2.cloudflarestorage.com
```

Build code shortcut (deploy)
```shell
python build-console-assets.py
```

## Getting Started with Development and Testing
The setup below assumes that your project directory is at `/opt/worki`

Set permission
```shell
chmod -R 0755 /opt/worki
```

Go to virtual environment
```
workon onvoard
```

Install required dependencies:
```shell
cd /opt/worki
pip install -r reqs/dev.txt
pip install -r reqs/test.txt
```

Install setup:
```shell
cd /opt/worki
chmod 0755 setup.sh
./setup.sh
source /etc/profile
```

Install & setup nginx server:
This will also use letsencrypt to setup ssl
```shell
cd /opt/worki
chmod 0755 install_nginx.sh
./install_nginx.sh
```

Install & setup postgres server:
```shell
cd /opt/worki
chmod 0755 install_postgres.sh

# This will also create database, user and password `onvoard`
./install_postgres.sh
```

Install & setup clickhouse:
```shell
cd /opt/worki
chmod 0755 install_clickhouse.sh
./install_clickhouse.sh
```

Install & setup rabbitmq server:
```shell
cd /opt/worki
chmod 0755 install_rabbitmq.sh
./install_rabbitmq.sh
```

Install & setup redis:
```shell
cd /opt/worki
chmod 0755 install_redis.sh
./install_redis.sh
```

Install & setup nodejs:
```shell
cd /opt/worki
chmod 0755 install_nodejs.sh
./install_nodejs.sh

Install & setup liquid:
```shell
cd /opt/worki
chmod 0755 install_liquid.sh
./install_liquid.sh
```

Install machine learning:
```shell
cd /opt/worki
chmod 0755 install_ml.sh
./install_ml.sh
```

Run test:
```shell
# full test
DJANGO_SETTINGS_MODULE="backend.settings.test"
python ./manage.py test --keepdb --parallel

# individual app
python ./manage.py test backend.common --keepdb
```

Provision database & setup webserver
```shell
cd /opt/worki
export SERVICE_TYPE=console

python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py loaddata dev.yaml dev_auto.yaml
python ./manage.py runserver 0.0.0.0:8000
```

Setup liquid service
```shell
cd /opt/worki/services/liquid
yarn
npm install -g forever
forever start -r esm index.js
```

Setup celery flower monitoring
```shell
pip install flower

cd /opt/worki
flower --port=5055 --broker_api=http://guest:guest@localhost:15672/api/

# Go to https://bwhere-flower.onvoard.com
```

Ensure you have setup your DNS `A records` so that you can access your dev environment from url below. We need to use an actual domain due to OAuth requirements with google API.
```shell
http://bwhere.onvoard.com
```

Now you can login with email `pirsquare.ryan@gmail.com` and password `test`


## Setting up Titan Server
A few things to keep in mind when setting up titan server
- Nginx runs on port 80
- Console server runs on port 8000
- Liquid service runs on port 4555
- Titan server runs on port 8001
- SSR node server runs on port 3001
- Endpoint for titan server is `https://bwhere-titan.onvoard.com`

Build code (dev)
```shell
# Upload titan files to server. For dev, we will build code and run on server.
cd /opt/worki/frontend/titan
yarn

# run dev server
node_modules/next/dist/bin/next dev -p 3001 --hostname localhost

# run titan server. Must ensure that service type is titan
export SERVICE_TYPE=titan
cd /opt/worki
python ./manage.py runserver 0.0.0.0:8001
```

Build code (deploy)
```shell
# For production, we will build in server
cd /opt/worki/frontend/titan
npm run build
/opt/worki/frontend/titan/node_modules/next/dist/bin/next start -p 3001 --hostname 0.0.0.0
```

Build code shortcut (deploy)
```shell
python build-titan-assets.py
```


## Utility Commands
Load fixtures
```shell
# Load Fixtures for Development
python ./manage.py loaddata dev.yaml dev_auto.yaml

# Load Fixtures for Production
python ./manage.py loaddata deploy.yaml deploy_auto.yaml
```

Clear pycache
```shell
# Linux
find . -name "__pycache__" -exec rm -rf {} \;

# Windows
del /S __pycache__
```

Export fixtures
```shell
# Fixtures will be exported as export.json
python ./manage.py dumpdata --natural --indent=2 > export.json
```

Setup celery worker + beat
```shell
C_FORCE_ROOT="true" celery worker --app=backend --loglevel=info --beat -n worker-celery -Q celery
C_FORCE_ROOT="true" celery worker --app=backend --loglevel=info -n worker-eevee -Q eevee
```

Purge all celery tasks
```shell
C_FORCE_ROOT="true" celery purge --app=backend -f -Q celery,eevee
```

Re-generate fixtures (execute in local workstation)
```shell
cd /opt/worki/scripts

# source fixtures
python gen_source_fixtures.py

# trigger fixtures
python gen_trigger_fixtures.py

# workflow action fixtures
python gen_workflow_action_fixtures.py

# copy dev fixtures to deploy
python copy_dev_fixtures_to_deploy.py
```

## Common Issues
### BlueprintJs
Building sass files from blueprintjs requires manual work.

**1) Configure webpack.config file**
See this [example](https://github.com/jgoz/druid/blob/776a67d080387d80ff4f1b0fae5ea9b3b5e15be2/web-console/webpack.config.js) and this [issue](https://github.com/palantir/blueprint/issues/6051). We will exclude `svg-icons` from compilation as it might cause issue and not straightforward.

**2) Replace Namespace**
Add namespace in webpack.config file
```
 new webpack.DefinePlugin({
     'BLUEPRINT_NAMESPACE': '"bp"',
     'process.env.BLUEPRINT_NAMESPACE': '"bp"',
 }),
```
Declare namespace variable to use before importing blueprint scss in your css file.
```
$ns: bp;
@import "~@blueprintjs/core/src/blueprint.scss";
```
After that, search `node_modules\@blueprintjs\core\src` directory and replace all `bp-5` namespace with `bp`.

### CSS Files Import Issue
Not sure why but we can't import css files directly but can import sass files.

This doesn't work
```
import "styles/vendors/react-datepicker/style.css";
```

This work
```
import "styles/vendors/react-datepicker/style.scss";
```

## Management Commands
Management commands prefixed with `dev` are utilities meant to be executed in development and test.

Execute routine tasks
```shell
python manage.py send_task routine_fetch_reviews
python manage.py send_task routine_update_connection_profile
```


## Post migrate tasks
**Note: This applies only production enivronment.**
- Login to `dev@onvoard.com` and add billing details. Use actual credit card information from OnVoard.
- Add large amount of credits to OnVoard so that our credit card will never be charged
- Add enterprise subscription to OnVoard with very high limits
- Add user `ryan@onvoard.com`. Add account `Ryan Demo` that will be used for demo-ing
- Add `ryan@onvoard.com` as member for `Ryan Demo`
- Go to admin panel and create a "Staff" group with access to all permission
- Inside admin panel, assign `ryan@onvoard.com` as staff user and add to "Staff" group.
- Verify email

Each sales rep will setup a separate account for demo. For phone subscription, always opt for a US number since it is the cheapest option at $1 per month.

## Compatibility
Tested on Almalinux 9
