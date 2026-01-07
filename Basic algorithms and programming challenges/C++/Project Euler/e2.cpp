#include <iostream>
#include <vector>

int main(){
	int total = 0;
	std::vector <int> fib;
	fib.push_back(1);
	fib.push_back(1);
	for (int i=2;i<1000;i++){
		int val = fib[i-1]+fib[i-2];
		if (val>4000000){
			return total;
		}
		else{
			if (val%2==0){
				total+=val;
			}
		fib.push_back(val);
		}
		
	}
	return total;
}
