# Method 1: 

# just write down and take xor till 8 or 12 ,you will see it is 
# following a sequence of repitition with below conclusions 

def xor_n(n):
    if n==0:
        return 0
    elif n% 4== 0:
        return n
    elif n%4==1:
        return 1
    elif n%4== 2:
        return n+1
    else:   # if n%4== 3
        return 0

print(xor_n(8))
print(xor_n(5))


# Java Code
"""
class Solution {
    public static int xor_n(int n) {
        if (n == 0) return 0;
        else if (n % 4 == 0) return n;
        else if (n % 4 == 1) return 1;
        else if (n % 4 == 2) return n + 1;
        else return 0; // n % 4 == 3
    }

    public static void main(String[] args) {
        System.out.println(xor_n(8));
        System.out.println(xor_n(5));
    }
}
"""

# C++ Code 
"""
#include <iostream>

using namespace std;

int xor_n(int n) {
    if (n == 0) return 0;
    else if (n % 4 == 0) return n;
    else if (n % 4 == 1) return 1;
    else if (n % 4 == 2) return n + 1;
    else return 0; // n % 4 == 3
}

int main() {
    cout << xor_n(8) << endl;
    cout << xor_n(5) << endl;
    return 0;
}
"""