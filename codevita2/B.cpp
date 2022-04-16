#include <iostream>
using namespace std;
int mod=1000000007;
unsigned long long factorial(unsigned long long int n)
{
    unsigned long long res = 1, i;
    for (i = 2; i <= n; i++)
        res =(res*i*1LL);
    return res;
}
unsigned long long countDer(unsigned long long int n)
{
   unsigned long long der[n + 1] = {0};
    der[1] = 0;
    der[2] = 1;
  for (int i = 3; i <= n; ++i)
		der[i] = (i - 1) * (der[i - 1] +
							der[i - 2]);

        return der[n];                    
}

unsigned long long int main() {
	int n;
	cin >>n;
	unsigned long long  x=factorial(n);
	cout<<x<<endl;
	unsigned long long y=countDer(n);
	cout<<y<<endl;
	unsigned long long ans = (x-y);
	cout<<ans<<endl;
	return 0;
}
