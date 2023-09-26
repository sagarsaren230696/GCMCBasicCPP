#include <stdlib.h>
#include <chrono>
#include <stdio.h>
#include <iostream>
#include <random>
#include <math.h>
#include <time.h>
#include <vector>
#include <string>
//#include <mcheck.h>
#include <assert.h>

double x_old = 9.98;
double x = 0;
double x_d = -0.8;
double L = 10;
double N_ch4 = 100;
int main(){
    // printf("%.2f \n",round (x_d / L));
    // x_d = x_d - L * round (x_d / L);
    // printf("%.2f",x_d);

    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::mt19937 generator (seed);
    // uniformly distributed real no in [0,1]
    std::uniform_real_distribution<double> uniform01(0.0, 1.0); 
    // uniformly distributed int; initialize with bogus range, will change later
    std::uniform_int_distribution<int> uniformint(0, 10); 
    // For picking a move: insertion, deletion, translation
    std::uniform_int_distribution<int> movepicker(0, 2); 

    decltype(uniformint.param()) new_range(0, N_ch4 - 1);
    uniformint.param(new_range);
    int which_ch4 = uniformint(generator);
    double dx = 0.1 * (uniform01(generator) - 0.5);
    x = fmod(x_old + dx,  L);
    printf("%.2f,%.2f,%.2f,%.2f",x_old,dx,x,x_old + dx);
}