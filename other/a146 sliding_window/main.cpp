#include <iostream>
#include <deque>
using namespace std;
int n, k, i;
int a[1000000];
int main(){
    //加了下面兩行就不會TLE了
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    while (cin >> n >> k){
        for (i=0; i<n; i++)
            cin >> a[i];

        deque<int> dq;

        for (i=0; i<n; i++){
            while (dq.size() && dq.front() <= i-k)
                dq.pop_front();
            while (dq.size() && a[dq.back()] > a[i])
                dq.pop_back();
            dq.push_back(i);

            if (i == k-1)
                cout << a[dq.front()];
            if (i > k-1)
                cout  << ' ' << a[dq.front()];
        }
        if (k > n) //k>n特殊處理
            cout << a[dq.front()];
        cout << "\n";

        //maximum
        dq.clear();
        for (i=0; i<n; i++){
            while (dq.size() && dq.front() <= i-k)
                dq.pop_front();
            while (dq.size() && a[dq.back()] < a[i])
                dq.pop_back();
            dq.push_back(i);

            if (i == k-1)
                cout << a[dq.front()];
            if (i > k-1)
                cout  << ' ' << a[dq.front()];
        }
        if (k > n) //k>n特殊處理
            cout << a[dq.front()];
        cout << "\n";
    }
}