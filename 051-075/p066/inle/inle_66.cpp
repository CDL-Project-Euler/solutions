#include <iostream>
#include <cmath>

//I solved this with a lot slower algorithm. I tried to optimize it and broke it :/
int diophantine_x_min(int d_max) 
{
    //Find the value of D ≤ d_max in minimal solutions of x for which the largest value of x is obtained.
    int x_max = 0;
    int d_at_x_min = 0;
    for (int d = 2; d <= d_max; d++) //loops through d's
    {
        long double sqrt_d = sqrt(d);
        if (sqrt_d - floor(sqrt_d) != 0)
        {
            for (int y = 1; true; y += 1) //loops through y's until it finds a viable x
            {
                long long int x = sqrt(d*pow(y, 2)+1);
                long double difference = pow(x, 2) - (d*pow(y, 2));
                if (difference == 1 and x > 0) // By the equation if x is a positive integer
                {
                    if(x > x_max) // if x is greater than x_max
                    {
                        x_max = x;
                        d_at_x_min = d;
                        std::cout << d_at_x_min << " : " << x_max << "\n";
                    }
                    break;
                }
            }
        }
    }
    return d_at_x_min;
}

int main()
{
    std::cout << diophantine_x_min(1000) << "\n";
}
