#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n, k, x, ans = 0;
    scanf("%d%d", &n, &k);
    int DP0 = 0;
    int DP[n][k+1];
    int last[1000000];
    for (int i=0; i<1000000; i++)
        last[i] = -1;
    
    for (int i=1; i<=n; i++) {
        scanf("%d", &x);
        DP0 = min(DP0+1, i-last[x]);
        last[x] = i;
        for (int cur_k=1; cur_k<=k; cur_k++) {
            DP[i][cur_k] = max(
            DP[i-1][cur_k],
            DP[i-DP0][cur_k-1] + DP0);
            ans = max(ans, DP[i][k]);
        }
    }
    printf("%d\n", ans);
}