

# fixed window just iterate and monitor start
# variable window need monitor and move both start and end



# Sliding Variable Window Master Template (MEMORISE THIS)
# from collections import defaultdict

# def sliding_window(arr, k):
#     left = 0
#     window = defaultdict(int)
#     result = 0

#     for right in range(len(arr)):
#         window[arr[right]] += 1

#         while condition_not_met(window):
#             window[arr[left]] -= 1
#             if window[arr[left]] == 0:
#                 del window[arr[left]]
#             left += 1

#         result = max(result, right - left + 1)

#     return result
