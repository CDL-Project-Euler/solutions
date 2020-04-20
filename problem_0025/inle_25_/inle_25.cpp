#include <iostream>
#include <vector>

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

std::vector<int> add_vector_nums(std::vector<int> vector1, std::vector<int> vector2, int base = 10)
{
    /*base vector number manipulation. Note: vectors are put in backwards.*/
    
    if(vector2.size() > vector1.size())
    {
        throw std::invalid_argument("vector 1 must be equal to or larger than vector 2");
    }
    
    for(int i = 0; i < vector2.size(); i++)
    {
        //adds digits and carries (doesn't do last digit)
        vector1[i] += vector2[i];
    }
    return carry_vector(vector1, base);
}

int fib_dig_index(int digits){
    //returns  the index of the first term in the Fibonacci sequence to contain digits digits
    std::vector<int> fib1(1,0);
    std::vector<int> fib2(1,1);
    std::vector<int> fib3;
    for (int index = 1; true; index++)
    {
        
        fib3 = fib2;
        fib2 = add_vector_nums(fib2, fib1);
        fib1 = fib3;
        if (fib2.size() >= digits)
        {
            return index + 1;
        }
    }
}

int main(){
    int fib = fib_dig_index(1000);
    std::cout << fib << "\n";
}