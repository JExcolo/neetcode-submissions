# from math import sqrt, pow, abs
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_list = []
        
        for point in points:
            x, y = point[0], point[1]
            dist = x ** 2 + y ** 2
            point_list.append([dist, [x, y]])
        
        self.quickSort(point_list, 0, len(point_list) - 1)
        output = []
        for i in range(k):
            output.append(point_list[i][1])
        return output

    def quickSort(self, arr, s, e):
        if  s >= e:
            return
        
        l = s

        for i in range(s, e):
            if arr[i][0] < arr[e][0]:
                arr[l], arr[i] = arr[i], arr[l]
                l += 1
        
        arr[l], arr[e] = arr[e], arr[l]


        self.quickSort(arr, s, l - 1)
        self.quickSort(arr, l + 1, e)
            