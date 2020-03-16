class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if not arr: return True
        arr.sort()
        ans = []
        c = collections.Counter(arr)
        for i in c:
            ans.append(c[i])
        
            
        return len(set(ans)) == len(set(arr))
