# logic: we can get ans(for addition) directly by taking 'xor'.
# but in case both bit are same  then we will have to forward the carry to the just next bit and so on.
# for forwarding the carry we will do '&' and will do left shift.

# this giving TLE in Python.
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b!= 0:
            temp= (a & b) << 1
            a= a ^ b
            b= temp
        return a

# the same approach got submitted in Java.
class Solution {
    public int getSum(int a, int b) {
      while(b !=0 ) {
        int temp = (a & b) << 1;
        a = a ^ b;
        b = temp;
      }
      return a;    
    }
}

