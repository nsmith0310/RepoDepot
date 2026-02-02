#include <iostream>
#include <vector>

//uses a sieve to generate primes 
int main(){
	std::vector<bool> numbers={false,false};
	int limit = 1000000;
	for (int i=0;i<limit-2;i++){numbers.push_back(true);}
	for (int i=2;i<limit;i++){
		int k = 2;
		while (i*k<limit){
			numbers[i*k]=false;
			k+=1;
		}
		
		
	}
	int count = 0;
	for (int i=0;i<limit;i++){
		if (numbers[i]==true){
			count+=1;
			if (count==10001){
				return i;
			}
		}
	}
	//should not happen: limit was set too low
	return -1;
	
}
