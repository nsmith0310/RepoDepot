#include <iostream>
#include <cmath>
using namespace std;
int count(long long num){
	int t = 0;
	if (num%2==0){
		t+=1;
		while (num%2==0){
			num/=2;
		}
	}
	
	for (int i=3;i<=sqrt(num);i+=2){
		if (num%i==0){
			t+=1;
			while (num%i==0){
				num/=i;
			}
		}
	}
	if (num>2){
		t+=1;
	}
	return t;	
}

int main(){
	
	int n = 4;
	int c=0;
	long long num = 0;
	for (int i=2;i<=1000000;i++){
		if (count(i)==n){
			c+=1;
			if (c==n){
				cout<<num;
				return 0;
			}
			else if (c==1){
				num = i;
			}
		}
		else{
			c = 0;
		} 
	}
	return 0;
}
