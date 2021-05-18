/* 
 * Author :  reyngs
 * Date   :  2021 may 17 17:18:35
 */

#include <bits/stdc++.h>
using namespace std;

int t,x,y;
char s[100050];

int main(){
    cin >> t;
    while(t--){
		scanf("%d%d%s", &x,&y,s);
		for (int i=0; s[i]; ++i){
			if (s[i]=='R'&&x>0) --x;
			if (s[i]=='L'&&x<0) ++x;
			if (s[i]=='U'&&y>0) --y;
			if (s[i]=='D'&&y<0) ++y;
		}
		puts(x==0&&y==0?"YES":"NO");
    }
}
