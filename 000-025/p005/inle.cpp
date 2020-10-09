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

int smallest_divisible(int max){
    int product = 1;
    for (int i = 2; i <= max; i++)
    {
        if (checkprime(i))
        {
            int power = 1;
            while (power * i <= max)
            {
                power *= i;
            }  
            product *= power;
        } 
    }  
    return(product);
}

int main(){
    std::cout << smallest_divisible(20) << "\n";
}