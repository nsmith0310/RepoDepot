#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main(){
	
	int limit = 1000;
	vector<int> perim;
	for (int i =0;i<=limit;i++){
		perim.push_back(0);
	}
	
	
	for (int a =0;a<limit;a++){
		for (int b=0;b<limit;b++){
			long double c = pow(a,2) + pow(b,2);
			long double c_2 = sqrt(c);
			if (int(c_2)==c_2){
				long long val = a+b+c_2;
				if (val<=limit){
					perim[val]+=1;
				}
			}
		}
	}
	
	int solution = 0;
	long long max =0;
	
	for (int i =0;i<=limit;i++){
		if (perim[i]>max){
			max = perim[i];
			solution = i;
		}
	}
	
	cout<<solution;
	return 0;
}
