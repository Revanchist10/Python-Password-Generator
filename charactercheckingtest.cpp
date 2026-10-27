#include <iostream>
using namespace std; 

int main()
{
    char testArr[] = "AABC"; 
    

    cout<<"Current index is: "<< testArr<<endl; 

    for (int i = 0; i<4; i++)
    {
        if(i>0)
        {
            if(testArr[i] == testArr[i-1])
            {
                cout<<"index "<<i<< " is the same as its neighbor index "<<i-1<<" replacing the letter with C"<<endl; 
                testArr[i] = 'C';
            }
        }
        
    }
    cout<<"New index is: "<<testArr; 
    return 0; 
}