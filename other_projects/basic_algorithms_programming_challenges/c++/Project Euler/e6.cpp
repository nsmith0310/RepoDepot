#include <iostream>

int main(){
	int sq = 0;
	int sm = 0;
	for (int i=1;i<=100;i++){
		sq+=i*i;
		sm+=i;
	}
	sm*=sm;
	
	return sm-sq;
	
}
