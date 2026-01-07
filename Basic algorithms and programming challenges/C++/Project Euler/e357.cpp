#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;
int main(){	
	long long total = 1;
	long long obj = 100000000;
	long long limit = 1000000000;
	vector<bool> numbers;	
	for (int i=0;i<=limit;i++){numbers.push_back(false);}	
	string line;	
	ifstream myfile("C:\\Users\\nicho\\Desktop\\include\\Auxillery\\primes.txt");
  	if (myfile.is_open())  		
  		{
    	while ( getline (myfile,line) )
    		{   			
    			long long val = stoll(line);
    			if (val>obj){break;}
      			numbers[val]=true;
    		}    	
  	}
	myfile.close();	
	for (int i = 2;i<=obj;i+=4)
	{
		bool add = false;
		if ((i/2)%2==1)
		{
			bool add = true;			
			if (!numbers[i+1]){add=false;continue;}
			if (!numbers[2+i/2]){add=false;continue;}	
			for (int j = 3;j<=sqrt(i);j++)
			{
				if (i%j==0)
				{
					long long num = j + i/j;
					if (!numbers[num]){add=false;continue;}
				}				
			}
			if (add==true)
			{
				total+=i;
			}
		}		
	}
	
	cout <<total;
	return 0;	
}
