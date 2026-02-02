//easier to do on paper- just list prime factors of every number from 2 through 20
//and which every number has the highest count of a prime over all the others, multiply the final product by that prime as many times
//as it appears in that number, and do not again multiply by that prime

/*
2
3
2 2
5 (final solution *= 5^1)
2 3
7 (final solution *= 7^1)
2 2 2
3 3 (final solution *= 3^2)
2 5
11 (final solution *= 11^1)
2 2 3
13 (final solution *= 13^1)
2 7
3 5
2 2 2 2 (final solution *= 2^4)
17 (final solution *= 3^2)
3 3 2
19 (final solution *= 19^1)
2 2 5
*/

#include <iostream>
#include <vector>
#include <cmath>
int main(){
	std::vector <int> primes = {2,3,5,7,11,13,17,19};
	std::vector <int> counts = {0,0,0,0,0,0,0,0};
	int lth = 8;
	
	
	for (int i = 2;i<=20;i++){
		for (int j = 0;j<lth;j++){
			int dummy = i;
			int counter =0;
			while (dummy%primes[j]==0){
				counter+=1;
				dummy/=primes[j];
			}
			if (counter>counts[j]){
				counts[j]=counter;
			}
		}
	}	
	int product = 1;
	for (int j=0;j<lth;j++){product*=pow(primes[j],counts[j]);}
	return product; 
	}
	

