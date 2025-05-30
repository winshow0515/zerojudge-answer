#include <iostream>
using namespace std;

string s1, s2;
int s1_len, s2_len, i, j;

main(){
	while (cin >> s1_len >> s1 >> s2_len >> s2){
		int dp[s1_len+1][s2_len+1] = {};
		for (i=0; i<=s1_len; i++)
			dp[i][0] = i;
		for (i=0; i<=s2_len; i++)
			dp[0][i] = i;
		
		for (i=1; i<=s1_len; i++){
			for (j=1; j<=s2_len; j++){
				if (s1[i-1] == s2[j-1])
					dp[i][j] = dp[i-1][j-1];
				else
					dp[i][j] = min(min(dp[i][j-1], dp[i-1][j]), dp[i-1][j-1])+1;
			}
		}
		cout << dp[s1_len][s2_len] << endl;
	}
}
