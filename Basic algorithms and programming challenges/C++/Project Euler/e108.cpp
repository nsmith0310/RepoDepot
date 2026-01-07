#include <iostream>
#include <cmath>
using namespace std;
long long sigma(long long num){
	
	long long total = 1;
	
	int counter = 0;
	while (num%2==0){
		counter+=1;
		num/=2;
	}
	
	total*=(2*counter+1);
	
	for (int i = 3;i<=sqrt(num);i+=2){
		int counter=0;
		while (num%i==0){
			counter+=1;
			num/=i;
		}
		total*=(2*counter+1);
	}
	
	if (num>2){
		total*=3;
	}
	return (total+1)/2;
	
}

int main(){
	
	for (long long i =4;i<10000000;i++){
		if (sigma(i)>1000){
			cout<<i;
			return 0;
		}
	}
	return 0;
}
