#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define int long long
int rec(int sum, int i, vector< int > &v, vector<int> &dp)
{
    if (sum == 0)
        return 1;
    if (sum < 0)
        return 0;
    if (dp[sum] != -1)
        return dp[sum];
    int ans = 0;
    for (int j = 0; j < v.size(); j++)
    {
        if (v[j] <= sum)
        {
            ans += rec(sum - v[j], i, v, dp);
        }
    }
    return dp[sum]= ans;
}
void solve()
{
    int s, m;
    cin >> s >> m;
    vector<int> dp(s + 1, -1);
    vector<int> v;
    for (int i = 1; i <= m; i++)
    {
        v.push_back(i);
    }
    cout <<rec(s, 0, v, dp)<<endl;
}
signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--)
        solve();
    return 0;
}