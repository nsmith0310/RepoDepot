#include <iostream>
#include <vector>
using namespace std;
//uses a sieve to generate primes 
int main(){
	vector<bool> numbers={false,false};
	int limit = 100000000;
	limit/=2;
	for (int i=0;i<limit-2;i++){numbers.push_back(true);}
	for (int i=2;i<limit;i++){
		int k = 2;
		while (i*k<limit){
			numbers[i*k]=false;
			k+=1;
		}
		
		
	}
	vector<long long> primes;
	int count = 0;
	for (int i=0;i<limit;i++){
		if (numbers[i]==true){
			count+=1;
			primes.push_back(i);
		}
	}
	limit*=2;
	long long total = 0;
	
	for (int i =0;i<count;i++){
		for (int j=i;j<count;j++){
			if (primes[i]*primes[j]<limit){
				total+=1;
			}
			else{
				break;
			}
		}
	}
	cout << total;
	return 0;
	
}
