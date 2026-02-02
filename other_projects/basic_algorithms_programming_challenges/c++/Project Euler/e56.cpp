#include <iostream>
#include "C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h"
#include <cmath>

using namespace std;

int main(){
	
	long long max = 0;
	for (int i=1;i<100;i++){
		for (int j=1;j<100;j++){
			ttmath::Int<20*20> num = 1;
			for (int k=0;k<j;k++){
				num*=i;
			}
			long long total = 0;
			string s;
			num.ToString(s);
			for (int k=0;k<s.length();k++){
				char x = s[k]-48;
				total+=x;
			}
			if (total>max){
				max = total;
			}
		}
	}
	cout<<max;
	return 0;
	
}
