#include <iostream>
#include <vector>
#include <numeric>

std::vector<int> carry_vector(std::vector<int> vect, int base = 10)
{
    //decimalizes vectors (carries values to the end) 
    for (int i = 0; i < vect.size()-1; i++)
    {
        vect[i+1] += vect[i]/base;
        vect[i] %= base;
    }

    for(int i = vect.size() -1; vect[i] >= base; i ++)
    {
        vect.push_back(vect[i]/base);
        vect[i] %= base;
    }
    return vect;
}

std::vector<int> scalar_mult_vector(std::vector<int> vect, int scale)
{
    for (int i = 0; i < vect.size(); i++)
    {
        vect[i] *= scale;
    }
    return carry_vector(vect);
}

int main()
{
    int largest_sum = 0;
    for (int a = 2; a < 100; a++)
    {
        for (int b = 50; b < 100; b++)
        {
            std::vector<int> power(1, a);
            for (int i = 0; i < b; i++)
            {
                power = scalar_mult_vector(power, a);
            }
            int sum_power = accumulate(power.begin(), power.end(), 0);

            if (sum_power > largest_sum)
            {
                largest_sum = sum_power;
            }
        }
    }
    std::cout << largest_sum << "\n";
}