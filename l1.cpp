
#include<iostream>
#include <cmath>

using namespace std;


double findA(double x, double y) {
    const double pi = 3.14159265358979323846;
    double numerator = 2 * std::cos(x - pi/6);
    double denominator = 0.5 + std::pow(std::sin(y), 2);
    return numerator / denominator;
}

double findB(double z) {
    double z_squared = z * z;
    return 1 + z_squared / 3 + z_squared / 5;
}

int main() {
    double x = 1.0;
    double y = 2.0;
    double resultA = findA(x, y);
    std::cout << "The result of the expression A is: " << resultA << std::endl;
    double z = 3.0;
    double resultB = findB(z);
    std::cout << "The result of the expression B is: " << resultB << std::endl;

    return 0;
}
