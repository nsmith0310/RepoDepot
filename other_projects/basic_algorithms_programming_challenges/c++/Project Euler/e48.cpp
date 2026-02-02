#include <iostream>
#include "C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h"
#include <cmath>

using namespace std;

int main(){
	
	ttmath::Int<20*20> num = 0;
	long long mod = pow(10,10);
	for (int i=1;i<=1000;i++){
		ttmath::Int<20*20> a = i;
		a %= mod;
    	ttmath::Int<20*20> res = 1;
    	ttmath::Int<20*20> b = i;
    	while (b > 0) 
		{
    	
        	if (b % 2==1)
        	
            	res = res * a % mod;
        
        	a = a * a % mod;
        	b >>= 1;
    	}
    
		
		num = (num+res)%mod;
	}
	cout<<num;
	return 0;
}
