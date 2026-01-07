#include <iostream>
#include <string>
using namespace std;
int main(){
	int limit = 1000000;
	int total = 1;
	
	string s = " ";
	int lth = 0;
	for (int i=1;i<limit;i++){
		string tmp = to_string(i);
		s+=tmp;
		lth+=tmp.length();
		if (lth>=limit){
			break;
		}
	}
	
	for (int i = 1;i<=limit;i*=10){
		total*=char(s[i])-48;
	}
	
	cout<<total;
	return 0;
}
