#include <iostream>
#include <cmath> 
using namespace std;

int fib(int n) { 
  double phi = (1 + sqrt(5)) / 2; 
  return round(pow(phi, n) / sqrt(5)); 
} 

int main(){
    int input;
    cin >> input;
    while(input > 0){
        input--;
        int n;
        cin >> n;
        // cout << n << endl;
        int x = log2(n);
        // cout << x << endl;
        int z = pow(2,x) - 1;
        // cout << z << endl;
        // cout << fib(z) << endl;
        cout << fib(z)%10 <<endl;
    }
    return 0;
}
