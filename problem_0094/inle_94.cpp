#include <iostream>
using namespace std;

//solved using pells equation & substitution

int main() {
    long int aTimes3, areaTimes3;
    long int x = 2;
    long int y = 1;
    long int limit = 1000000000;
    long int perimSum = 0;
    while (true) {
        aTimes3 = 2 * x + 1;
        areaTimes3 = y * (x + 2);

        if (aTimes3 > limit) break;

        if (aTimes3 > 0 && areaTimes3 > 0 && aTimes3 % 3 == 0 && areaTimes3 % 3== 0) {
            cout << aTimes3 << " " << aTimes3 / 3 << "\n";
            perimSum += aTimes3 + 1;
        };

        aTimes3 = 2 * x - 1;
        areaTimes3 = y * (x - 2);

        if (aTimes3 > 0 && areaTimes3 > 0 && aTimes3 % 3 == 0 && areaTimes3 % 3 == 0) {
            perimSum += aTimes3 - 1;
        };
        x = 2 * x + 3 * y;
        y = 2 * y + (x - 3 * y)/2;
    }
    cout << perimSum << "\n";
}