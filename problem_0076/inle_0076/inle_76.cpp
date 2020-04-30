#include <iostream>
#include <vector>

int summations_counting(int stop)
{
    //Includes the number. I learned about this method at https://www.mathblog.dk/project-euler-76-one-hundred-sum-integers/. 
    //But I learned about dynamic programming, so I don't see a problem with it :).
    int N = 1;
    std::vector<long int> ways (stop + 1,0);
    ways[0] = 1;
    for (int N = 1; N < stop; N++)
    {
        for(int N2 = N; N2 <= stop; N2++)
        {
            ways[N2] += ways[N2 - N];
        }
    }
    return ways[stop-1];
}

int main()
{
    std::cout << summations_counting(100) << "\n";
}