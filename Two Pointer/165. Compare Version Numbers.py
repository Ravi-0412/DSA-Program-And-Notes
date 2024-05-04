# Just we have to compare each version removing '0' at start.

# Method1: Removing zero at front using 'lstrip'

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m, n  = len(version1) , len(version2)
        i, j = 0, 0
        while i < m or j < n:
            temp1 = ""
            while i < m and version1[i] != ".":
                temp1 += version1[i]
                i += 1
            i += 1
            temp2 = ""
            while j < n and version2[j] != ".":
                temp2 += version2[j]
                j += 1
            j += 1
            temp1 = temp1.lstrip("0")
            temp1 = int(temp1) if temp1 else 0
            temp2 = temp2.lstrip("0")
            temp2 = int(temp2) if temp2 else 0
            if temp1 > temp2 :
                return 1
            if temp1 < temp2:
                return -1
        return 0

# Method2:
# adding each revision as an element in list and compare them.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        levels1 = version1.split('.')
        levels2 = version2.split('.')
        length = max(len(levels1), len(levels2))

        for i in range(length):
            v1 = int(levels1[i]) if i < len(levels1) else 0
            v2 = int(levels2[i]) if i < len(levels2) else 0
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1

        return 0