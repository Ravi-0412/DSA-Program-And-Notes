#include<bits/stdc++.h>
using namespace std;

int max_distinct_cups=INT_MIN;
int min_num_cups=INT_MAX;
vector<int>res(10);
int c=0;

void solve(int cnt_max,vector<int>v, int n ,int x, int sum,vector<int>num, vector<bool>vis){

              
            //  cout<<sum<<endl;
            
              if(sum==x)
              {
                  //cout<<sum<<endl;
                  int distinct_cups=0,num_cups=0;
                  set<int>s;
                  
                  for(int k=0;k<n;k++)
                  {
                      if(vis[k])
                      s.insert(v[k]),num_cups+=num[k];
                      
                      distinct_cups=s.size();
                      
                      if(distinct_cups>max_distinct_cups)
                      res=num,max_distinct_cups=distinct_cups;
                      else if(distinct_cups==max_distinct_cups)
                      {
                          if(num_cups<min_num_cups)
                          res=num,min_num_cups=num_cups;
                      }     
                  }
                  
                //   for(auto z : res)
                //   cout<<z<<" ";
                //   cout<<endl;

                  for(int k=0;k<n;k++) num[k]=0;
                  return ;
              }
              else if(sum>x){
                
                  for(int k=0;k<n;k++) num[k]=0;
                  return ;
              }
   
    for(int i=0;i<n;i++)
    {
        if(vis[i])
        continue;

        for(int j=1;j<=cnt_max;j++)
        {
              if(sum+v[i]*j<=x)
              {
                       vis[i]=true;
                       num[i]=j;
                       
                       solve(cnt_max,v,n,x,sum+v[i]*j,num,vis);
                       vis[i]=false;           
              }
              
        }
    }
}

int main(){

  int n,x,mi=INT_MAX;
  cin>>n;
  vector<int>v;
  vector<int>num(n,0);
  vector<bool>vis(n,false);

  for(int i=0;i<n;i++){
      cin>>x;
      v.push_back(x);
      mi=min(mi,x);
  }
   
   cin>>x;

   int cnt_max=x/mi;
   //cout<<cnt_max<<endl;
   solve(cnt_max,v,n,x,0,num,vis);
   
   vector<pair<int,int>>ans;
   
   for(int i=0;i<n;i++)
   ans.push_back({v[i],res[i]});
   
   sort(ans.begin(),ans.end());
   
   for(int i=0;i<n;i++)
   cout<<ans[i].first<<" ";
   
   cout<<endl;
   
   for(int i=0;i<n;i++)
   cout<<ans[i].second<<" ";
   
}