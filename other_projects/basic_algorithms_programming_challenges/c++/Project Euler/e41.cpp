#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
bool is_prime(long long n){
	if (n%2==0){return false;}
	for (int i=3;i<=sqrt(n);i+=2){
		if (n%i==0){return false;}
	}
	return true;
}

int main(){
	for (int i= 9;i>=1;i--){
		long long max = 0;
		vector<string> perms;
		for (int j = 1;j<=i;j++){
			perms.push_back(to_string(j));
		}
		
		do{
			string s = "";
			for (int k = 0;k<i;k++){
				s+=perms[k];
			}
			long long val = stoll(s);
			if (is_prime(val)){
				if (val>max){
					max = val;
				}
			}
		}
		while (next_permutation(perms.begin(),perms.end()));
		if (max){
			cout<<max;
			return 0;
		}
	}
	
}
