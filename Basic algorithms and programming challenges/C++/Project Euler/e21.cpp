#include <iostream>
#include <vector>
using namespace std;
int main(){
	vector<int> nums;
	
	
	long long t = 0;
	
	for (int i = 0;i<10000;i++){
		int total = 0;
		for (int j = 1;j<=i/2;j++){
			if (i%j==0){
				total+=j;
			}
		}
		nums.push_back(total);
	}
	
	for (int i=0;i<10000;i++){
		for (int j=0;j<10000;j++){
			if (i!=j&&nums[i]==j&&nums[j]==i){
				t+=i+j;
			}
		}
	}
	cout<<t/2;
	return 0;
	
}
