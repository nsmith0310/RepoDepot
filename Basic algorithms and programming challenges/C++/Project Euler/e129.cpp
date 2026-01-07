#include "C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h"
#include <iostream>
#include <algorithm>
using namespace std;

bool check(long long n,long long k){
	ttmath::UInt<1000> rep = 1;
	for (int i = 0;i<k;i++){
		rep*=10;
	}
	rep = (rep-1)/9;
	return (rep%n==0);
	
}


int main(){
	int limit = 1000;
	for (int i = 17;i<1000000;i++){
		if (__gcd(i,10)==1){
			for (int k = 1;k<10000000;k++){
				if (check(i,k)){
					if (k>limit){
						cout<<i;
						return 0;
					}
					break;
				}
			}
		}
	}
}

