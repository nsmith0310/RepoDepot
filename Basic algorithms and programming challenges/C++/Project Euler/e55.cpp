#include <iostream>
#include "C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h"
using namespace std;
bool pal(string s){
	int i =0;
	int j = s.length()-1;
	while (i<=j){
		if (s[i]!=s[j]){return false;}
		i+=1;
		j-=1;
	}
	return true;
}

int main(){
	
	
	int limit = 10000;
	//int limit = 349;
	int total = 0;
	
	for (int i = 1;i<=limit;i++){
		bool flag=true;
		ttmath::UInt<100> num = i;
		for (int j = 1;j<50;j++){
			string tmp;
			num.ToString(tmp);
			
			string tmp1 = "";
			for (int k = tmp.length()-1;k>=0;k--){
				tmp1+=tmp[k];
			}
			
			ttmath::UInt<100> tmp2 = tmp1;
			//cout<<num<<" "<<tmp2<<"\n";
			
			num+=tmp2;
			string tmp3;
			num.ToString(tmp3);
			
			
			if (pal(tmp3)){
				flag = false;
				break;
			}
			
		}
		if (flag){
			total+=1;
		}
	}
	
	cout<<total;
	return 0;
}


