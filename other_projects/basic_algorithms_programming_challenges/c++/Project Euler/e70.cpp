#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
using namespace std;

//long ~24 sec 8319823
int totient(unsigned long long num){
	unsigned long long r = num;
	unsigned long long test = num;	
	if (num%2==0){
		r-=r/2;		
		while (num%2==0){
			num/=2;
		}
	}	
	for (int i =3;i<=sqrt(num);i+=2){
		if (num%i==0){
			r-=r/i;			
			while (num%i==0){
				num/=i;
			}
		}
	}	
	if (num>2&&num!=test){
		r-=r/num;
	}	
	else if (num==test){
		return num-1;
	}
	return r;	
}

int main(){
	
	long limit = 10000000;
	
	long num = 0;
	float min = limit;
	
	for (int i=2;i<limit;i++){
		long long val = totient(i);
		float q = float(i)/float(val);
		if (q<min){
			string s1 = to_string(i);
			string s2 = to_string(val);
			
			vector<int> v1;
			vector<int> v2;
			
			for (int j =0;j<s1.length();j++){
				v1.push_back(int(s1[j]-48));
			}
			sort(v1.begin(),v1.end());
			for (int j =0;j<s2.length();j++){
				v2.push_back(int(s2[j]-48));
			}
			
			sort(v2.begin(),v2.end());
			if (v1==v2){
				//cout<<q;
				min = q;
				num = i;
			}
		}
		
			
		
	}
	
	cout<<num;
	return 0;
}
