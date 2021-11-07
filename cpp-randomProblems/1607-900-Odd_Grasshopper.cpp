/*
 *  Author : greyngs
 *  Date   : 2021 Nov 6 22:00:30
 */
// http://codeforces.com/problemset/problem/1607/B
#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
   int t;
   cin>>t;
   while(t--){
      ll x,n;
      cin>>x>>n;
      ll i;
      for(i=n-n%4+1; i<=n; i++){
         if(x%2==0) x-=i;
	 else x+=i;	 
      }
      cout<<x<<endl;
   }
   return 0;
}
