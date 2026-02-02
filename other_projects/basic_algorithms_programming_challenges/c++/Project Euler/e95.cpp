#include <iostream>
#include <cmath>
#include <vector>
#include <map>

//could be sped up by using a table to store chains: for example, all members of a chain have the same length, and can be skipped if encountered in a chain
//prior to main iteration
using namespace std;
int main(){	
	int limit = 1000000;
	vector<int> nums = {0,0};	
	for (int i=2;i<=limit;i++){
		int t = 1;
		for (int j=2;j<=sqrt(i)+1;j++){
			if (i%j==0){
				t+=j+i/j;
			}
		}
		nums.push_back(t);
	}	
	int max = 0;
	int min = 0;
	for (int i = 4;i<limit;i++)
	{			
		int mn = i;
		int lth = 0;
		int next = nums[i];
		
		if (next<=limit){
			map<int,int> m;
			m[i]=1;
			lth+=1;
			if (next<mn){
				mn=next;
			}
			while (m[next]==0){
				m[next]=1;
				if (next<mn){
					mn = next;
				}
				lth+=1;
				next = nums[next];
				if (next>limit){
					lth = 0;
					break;
				}
			}
			if (next==i){
				lth-=1;
				if (lth>max){
					max = lth;
					min = mn;
				}				
			}
		}	
	}
	cout<<min;
	return 0;
}
