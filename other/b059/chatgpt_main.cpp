#include <iostream>
#include <queue>
using namespace std;

int ix[8] = {3, 3, -3, -3, 1, -1, 1, -1};
int iy[8] = {1, -1, 1, -1, 3, 3, -3, -3};
int table[101][101];

int main() {
    int n, x, y, dog_x, dog_y, target_x, target_y;
    while (cin >> n) {
        // 初始化表格
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                table[i][j] = 0;  // 清空狀態
            }
        }
        
        // 輸入障礙物位置
        for (int i = 0; i < n; i++) {
            cin >> x >> y;
            table[x][y] = 1;
        }

        
        cin >> dog_x >> dog_y >> target_x >> target_y;

        //BFS
        queue<pair<int, int>> q;
        q.push({dog_x, dog_y});
        table[dog_x][dog_y] = 1;

        bool found = false;
        int cur_cost = 0;


        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                auto [x, y] = q.front();
                q.pop();
                
                // 找到目標
                if (x == target_x && y == target_y) {
                    cout << cur_cost << endl;
                    found = true;
                    break;
                }

                for (int k = 0; k < 8; k++) {
                    int nx = x + ix[k], ny = y + iy[k];
                    if (nx < 0 || nx > 99 || ny < 0 || ny > 99)  // 邊界檢查
                        continue;

                    if (table[nx][ny] != 1) {
                        if ((ix[k] == 3 && x + 1 <= 99 && table[x + 1][y] != 1) ||
                            (ix[k] == -3 && x - 1 >= 0 && table[x - 1][y] != 1) ||
                            (iy[k] == 3 && y + 1 <= 99 && table[x][y + 1] != 1) ||
                            (iy[k] == -3 && y - 1 >= 0 && table[x][y - 1] != 1)) {
                            q.push({nx, ny});
                            table[nx][ny] = 1;
                        }
                    }
                }
            }

            if (found) break;
            cur_cost++;
        }

        if (!found) {
            cout << "impossible" << endl;
        }
    }
}