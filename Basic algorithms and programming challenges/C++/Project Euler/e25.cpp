#include "C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h"
#include <iostream>
#include <vector>
using namespace std;

int main(){
	vector<ttmath::Int<20*20>> fib;
	fib.push_back(1);
	fib.push_back(1);
	int i = 1;
	while (1==1){
		ttmath::Int<20*20> num = fib[i]+fib[i-1];
		string s;
		num.ToString(s);
		if (s.size()>=1000){
			cout<<i+2;
			break;
		}
		else{
			fib.push_back(num);
			i+=1;
		}
	}
	return 0;
	
}
