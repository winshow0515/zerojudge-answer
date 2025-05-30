//AC
#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main(){
    int M, S, N;
    cin >> M >> S >> N;
    vector<int> x(N); 
    for (int i=0; i<N; i++){
        cin >> x[i];
    }
    
    int total_rented = accumulate(x.begin(), x.end(), 0);
    int required_empty = M-S;

    if (S <= M-total_rented){
        cout << 0 << endl;
        return 0;
    }

    vector<bool> dp(required_empty+1, false);
    dp[0] = true;

    for (int i=0; i<N; i++){
        if (x[i] > required_empty)
            continue;
        for (int j=required_empty; j >= x[i]; j--){
            dp[j] = dp[j] || dp[j-x[i]];
        }
    }

    for (int j=required_empty; j >= 0; j--){
        if (dp[j]){
            cout << total_rented-j << endl;
            return 0;
        }   
    }

    cout << total_rented << endl;
    return 0;
}