# Just do what question is telling to do.

class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        comp = ""
        i = 0
        while i < n:
            j = i + 1
            while j < n and word[j] == word[j -1]:
                j += 1
            cnt = j - i
            if cnt <= 9:
                comp += str(cnt) + word[i]
            else:   
                q, r = divmod(cnt, 9)
                comp += q *(str(9) + word[i])
                # for k in range(q):
                #     comp += str(9) + word[i]
                if r != 0:
                    comp += str(r) + word[i]
            i = j
        return comp


# Better way to write.
# Run the inside while loop maximum '9' times for same chosen character.
class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        comp = ""
        i = 0
        while i < n:
            cnt = 0
            c = word[i]
            while i < n and word[i] == c and cnt < 9:
                i += 1
                cnt += 1
            comp += str(cnt) + c 
        return comp