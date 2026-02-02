#include <iostream>
#include <vector>
#include <map>
using namespace std;
int main(){
	vector<bool> numbers={false,false};
	int limit = 1000000;
	for (int i=0;i<limit-2;i++){numbers.push_back(true);}
	for (int i=2;i<limit;i++){
		int k = 2;
		while (i*k<limit){
			numbers[i*k]=false;
			k+=1;
		}
	}
	vector<int> primes;	
	map<int, int> c;
	int lth = 0;
	int count = 0;
	for (int i=0;i<limit;i++){
		if (numbers[i]==true){
			primes.push_back(i);
			c[i]=1;
			lth+=1;
		}
	}
	map<int, int> m;
	for (int i=1;i<=1000;i++){
		m[i*i]=1;
	}
	for (int i = 3;i<1000000000;i+=2){
		if (!c[i]){
		
			bool found = true;
			for (int j = 0;j<lth;j++){
				if (primes[j]>=i){
					break;
				}
				int val = i-primes[j];
				if (val%2==0){
					val/=2;
					if (m[val]==1){
						found = false;
					}
				}
			}
			if (found==true){
				cout<<i;
				return 0;
			}
	}
	}
	return -1;
	
}
