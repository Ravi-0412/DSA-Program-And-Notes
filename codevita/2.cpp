

#include <bits/stdc++.h>

using namespace std;

// void reader(){
// 	#ifndef ONLINE_JUDGE
// 	freopen("input.txt","r",stdin);
// 	freopen("output.txt","w",stdout);
// 	#endif
// }

int main()
{
	// reader();
	// IOS
		int m,n;
		cin>>m>>n;
		vector <string> a(m);
		for(int i=0; i<m; i++){
			cin>>a[i];
		}
		int cs=0,es=0;
		for(int i=0; i<n; i++){
			int ch=0,cn=0;
			for(int j=0; j<m; j++){
				if(a[j][i]=='C' && ch==0){
					ch=m-j-1;
					//cn++;
				}
				if(a[j][i]=='C'){
					cn++;
				}
			}
			if(ch){
				cs+=cn;
				es+=ch*2;
				continue;
			}
			int x1=0;
			if(a[m-1][i]=='H'){
				for(int j=m-1; j>=0; j--){
					if(a[j][i]!='H'){
						x1=m-j-1;
						break;
					}
				}
			}
			es+=x1*2;

		}
		cout<<cs<<" "<<es<<endl;
	//look down
	return 0;
}