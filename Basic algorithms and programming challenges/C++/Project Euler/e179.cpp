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
	
	total*=(counter+1);
	
	for (int i = 3;i<=sqrt(num);i+=2){
		int counter=0;
		while (num%i==0){
			counter+=1;
			num/=i;
		}
		total*=(counter+1);
	}
	
	if (num>2){
		total*=2;
	}
	return total;
	
}


int main(){
	
	long long limit = 10000000;
	
	long long total = 0;
	
	long long val = sigma(2);
	
	for (long long i=3;i<=limit;i++){
		long long tmp = sigma(i);
		if (tmp==val){
			total+=1;
		}
		val=tmp;
	}
	cout<<total;
	return 0;
	
}
