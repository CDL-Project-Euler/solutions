#include <iostream>
#include <cmath>


bool checkprime(int value){
    if(value == 0 or value == 1)
    {
        return false;
    }

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


int main()
{
    bool not_found = true;
    for (int odd_num = 33; not_found; odd_num += 2)
    {
        for (int i = 0; 2 * pow(i, 2) < odd_num; i++)
        {
            not_found = false;
            if( checkprime(odd_num-2 * pow(i,2)))
            {
                not_found = true;
                break;
            }
        }
        if(! not_found)
        {
            std::cout << odd_num << "\n";
        }
    }
}