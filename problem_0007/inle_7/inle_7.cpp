#include <iostream>
#include <cmath>

bool checkprime(int value){
    int factor = 2;
    double sqrt = std::pow(value, 0.5);
    while(factor <= sqrt){
        if (value % factor == 0){
            return(false);
        }
        factor ++;
    }
    return(true);
}

int nthprime(int n){
    int count = 0;
    int num = 1;
    while (count < 10001)
    {
        num ++;
        if (checkprime(num))
        {
            count ++;
        }
    }
    return num;
}

int main(){
    std::cout << nthprime(10001) << "\n";
}