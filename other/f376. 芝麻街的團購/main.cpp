#include <iostream>
#include <algorithm>
using namespace std;
long long n;
long long arr[100000];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    for (int i=0; i<n; i++)
        cin >> arr[i];
    sort(arr, arr+n);

    long long mid = n/2;
    if (n%2)//odd
        cout << arr[mid];
    else
        cout << arr[mid-1];
}