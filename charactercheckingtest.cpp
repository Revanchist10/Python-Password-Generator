#include <iostream>
using namespace std; 

int main()
{
    char testArr[] = "AABC"; //array to check for similar characters
    
    cout<<"Current index is: "<< testArr<<endl; //print the original array

    for (int i = 0; i<4; i++)
    {
        if(i>0) //only check for same characters after the 0th index
        {
            if(testArr[i] == testArr[i-1]) //make sure that the ith index is not the same as the previous index
            {
                cout<<"index "<<i<< " is the same as its neighbor index "<<i-1<<" replacing the letter with C"<<endl; //print that two indexes are matching, and what char the ith index will be replaced with
                testArr[i] = 'C'; //replace the ith index with a new char
            }
        }
    }
    cout<<"New index is: "<<testArr; //print the new, fixed index that follows the rules
    return 0; 
}