#include <bits/stdc++.h>
#define ll long long 
#define endl "\n"
#define IOS ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define mod 1000000007
#define pb push_back
#define buffer cin.ignore(numeric_limits<streamsize>::max(),'\n'); 
#define class_operator bool operator < (const movie & rhs) const {return en<rhs.en;}

using namespace std;

void reader(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
}

#define MAX 8000

int solve1(int x, int rs,int res[])
{
    int carry = 0;
    for (int i=0; i<rs; i++)
    {
        int prod = res[i] * x + carry;
        res[i] = prod % 10; 
        carry  = prod/10;   
    }
    while (carry)
    {
        res[rs] = carry%10;
        carry = carry/10;
        rs++;
    }
    return rs;
}

// ll solve2(ll x,int rs,int res[]){
// 	vector 
// 	for(int i=0; i<rs; i++){
// 		int temp=res[i]-
// 	}
// }

void solve(int n,int rs[],int rs1)
{
    int res[MAX]={0};
    res[0] = 1;
    int res_size = 1;
    for (int x=2; x<=n; x++)
        res_size = solve1(x, res_size,res);
 	vector <int> rt(res_size);
 	int carry=0;
 	int rsize=rs1;
 	for(int i=0; i<rsize; i++){
 		if(res[i]-carry<rs[i]){
 			
 			rt[i]=res[i]+10-carry-rs[i];
 			carry=1;
 		}
 		else{
 			
 			rt[i]=res[i]-carry-rs[i];
 			carry=0;
 		}
 	}
 	for(int i=rsize; i<res_size; i++){
 		if(res[i]-carry<0){
 			
 			rt[i]=res[i]+10-carry;
 			carry=1;
 		}
 		else{
 			
 			rt[i]=res[i]-carry;
 			carry=0;
 		}
 	}
 	for(int i=res_size-1; i>=0; i--){
 		if(rt[i]>0){
 			res_size=i;
 			break;
 		}
 	}
    for (int i=res_size; i>=0; i--)
        cout << rt[i];
}
 
 
int main()
{
	//reader();
	IOS
	int n;
	cin>>n;
	if(n==1){
		cout<<"1"<<endl;
	}
	else if(n==2){
		cout<<"1"<<endl;
	}
	else{
		int res1[MAX]={0};
		int res_size = 1;
		res1[0]=1;
	    for (int x=3; x<=n; x++){
	        res_size = solve1(x, res_size,res1);
	       	if(x%2){
	       		for(int j=0; j<res_size; j++){
	       			if(res1[j]!=0){
	       				res1[j]--;
	       				break;
	       			}
	       			else{
	       				res1[j]=9;
	       			}
	       		}
	       	}
	       	else{
	       		for(int j=0; j<res_size; j++){
	       			if(res1[j]!=9){
	       				res1[j]++;
	       				break;
	       			}
	       			else{
	       				res1[j]=0;
	       			}
	       		}
	       		// solvea(res2);
	       	}
	    }
		// vector <ll> dp(max(n+1,3),0);
		// dp[0]=0;
		// dp[1]=0;
		// dp[2]=1;
		// for(int i=3; i<=n; i++){
		// 	dp[i]=i*dp[i-1];
		// 	if(i%2){
		// 		dp[i]--;
		// 	}
		// 	else{
		// 		dp[i]++;
		// 	}
		// }
		// vector <int> rx;
		// ll y1=dp[n];
		// cout<<dp[n-5]<<endl;
		// cout<<y1<<endl;
		// // while(y1){
		// // 	rx.pb(y1%10);
		// // 	y1/=10;
		// // }
		solve(n,res1,res_size);
	}
	//look down
	return 0;
}

/* stuff you should look for
	* int overflow, array bounds
	* special cases (n=1?)
	* do smth instead of nothing and stay organized
	* WRITE STUFF DOWN
	* DON'T GET STUCK ON ONE APPROACH
*/