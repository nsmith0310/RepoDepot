#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
	
	vector<long> factorial = {1};
	for (int i=1;i<10;i++){
		long total = 1;
		for (int j=2;j<=i;j++){
			total*=j;
		}
		factorial.push_back(total);
	}
	
	long long total = 0;
	
	for (int i=3;i<1000000;i++){
		string s = to_string(i);
		int lth = s.length();
		long long tmp = 0;
		for (int j=0;j<lth;j++){
			char x = s[j]-48;
			tmp+=factorial[x];
		}
		if (tmp==i){
			total+=i;
		}
	} 
	cout<<total;
	return 0;
}
