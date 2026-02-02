#include <iostream>
#include <cmath>
int count(int n){
	int t = 1;
	
	int num = 1;
	while (n%2==0){
		num+=1;
		n/=2;
	}
	t*=num;
	for (int j=3;j<=sqrt(n)+1;j+=2){
		int tmp = 0;
		while (n%j==0){
			tmp+=1;
			n/=j;
		}
		if (tmp!=0){
			tmp+=1;
			t*=tmp;
		}
	}
	if (n>2){
		t*=2;
	}
	return t;
	
}


int main(){
	
	for (int i=2;i<100000;i++){
		long long num = count((i*(i+1))/2);
		if (num>500){
			std::cout<<(i*(i+1))/2;
			return 0;
		}
		
	}
	return -1;
}
