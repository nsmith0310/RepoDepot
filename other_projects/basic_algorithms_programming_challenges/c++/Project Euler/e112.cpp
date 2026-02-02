#include <string>
#include <iostream>

using namespace std;

bool bounce(long long n){
	string s = to_string(n);
	
	bool inc = false;
	bool dec = false;
	
	int dig = char(s[0])-48;
	for (int i = 1;i<s.length();i++){
		int new_dig = char(s[i])-48;
		
		if (new_dig>dig){
			inc = true;
		}
		else if (new_dig<dig){
			dec = true;
		}
		dig = new_dig;
	}
	if (inc&&dec){
		return true;
	}
	else{
		return false;
	}
	
}

int main(){
	double total = 0;
	double bouncy = 0;
	double limit = 0.99;
	long long i = 1;
	while (true){
		if(bounce(i)){
			bouncy+=1.0;
		}
		total+=1.0;
		if (bouncy/total == limit){
			cout<<i;
			return 0;
		}
		i+=1;
	}
}
