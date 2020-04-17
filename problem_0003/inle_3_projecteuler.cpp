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

int main(){
    int largest_factor = 0;
    double sqrt_num = std::pow(600851475143, 0.5);
    int current = 1;
    while(current <= sqrt_num){
        bool current_is_prime = checkprime(current);
        if (600851475143 % current == 0 and current_is_prime){
            largest_factor = current;
        }
        current ++;
    }
    std::cout << largest_factor;
}
