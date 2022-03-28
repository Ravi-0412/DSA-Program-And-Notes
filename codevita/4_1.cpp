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

void solve(int j,vector <int> &v,vector <int> &a,vector <int> &res,int *mi,int tmi,int *ci,int tci,int sum,int k){
	int az=a.size();
	if(sum==k){
		if(*ci<tci){

			for(int i=0; i<az; i++){
				res[i]=a[i];
				//a[i]=0;
			}
			*ci=tci;
		}
		else if(*ci==tci){
			if(*mi>tmi){
				for(int i=0; i<az; i++){
					res[i]=a[i];
					//a[i]=0;
				}
				*mi=tmi;
			}

		}
		return ;
	}
	if(sum>k){
		return;
	}
	//cout<<sum<<endl;
	for(int i=j; i<az; i++){
		// cout<<a[i]<<" ";
		a[i]++;
		if(a[i]==1){
			solve(i,v,a,res,mi,tmi+1,ci,tci+1,sum+v[i],k);
		}
		else{
			// a[i]++;
			solve(i,v,a,res,mi,tmi+1,ci,tci,sum+v[i],k);
			// a[i]--;
		}
		a[i]--;
	}
}

int main()
{
	// reader();
	// IOS
	// int t;
	// cin>>t;
	// while(t--)
	// {
		int n;
		cin>>n;
		vector <int> v(n);
		for(int i=0; i<n; i++){
			cin>>v[i];
		}
		int k;
		cin>>k;
		vector <int> a(n,0);
		vector <int> res(n,0);
		int mi=INT_MAX,ci=0;
		solve(0,v,a,res,&mi,0,&ci,0,0,k);
		map <int,int> m;
		for(int i=0; i<n; i++){
			if(res[i]){
				m[v[i]]=res[i];
			}
			// cout<<a[i]<<" ";
			// cout<<res[i]<<" ";
		}
		for(auto itr=m.begin(); itr!=m.end(); itr++){
			cout<<itr->first<<" ";
		}
		cout<<endl;
		for(auto itr=m.begin(); itr!=m.end(); itr++){
			cout<<itr->second<<" ";
		}
		cout<<endl;
	// }
	//look down
	return 0;
}
