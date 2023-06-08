class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans= 0
        for i in range(32):
            # first get the ith bit from right side in a,b,c 
            bit1= (a >> i) % 2   # (a >> i) & 1
            bit2= (b >> i) % 2
            bit_or= bit1 | bit2
            expected_or= (c >> i) % 2
            if bit_or != expected_or:
                # means we have to flip the bits
                if bit_or == 1:
                    # means we have to make 'OR' equal to '1'.
                    # And flip will depend on value of bit1 and bit2. i.e both are '1' then ans+= 2 and if one of them is '1 then ans+= 1
                    ans+= bit1 + bit2
                else: # means we have to make 'OR' equla to '1'.
                    # for this make any of the bit= 1 so ans += 1
                    ans += 1
        return ans


# method 2: getting the bit from MSB
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans= 0
        for i in range(31, -1, -1):

            bit1= (a >> i) & 1
            bit2= (b >> i) & 1
            bit_or= bit1 | bit2
            expected_or= (c >> i) & 1
            print(bit1, bit2)
            if bit_or != expected_or:
                if bit_or == 1:
                    ans+= bit1 + bit2
                else:
                    ans += 1
                print(ans, i, "ans")
        return ans