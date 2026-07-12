class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {}
        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1
        
        s2Count = {}

        for i in range(len(s2)):
            substring = s2[i : i + len(s1)]
            matches = 0

            for c in substring:
                if c not in s1Count:
                    break

                s2Count[c] = s2Count.get(c, 0) + 1

                if s1Count[c] < s2Count[c]:
                    matches -= 1
                    break
                elif s1Count[c] == s2Count[c]:
                    matches += 1

            if matches == len(s1Count):
                return True
  
            s2Count.clear()

        return False
        
