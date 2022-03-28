#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define int long long
bool check(int n)
{
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}
int rec(int x, int y)
{
    if (check(x) || check(y))
        return 0;
    return x * y / ((x - y) * (x - y));
}
void solve()
{
    int f, p1, p2;
    cin >> f >> p1 >> p2;
      bool flag = false;
    if (check(p1) && f==0)
    {
        cout << p1 << " " << p1 + 1 << endl;
        return ;
    }
   
    else
    {
        int f1 = rec(p1, p2);
        for (int i = p1; i <= p2 - 1; i++)
        {
            for(int j=i+1;j<=p2;j++)
            {
                if(rec(i,j)>=f)
                {
                    cout<<i<<" "<<j<<endl;
                    flag=true;
                    break;
                }
            }
            if(flag==true)
            break;
        }
    }
    if (flag == false)
        cout << "None" << endl;
}
signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    // cin >> t;
    // while (t--)
    solve();
    return 0;
}
