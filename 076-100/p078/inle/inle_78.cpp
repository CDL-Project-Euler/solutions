#include <iostream>
#include <vector>

std::vector<int> carry_vector(std::vector<unsigned long int> vect, int base = 10)
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

unsigned long long int coin_partitions(int factor)
{
    std::vector<unsigned long int> N = {1};
    std::vector<unsigned long int> ways = {1};
    while (true)
    {
        if (ways[0] == 0)
        {
           return N; 
        }
        N[0] += 1;
        ways += N/2;
    }
}



int main()
{
    std::cout << coin_partitions(1000000) << "\n";
}