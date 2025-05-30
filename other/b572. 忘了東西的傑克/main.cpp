#include<iostream>
using namespace std;

int main(){
    
    //input
    int n, h1, m1, bus_h2, bus_m2, need;
    cin >> n;
    
    while (n--){
        cin >> h1 >> m1 >> bus_h2 >> bus_m2 >> need;
        //現在時間+來回時間 compare with 公車時間
        //相加
        h1 += (m1 + need)/60;
        m1 = (m1+need)%60;
        if (h1 > bus_h2){
            cout << "No" << endl;
        }
            
        else if (h1 == bus_h2 and m1 > bus_m2){
            cout << "No" << endl;
        }
        else
            cout << "Yes" << endl;
    }
}