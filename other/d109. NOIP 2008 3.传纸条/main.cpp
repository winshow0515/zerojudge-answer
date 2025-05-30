#include <iostream>
#include <algorithm>
#define INF 100000000
using namespace std;
int n, m, grid[50][50], dp[50][50][50][50];

int rec(int xa, int ya, int xb, int yb){
    if (xa+ya+xb+yb == 0) return 0;
    if (xa < 0 || ya < 0 || xb < 0 || yb < 0)
        return -INF;
    if (xa==xb && ya==yb)
        return -INF;
    if (dp[xa][ya][xb][yb])
        return dp[xa][ya][xb][yb];
    return dp[xa][ya][xb][yb] =
        grid[xa][ya] + grid[xb][yb] + max({
            rec(xa-1, ya, xb-1, yb),
            rec(xa-1, ya, xb, yb-1),
            rec(xa, ya-1, xb-1, yb),
            rec(xa, ya-1, xb, yb-1)
        });
}

int main(){
    cin >> m >> n;
    for (int i=0; i<m; i++)
        for (int j=0; j<n; j++)
            cin >> grid[i][j];
    cout << rec(m-1, n-2, m-2, n-1);
    return 0;
}