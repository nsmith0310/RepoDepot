#include <vector>
#include <iostream>
#include <string>
#include "C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h"
using namespace std;
int main(){
	ttmath::UInt<100> total = 0;
	ttmath::UInt<100> limit = 1000000000;
	
	
	int exp = 0;
	while (limit>=1){
		exp+=1;
		limit/=10;
		
	}
	vector<ttmath::UInt<100>> mult = {0,20,100,600};
	
	int counter = 0;
	for (int i = 1;i<exp;i+=1){
		total+=mult[counter];
		
		if (counter==1 || counter==3){
			mult[counter]*=900;
		}
		else if (counter==2){
			mult[counter]*=500;
		}
		counter+=1;
		if (counter==4){
			counter=0;
		}
	}
	
	
	
	cout<<total;
	return 0;
}
