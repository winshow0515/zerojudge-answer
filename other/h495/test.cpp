#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    switch(n){
        case 0:
        case 1:
            cout << -1 << endl;
            break;
        case 2:
            cout << 1 << endl;
            break;
    }
}