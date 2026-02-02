
//faster way to find solution using Euler's pentagonal theorem; builds the partition count series using the generalized penatgonal numbers
//to add/subtract previously discovered partition counts
#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h>

using namespace std;

int main(){	
	int limit = 100000;
	vector<long long> pent;
	vector<ttmath::UInt<100>> part={1, 1, 2, 3, 5};	
	for (int i=1;i<=limit;i++){
		long long num = (i*(3*i -1))/2;
		pent.push_back(num);
		long long num1 = (-i*(-3*i -1))/2;
		pent.push_back(num1);
	}	
	int n = 5;	
	for (int i = n;i<=limit;i++){
		ttmath::UInt<100> val = 0;		
		int p = 0;
		int c = 0;		
		for (int j=0;j<=limit;j++){
			long long pt = pent[j];			
			if (pt>i){
				break;
			}
			else
			{
				if (p==0){
					val+=part[i-pt];
					c+=1;
				}
				else
				{
					val-=part[i-pt];
					c+=1;
				}
				if (c==2){
					if (p==0){
						p=1;
						c=0;
					}
					else{
						p=0;
						c=0;
					}
				}
			}
		}
		if (val%1000000==0){
			cout<<i;
			return 0;
		}
		else{
			part.push_back(val);
		}		
	}	
	return 0;
}




/*
THE FOLLOWING IS A LONG WAY TO FIND THE SOLUTION

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
	
	
	ttmath::UInt<100> div = 1000000;
	int n = 2;
	for (int i = n;i<limit;i++){
		ttmath::UInt<100> total = 0;
		for (int j = 0;j<i;j++){
			total+=nums[i-j]*a[j];
			
		}
		total/=i;
		if (total%div==0){
			cout<<i;
			return 0;
		}
		a.push_back(total);
	}
	
	return 0;
}
*/	
	
