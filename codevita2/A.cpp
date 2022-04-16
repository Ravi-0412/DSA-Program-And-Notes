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

int main()
{
	//reader();
	IOS
	int n;
	cin>>n;
	vector <string> a(n);
	for(int i=0; i<n; i++){
		cin>>a[i];
	}
	string s;
	cin>>s;
	int l=s.length();
	vector <int> v;
	string res="";
	for(int i=0; i<l; i++){
		if(i==l-1){
			res+=s[i];
			int y=stoi(res);
			v.pb(y);

		}
		else if(s[i]==','){
			int y=stoi(res);
			v.pb(y);
			res="";
		}
		else{
			res+=s[i];
		}

	}
	int g=v.size();
	vector <int> v2(g);
	int g2=g/2;
	int j1=0;
	for(int i=g2; i<g; i++){
		v2[j1]=v[i];
		j1++;
	}
	for(int i=g2-1; i>=0; i--){
		v2[j1]=v[i];
		j1++;
	}
	int al1=a[0].length();
	int cl=0,cl2=0;
	vector <int> v3(n,0);
	for(int j=0; j<n; j++){
		cl=0;
		for(int i=0; i<al1; i++){
			if(a[j][i]=='_'){
				cl++;
			}
		}
		v3[j]=cl;
	}
	for(int i=0; i<g; i++){
		for(int j=0; j<n; j++){
			if(v3[j]>=v2[i]){
				string temp2=to_string(i+1);
				int ajl=a[j].length();
				int k=0,k1=ajl;
				string temp1="";
				for(int i1=0; i1<ajl; i1++){
					if(a[j][i1]=='_'){
						temp1+=temp2;
						k++;
					}
					else{
						temp1+=a[j][i1];
					}
					if(k==v2[i]){
						k1=i1+1;
						break;
					}
				}
				for(int i1=k1; i1<ajl; i1++){
					temp1+=a[j][i1];
				}
				a[j]=temp1;
				v3[j]-=v2[i];
				break;
			}
		}
	}
	for(int i=0; i<n; i++){
		cout<<a[i]<<endl;
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