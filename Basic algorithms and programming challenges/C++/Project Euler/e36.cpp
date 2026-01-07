#include <iostream>
#include <string>

using namespace std;
bool bin(long long ten){
	int lth = 0;
	string s = "";
	while (ten>0){
		string tmp = to_string(ten%2);
		s = tmp + s;
		ten/=2;
		lth+=1;
	}
	
	int i = 0;
	int j = lth-1;
	while (i<=j){
		if (s[i]!=s[j]){
			return false;
		}
		i+=1;
		j-=1;
	}
	return true;
}


int main(){
	long long limit = 1000000;
	long long total = 0;
	
	for (int i = 1;i<=999;i++){
		string left = to_string(i);
		
		string right = "";
		string right1 = "";
		for (int j = 0;j<left.length();j++){
			right = left[j]+right;
		}
		right = left + right;
		for (int j = 0;j<left.length()-1;j++){
			right1 = left[j]+right1;
		}
		right1 = left + right1;
		
		if (bin(stoi(right))){
			total+=stoi(right);
		}
		if (bin(stoi(right1))){
			total+=stoi(right1);
		}
	}
	cout<<total;
	return 0;
}
