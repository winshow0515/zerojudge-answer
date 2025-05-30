#include <iostream>
#include <vector>
using namespace std;
char table[101][101];
int ix[] = {1, 0, -1, 0};
int iy[] = {0, 1, 0, -1};
vector<pair<int, int>> Q[10000];
int main(){
    int n, ans=-1;
    scanf("%d", &n);
    for(int i=0; i<n; i++)
        scanf("%s", table[i]);

    Q[0].push_back({1, 1});
    for(int cur_cost=0; !Q[cur_cost].empty(); cur_cost++){
        for (auto &[x, y] : Q[cur_cost]) {
            if(x == n-2 && y == n-2) {
                cout << cur_cost << endl;
                return 0;
            }
            for(int k=0; k<4; k++){
                int nx = x + ix[k], ny = y + iy[k];
                if(table[nx][ny] == '.'){
                    Q[cur_cost+1].push_back({nx, ny});
                    table[nx][ny] = '#';
                }
            }
        }
    }
    printf("No solution!");
    return 0;
}