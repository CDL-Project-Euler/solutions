// A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
//For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
// A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
// As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
//By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
//However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
// Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#include <iostream>
#include <vector>
#include <math.h>

bool is_abundant(int var)
{
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
    if(sqrt == floor(sqrt))
    {
        count += sqrt;
    }

    if (count > var)
    {
        return true;
    }
    return false;
}


int sum_non_abundant(int max)
{
    //Determines the sum of non abundant numbers under max
    int current_index = -1;

    std::vector<int> abundants;
    std::vector<bool> not_is_sum(max, true);

    for (int i = 12; i <= max - 11; i++)
    {
        if (is_abundant(i))
        {
            abundants.push_back(i);
            current_index += 1;
            for (int index2 = 0; index2 <= current_index and abundants[index2] + i < max; index2++)
            {
                not_is_sum[abundants[index2] + i - 1] = false;
            }   
        }
    }

    int sum_non_abundant = 0;
    for (int i = 1; i < max; i++)
    {
       if (not_is_sum[i - 1])
       {
           sum_non_abundant += i;
       }
    }
    return sum_non_abundant;
}

int main(){
    std::cout << sum_non_abundant(28126) << "\n";
}