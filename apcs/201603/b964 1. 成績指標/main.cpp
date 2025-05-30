#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n, temp, pas = 101, fall = -1;
    vector<int> v;
    cin >> n;
    
    for (int i=0; i<n; i++){
        cin >> temp;
        v.push_back(temp);
        if (temp >= 60)
            pas = min(pas, temp);
        else
            fall = max(fall, temp);
    }
    sort(v.begin(), v.end());
    for (int i=0; i<n-1; i++)
        cout << v[i] << " ";
    
    cout << v[n-1] <<endl;
    if (fall == -1)
        cout << "best case" << endl;
    else
        cout << fall << endl;

    if (pas == 101)
        cout << "worst case" << endl;
    else
        cout << pas << endl;
    return 0;
}