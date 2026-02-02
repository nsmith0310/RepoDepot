#include <iostream>
#include <cmath>

using namespace std;

int totient(unsigned long long num){
	unsigned long long r = num;
	unsigned long long test = num;	
	if (num%2==0){
		r-=r/2;		
		while (num%2==0){
			num/=2;
		}
	}	
	for (int i =3;i<=sqrt(num);i+=2){
		if (num%i==0){
			r-=r/i;			
			while (num%i==0){
				num/=i;
			}
		}
	}	
	if (num>2&&num!=test){
		r-=r/num;
	}	
	else if (num==test){
		return num-1;
	}
	return r;	
}

int main(){
	float max = 0;
	int num1 = 0;
	for (int i = 2;i<=1000000;i++){
		float num = (float)i/totient(i);
		if (num>max){
			max = num;
			num1 = i;
		}
	}
	cout<<num1;
	return 0;
}
