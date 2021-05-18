/* 
 * Author :  reyngs
 * Date   :  2021 abr 21 12:43:37
 */
// https://codeforces.com/problemset/problem/1512/B
#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define REP(i,a,b) for(int i=a; i<b; i++)
#define PB push_back
#define MP make_pair

int main(){
    int t;
    cin >> t;
    
    while(t--){
	int n;
	cin >> n;
	vector<int> x,y;
	string m[400];
	REP(i,0,n){
	    cin >> m[i];
	    REP(j,0,n){
		if(m[i][j]=='*'){
		    x.PB(i);
		    y.PB(j);
		}
	    }
	}
	if (x[0]==x[1]){
	    x[1]=x[0]==0;
	}
    	if (y[0]==y[1]){
	    y[1]=y[0]==0;
    	}
	for (int i : x)
		for (int j : y)
			m[i][j]='*';
	REP(i,0,n){
		cout << m[i] << "\n";
	}
    }
    return 0;
}	
