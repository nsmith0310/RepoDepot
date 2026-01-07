#include <iostream>
#include "C:\Users\nicho\Desktop\include\ttmath-0.9.4.prerelease-src-2019.07.31\ttmath\ttmath.h"
#include <string>
using namespace std;
int main(){
	
	//The 'big int' is declared immediately below; the <20*20> involves the space allocated, and seems to need to be proportional to the size
	//of the number being worked with
	ttmath::Int<20*20> n=1;
	for (int i=0;i<1000;i++){
		n*=2;
	}
	string s;
	n.ToString(s);
	int total = 0;
	for (int j=0;j<s.length();j++){
		char x = s[j];
		total+=x-48;
	}
	cout<<total;
	return 0;
}
