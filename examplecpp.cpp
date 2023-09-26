#include <iostream>
#include <sstream>
#include <string>
using namespace std; 
   
int main() 
{ 
    string str = "Simple Questions To Check"; 
     
    istringstream s(str);  
    string word; 
    s.str(str); s.clear();
    double a,b,c,d;
   
    int count = 0; 
    // while (s >> word) 
    //     count++;
         
    // cout << " Number of words in given string are: " << count; 
    s >> a >> b >> c >> d;
    cout << a << b << c << d;
    return 0; 
}