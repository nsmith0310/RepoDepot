#include <iostream>
#include <vector>

using namespace std;

int main(){
	vector<bool> numbers={false,false};
	vector<int> primes;
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
	int lth = 0;
	for (int i=0;i<limit;i++){
		if (numbers[i]==true){
			primes.push_back(i);
			lth+=1;
		}
	}	
	int max = 0;
	int num = 0;	
	for (int i = 0;i<lth;i++){	
		long long total =0;
		for (int j=i;j<lth;j++){			
			total+=primes[j];
			if (total>=limit){
				break;
			}
			if (numbers[total]==true){
				if (j-i+1>max){
					max = j-i+1;
					num = total;					
				}
			}
		}
	}
	cout<<num;
	return 0;
}
