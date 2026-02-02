#include <iostream>
#include "C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h"

using namespace std;
int main(){
	
	long long total = 0;
	ttmath::UInt<100> limit = 1000000;
	
	for (int i = 1;i<=100;i++){
		for (int j = 1;j<=i;j++){
			ttmath::UInt<100> numr = 1;
			ttmath::UInt<100> den1 = 1;
			ttmath::UInt<100> den2 = 1;
			
			for (int k = 1;k<=i;k++){
				numr*=k;
			}
			for (int k = 1;k<=i-j;k++){
				den1*=k;
			}
			for (int k = 1;k<=j;k++){
				den2*=k;
			}
			
			numr/=(den1*den2);
			if (numr>limit){
				total+=1;
			}
		}
	}
	cout<<total;
	return 0;
		
}




