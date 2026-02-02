#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main(){
	long long total = 0;
	for (int i=2;i<1000000;i++){
		string str = to_string(i);
		int lth = str.length();
		long long val = 0;
		for (int j=0;j<lth;j++){
			char x = str[j];
			val+=pow(x-48,5);
		}
		if (val==i){
			total+=i;
		}
	}
	cout<<total;
	return 0;
	
}
