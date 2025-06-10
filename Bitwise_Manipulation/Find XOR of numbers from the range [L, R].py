# xor bw two no: 'a' and 'b
# equal to= f(b)^ f(a-1)
# take xor till zero to b and after that  to remove the
# xor result of extra no i.e till 0 to 'a-1'
# again take (xor of zero till 'a-1' with zero till 'b')
# as xor of same no = 0 and since we are taking xor of extra
# no again with themselves ,xor of zero till 'a-1' will cance out 
# and we will get the desired result

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

a= int(input("enter the 1st no: "))
b= int(input("enter the 2nd no: "))
xor1= xor_n(a-1)   # xor to remove the extra no
xor2= xor_n(b)     #  xor from zero till b
print(xor2^xor1)

# Java Code 
"""
import java.util.Scanner;

class Solution {
    // Function to compute XOR from 0 to n using properties
    public static int xor_n(int n) {
        if (n == 0) return 0;
        else if (n % 4 == 0) return n;
        else if (n % 4 == 1) return 1;
        else if (n % 4 == 2) return n + 1;
        else return 0; // n % 4 == 3
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the 1st number: ");
        int a = scanner.nextInt();
        
        System.out.print("Enter the 2nd number: ");
        int b = scanner.nextInt();
        
        int xor1 = xor_n(a - 1); // XOR to remove extra numbers
        int xor2 = xor_n(b);     // XOR from zero till b

        System.out.println(xor2 ^ xor1);
        
        scanner.close();
    }
}
"""

# C++ Code 
"""
#include <iostream>

using namespace std;

// Function to compute XOR from 0 to n using properties
int xor_n(int n) {
    if (n == 0) return 0;
    else if (n % 4 == 0) return n;
    else if (n % 4 == 1) return 1;
    else if (n % 4 == 2) return n + 1;
    else return 0; // n % 4 == 3
}

int main() {
    int a, b;
    cout << "Enter the 1st number: ";
    cin >> a;
    cout << "Enter the 2nd number: ";
    cin >> b;

    int xor1 = xor_n(a - 1); // XOR to remove extra numbers
    int xor2 = xor_n(b);     // XOR from zero till b

    cout << (xor2 ^ xor1) << endl;

    return 0;
}
"""