#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
using namespace std;

bool ip(unsigned long long val){
	unsigned long long check = (1 + sqrt(1+(24*val)))/6;
	//cout<<check<<"\n";
	return floor(check)==check;
}

bool ih(unsigned long long val){
	unsigned long long check = (1 + sqrt(1 + 8*val))/4;
	//cout<<check;
	return floor(check)==check;
}

int main(){
	cout<<fixed;
	for (unsigned int i = 286;i<55386;i++){
		unsigned long long val = (i*(i+1))/2;
		//cout <<val;
		if (ip(val)&&ih(val)){
			
			unsigned long long idxp = (1 + sqrt(1+(24*val)))/6;
			unsigned long long idxh = (1 + sqrt(1 + 8*val))/4;
			
			unsigned long long nump = (idxp*(3*idxp-1))/2;
			unsigned long long numh = idxh*(2*idxh -1);
			
			if (nump==numh&&numh==val){
				cout<<setprecision(0)<<val<<"\n";
				
			}
			
			
		}
	}
	
	return 1;
}
