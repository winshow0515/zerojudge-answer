//水題h495. 農家樂(Agricola) 
#include <iostream>
using namespace std;
int a(int n){
    switch(n){
        case 0: case 1: return -1;
        case 2: return 1;
        case 3: return 2;
        case 4: return 3;
        default: return 4;
    }
}
int bd(int n){
    switch(n){
        case 0: return -1;
        case 1: return 1;
        case 2: return 2;
        case 3: return 3;
        default: return 4;
    }
}
int ce(int n){
    switch(n){
        case 0: return -1;
        case 1: case 2: case 3: return 1;
        case 4: case 5: return 2;
        case 6: case 7: return 3;
        default: return 4;
    }
}
int f(int n){
    switch(n){
        case 0: return -1;
        case 1: case 2: return 1;
        case 3:  case 4: return 2;
        case 5: case 6: return 3;
        default: return 4;
    }
}
int g(int n){
    switch(n){
        case 0: return -1;
        case 1: return 1;
        case 2: case 3:  return 2;
        case 4: case 5: return 3;
        default: return 4;
    }
}
int main(){
    int T, A,B,C,D,E,F,G,H,I,J,K,L,M;
    cin >> T;
    while (T--){
        cin >>A>>B>>C>>D>>E>>F>>G>>H>>I>>J>>K>>L>>M;
        int total = 0;
        total += a(A)+bd(B)+ce(C)+bd(D)+ce(E)+f(F)+g(G) -H+I+J+2*K+3*L+M;
        cout << total << endl;
    }
    return 0;
}