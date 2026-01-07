

#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
using namespace std;

bool test(float val){
	
	long double check = (1 + sqrt(1+(24*val)))/6;
	
	return int(check)==check;
	
}

int main()
{
	int limit = 2200;
	vector<long double> v;
	cout<<fixed;
	for (int i = 1;i<limit;i++){
		v.push_back((i*(3*i - 1))/2);	
	}
	
	for (int i=0;i<limit-1;i++){
		for (int j=i+1;j<limit;j++){
			if (test(v[i]+v[j])&&test(v[j]-v[i])){
				cout<<setprecision(0)<<v[j]-v[i];
				return 0;
			}
		}
	}
	return -1;
}
	
	
	
	
