#include <iostream>
#include <cmath>

int main(){
    float min_dist_n = 3;
    float min_dist_d = 7;
    float min_dist = 1;
    float n;
    for(float d = 8; d <= 1000000; d ++) {
        if (int(d) % 7 != 0) { // The closest fraction simplifies to 3/7 if d is divisible by 7
            n = floor(d * 3/7);
            if (3.0/7.0 - n / d < min_dist) {
                min_dist_n = n;
                min_dist_d = d;
                min_dist = 3.0/7.0 - n/d;
            }
        }
    }
    std::cout << min_dist_n << "/" << min_dist_d << "\n";
}