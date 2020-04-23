#include <iostream>
#include <vector>
#include <cmath>

int count_prime_factors(int var){
    //Determines count of var's number of factors NOTE: includes number, but includes 1
    int count = 1;

    for (int factor = 2; var != 1; factor++)
    {
        if( var % factor == 0)
        {
            count += 1;
            var /= factor;

        }
    }
    return count;
}

int distinct_factors_above_min(int var, int min){
    //Determines whether var's number of distinct factors is abovea minimum
    int count = 0;

    for (int factor = 2; var != 1; factor++)
    {
        if( var % factor == 0)
        {
            count += 1;
            while (var % factor == 0)
                {
                    var /= factor;
                }
        }

        if (count >= min)
        {
            return true;
        }
    }
    return false;
}

int main()
{
    bool not_found = true;
    int minimum = 4;
    for (int i = 2; not_found; i++)
    {
        if (distinct_factors_above_min(i, minimum) and distinct_factors_above_min(i + 1, minimum) and distinct_factors_above_min(i + 2, minimum) and distinct_factors_above_min(i + 3, minimum))
        {
            not_found = false;
            std::cout << i;
        }
    }
    
}