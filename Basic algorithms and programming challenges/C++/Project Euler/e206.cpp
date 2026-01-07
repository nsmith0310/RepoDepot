#include <string>
#include <iostream>

using namespace std;

int main(){
	
	for (long long i = 1010101010;i<=1389026623;i+=10){
		long long num = i*i;
		string s = to_string(num);
		if(s[0]=='1'&&s[2]=='2'&&s[4]=='3'&&s[6]=='4'&&s[8]=='5'&&s[10]=='6'&&s[12]=='7'&&s[14]=='8'&&s[16]=='9'&&s[18]=='0'){
			cout<<i;
			return 0;
				
		}		
	}
}
