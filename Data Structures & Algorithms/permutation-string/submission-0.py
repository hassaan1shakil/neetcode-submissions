class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {}
        s2Count = {}

        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1
        
        l = 0
        r = len(s1) - 1
        while r < len(s2):
            substring = s2[l:r+1]
            for c in substring:
                s2Count[c] = s2Count.get(c, 0) + 1
            
            matches = 0
            for key in s2Count.keys():
                if key not in s1Count:
                    break
                if s2Count[key] != s1Count[key]:
                    break
                 
                matches +=1 

            if matches == len(s1Count):
                return True
                
            l += 1
            r += 1
            s2Count.clear()

        return False
        
