#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;
//uses a sieve to generate primes 
int main(){
	std::vector<bool> numbers={false,false};
	int limit = 1000000000;
	for (int i=0;i<limit-2;i++){numbers.push_back(true);}
	for (int i=2;i<limit;i++){
		int k = 2;
		while (i*k<limit){
			numbers[i*k]=false;
			k+=1;
		}
		
		
	}
	
	ofstream file;
	file.open("C:\\Users\\nicho\\Desktop\\include\\Auxillery\\primes.txt");
	for (int i=0;i<limit;i++)
	{
		if (numbers[i]==true)
		{
			file<<to_string(i)<<"\n";
		}
		
	}
	
	file.close();
	return -1;
	
}
