# 4월 1일 수정 예정

def quick_sort(x):
    def recursive(start, end):
        if start >= end:
            return

        left, right = start + 1, end
        pivot = x[start]

        while left <= right:
            while left <= right:
                if x[right] < pivot:
                    break
                right -= 1 
            while left <= right:
                if x[left] > pivot:
                    break
                left += 1

            if right >= left:
                x[left], x[right] = x[right], x[left]
            
        x[right], x[start] = x[start], x[right]

        recursive(start, right - 1)
        recursive(right+1, end)

    recursive(0, len(x) - 1)
    print(x)

s = [4, 7, 9, 6, 3, 5]
a = [5, 24 , 5, 7, 8, 9, 4, 8, 12, 7, 32, 7, 2]

quick_sort(a)