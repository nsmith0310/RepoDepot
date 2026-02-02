//is slow ~4 min and non-general (9350130049860600)

#include <iostream>
#include <cmath>
#include <vector>
#include "C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h"
using namespace std;

int main(){
	
	vector<int> primes = {2,3,5,7,11,13,17,19,23,29,31,37};
	vector<int> limits = {22,14,10,8,1,1,1,1,1,1,1,1};
	int lth = 11;
	
	vector<vector<int>> combs = {{}};
	for (int i = 0;i<=lth;i++){
		vector<vector<int>> next;
		for (int j=0;j<=limits[i];j++)
			for (int k=0;k<combs.size();k++){
				vector<int> tmp = combs[k];
				tmp.push_back(j);
				next.push_back(tmp);
				
			}
		combs = next;
	}
	ttmath::UInt<100> min = 999999999999999999999999;
	
	for (int i = 0;i<combs.size();i++){
		
		ttmath::UInt<100> total = 1;
		for (int j = 0;j<=lth;j++){
			total*=(2*combs[i][j] +1);
		}
		total = (total+1)/2;
		if (total>4000000){
			ttmath::UInt<100> num = 1;
			for (int j = 0;j<=lth;j++){
				for (int k = 1;k<=combs[i][j];k++){
					num*=primes[j];
				}
			}
			if (num<min){
				min = num;
			}
			
		}
		
		
	}
	cout<<min;
	return 0;
}
