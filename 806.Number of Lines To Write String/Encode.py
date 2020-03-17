class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        
        tmp = 0
        count = 1
        for word in S:
            tmp += widths[(ord(word) - 97)]
            if tmp > 100:
                count += 1
                tmp = widths[(ord(word) - 97)]
        
        return count, tmp
