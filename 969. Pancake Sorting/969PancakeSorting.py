import sys
class Solution(object):
    def pancakeSort(self, arr):
        def pancake_flip(arr,k):
            return arr[:k][::-1]+arr[k:]
        # print(pancake_flip(arr,3))
        n=len(arr)
        i=n-1
        ans=[]
        while i>=0:
            
            curr_max=arr[i]
            curr_max_index=i
            j=i-1
            
            while j>=0:
                if arr[j]>curr_max:
                    curr_max=arr[j]
                    curr_max_index=j
                j-=1
            if curr_max>arr[i]:
                # print(i,arr,curr_max,curr_max_index)
                arr=pancake_flip(arr,curr_max_index+1)
                # print(i,arr,curr_max,curr_max_index)
                arr=pancake_flip(arr,i+1)
                ans.append(curr_max_index+1)
                ans.append(i+1)
                # print(i,arr,curr_max,curr_max_index)
            i-=1
        return ans