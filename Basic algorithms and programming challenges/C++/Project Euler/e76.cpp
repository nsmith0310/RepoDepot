


#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h>
using namespace std;
int main(){	
	int limit = 1000000;
	vector<ttmath::UInt<100>> nums = {0,1};	
	for (int i=2;i<=limit;i++){
		int t = 1;
		for (int j=2;j<=sqrt(i);j++){
			if (i%j==0){
				if(j==i/j){
					t+=j;
				}
				else{
					t+=j+i/j;
				}
				
			}
		}
		ttmath::UInt<100> val = t+i;
		nums.push_back(val);
	}
	vector<ttmath::UInt<100>> a= {1,1};
	
	map<int,map<int,ttmath::UInt<100>>> dp;
	
	
	
	int n = 2;
	for (int i = n;i<limit;i++){
		ttmath::UInt<100> total = 0;
		for (int j = 0;j<i;j++){
			total+=nums[i-j]*a[j];
			
		}
		total/=i;
		if (i==100){
			cout<<total-1;
			return 0;
		}
		a.push_back(total);
	}
	
	return 0;
}
	
	
