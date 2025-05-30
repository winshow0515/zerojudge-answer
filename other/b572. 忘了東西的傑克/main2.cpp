#include<iostream>
using namespace std;

int main(){
    
    //input
    int n, h1, m1, h2, m2, need, time1, time2;
    cin >> n;
    
    while (n--){
        cin >> h1 >> m1 >> h2 >> m2 >> need;
        //計算總分鐘數
        time1 = h1 * 60 + m1;
        time2 = h2 * 60 + m2;
        if (time1 + need > time2){
            cout << "No" << endl;
        }
        else{
            cout << "Yes" << endl;
        }
    }
}