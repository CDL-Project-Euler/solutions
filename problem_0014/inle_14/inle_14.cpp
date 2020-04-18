#include <iostream>

int length_collatz(int number)
{
    int count = 1;
    std::cout << number;
    while (number != 1)
    {
        if(number % 2 == 0)
        {
            number = number/2;
        } 
        else 
        {
            number = 3 * number - 1;
        }
        count ++;
    } 
    return count;
}


int longest_collatz(int64_t max) 
{
    int length;
    int longest;
    int current_len;
    std::cout << max;
    for (int start = 2; start < max; start++)
    {
        current_len = length_collatz(start);

        std::cout << "this happened" << start;

        if (length < current_len)
        {
            length = current_len;
            longest = start;
        }
    }
    return longest;
}

int main(){
    std::cout << longest_collatz(1000000);
}