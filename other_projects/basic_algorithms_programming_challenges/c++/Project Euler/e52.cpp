
#include "C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h"
#include <iostream>     // std::cout
#include <algorithm>    // std::next_permutation, std::sort
#include <string>
#include <vector>
using namespace std;
int main(){
	for (int i=1;i<100000000;i++){
		vector<int> num;
		string s_num = to_string(i);
		for (int j=0;j<s_num.length();j++){
			char x = s_num[j]-48;
			num.push_back(x);
		}
		sort (num.begin(),num.end());
		
		bool found = true;
		for (int j = 2;j<=6;j++){
			int multiple = i*j;
			vector<int> num_1;
			string s_num_1 = to_string(multiple);
			for (int k=0;k<s_num_1.length();k++){
				char x = s_num_1[k]-48;
				num_1.push_back(x);
			}
			sort (num_1.begin(),num_1.end());
			if (num_1!=num){
				found=false;
				break;
			}
			
		}
		if (found==true){
			cout<<i;
			return 0;
		}
	}
	//uh oh
}
