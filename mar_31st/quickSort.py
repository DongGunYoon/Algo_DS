# 4월 1일 수정 예정

# def quicksort(x):
#     def recursive(start, end):
#         if start >= end:
#             return

#         left, right = start + 1, end
#         pivot = x[start]

#         while left <= right:
#             while left <= right:
#                 if x[left] > pivot:
#                     break
#                 left += 1
#             while left <= right:
#                 if x[right] < pivot:
#                     break
#                 right -= 1
            
#             if left <= right:
#                 x[left], x[right] = x[right], x[left]

#         x[left], x[start] = x[start], x[left]        
#         recursive(start, left - 1)
#         recursive(left+1, end)

#     recursive(0, len(x) - 1)
#     print(x)