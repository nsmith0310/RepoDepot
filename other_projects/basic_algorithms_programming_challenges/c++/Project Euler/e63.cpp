#include <iostream>
#include <string>
#include <C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h>
using namespace std;
int main(){
	
	int total = 0;
	
	for (int i = 1;i<=30;i++){
		bool kill = false;
		for (int j = 1;j<1000;j++){
			ttmath::UInt<100> num = 1;
			ttmath::UInt<100> num2 = j;
			for (int k=0;k<i;k++){
				num*=num2;
			}
			string s;
			num.ToString(s);
			if (s.length()>i){
				kill=true;
				break;
			}
			else if (s.length()==i){
				total+=1;
			}
			
		}
	}
	cout<<total;
	return 0;
	
}
