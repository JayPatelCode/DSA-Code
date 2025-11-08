/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
#include<iostream>
using namespace std;

int main()
{
int row,col,i=1;
//      1
//     2 3
//    4 5 6
//   7 8 9 10 

for(row=1;row<=4;row++)
 {
     
     
 for(col=1;col<=4-row;col++)
 cout<<" ";
 
 
for(col=1;col<=row;col=col+1)
cout<<i++;


cout<<endl;
 
 }
 }
 

