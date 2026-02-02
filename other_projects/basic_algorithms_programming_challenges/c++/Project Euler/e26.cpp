#include <iostream>
#include "C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h"
#include <vector>
using namespace std;

int main(){
	
	vector<ttmath::UInt<1000>> tens = {1};
	int lth = 1;
	for (int i = 1;i<=989;i++){
		ttmath::UInt<100> num = 1;
		for (int j = 0;j<i;j++){
			num*=10;
		}
		tens.push_back(num);
		lth+=1;
	}
	
	int max = 6;
	int num = 7;
	for (int i = 11;i<1000;i+=2){
		for (int j = 1;j<lth;j++){
			if (tens[j]%i==1){
				if (j>max){
					max = j;
					num = i;
				}
				break;
			}
		}
	}
	cout<<num;
	return 0;
}
