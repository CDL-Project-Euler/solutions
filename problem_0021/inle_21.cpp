// Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
// If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
//The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

// Evaluate the sum of all the amicable numbers under 10000.
#include <iostream>
#include <vector>
#include <math.h>

int sum_proper_divisors(int var){
    //Determines sum of var's number of factors NOTE: Does not include number, but includes 1
    int count = 1;
    double sqrt = pow(var, 0.5);

    for (int factor = 2; factor < sqrt; factor++)
    {
        if( var % factor == 0)
        {
            count += factor + var/factor;
        }
    }
    return count;
}

int amicable_sum(int top){
    int sum = 0;
    std::vector<int> numbers;

    for (int i = 0; i <= top; i++)
    {
        numbers.push_back(sum_proper_divisors(i));
    }
    for (int i = 0; i < top; i++)
    {
        int current_sum = numbers[i];
        if (current_sum < numbers.size() and current_sum != i)
        {
            if (numbers[current_sum] == i)
            {
                sum += current_sum;
            }
        }
    }
    return sum;
}

int main(){
    std::cout << amicable_sum(10000) << '\n';
}