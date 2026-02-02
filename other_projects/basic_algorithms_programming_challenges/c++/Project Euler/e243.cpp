#include <iostream>
#include <vector>
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
long long seive(long long n){
	vector<bool> numbers={false,false};
	int limit = n;
	for (int i=0;i<limit-2;i++){numbers.push_back(true);}
	for (int i=2;i<limit;i++){
		int k = 2;
		while (i*k<limit){
			numbers[i*k]=false;
			k+=1;
		}
		
		
	}
	long long total = 1;
	
	for (int i=0;i<limit;i++){
		if (numbers[i]==true){
			total*=i;
			}
		}
	return total;	
	}
		
//seems to be needed for avoiding precision errors
bool comp(long long num1,long long den1,long long num2,long long den2){
	return num1*den2<num2*den1;
}

int main(){
	long long num = 0;
	
	
	long long num1 = 15499;
	long long den1 = 94744;
	
	
	for (int i = 10;i<1000000000;i++){
		long long t = totient(seive(i));
				
		if (comp(t,seive(i)-1,num1,den1)){
			long long num = seive(i-1);
			
			long long m = 1;
			while (1==1){
				long long tmp = num*m;
				long long tmp1 = totient(tmp);
				
				if (comp(tmp1,tmp-1,num1,den1)){
					cout<<num*m;
					return 0;
				}
				m+=1;
			}
		}
	}
}
