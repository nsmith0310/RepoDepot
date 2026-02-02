#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
int main(){
	
	int num_zeroes = 8;
	long long limit = pow(10,num_zeroes);
	long long lth = 0;
	vector<long long> squares;
	for (int i = 1;pow(i,2)<limit;i++){
		squares.push_back(pow(i,2));
		lth+=1;
	}
	
	long long total = 0;
	
	if (num_zeroes%2==0){
		num_zeroes/=2;
	}
	else{
		num_zeroes/=2;
		num_zeroes+=1;
	}
	string pal = "";
	for (int i = 0;i<num_zeroes;i++){
		pal+="9";
	}
	long long nines = stoi(pal);
	
	for (int i = 1;i<=nines;i++){
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
		
		
		long long num1 = stoi(right);
		long long num2 = stoi(right1);
		
		if (num1<limit){
			bool kill = false;
			for (int j=0;j<lth;j++){
				long long tmp = 0;
				long long ct = 0;
				for (int k=j;k<lth;k++){
					ct+=1;
					tmp+=squares[k];
					if (tmp==num1&&ct>1){
						total+=num1;
						kill=true;
						break;
					}
					else if (tmp>num1){
						break;
					}
				}
				if (kill==true){
					break;
				}
			}	
		}
		if (num2<limit){
			bool kill1 = false;
			for (int j=0;j<lth;j++){
				long long tmp1 = 0;
				long long ct1 = 0;
				for (int k=j;k<lth;k++){
					ct1+=1;
					tmp1+=squares[k];
					if (tmp1==num2&&ct1>1){
						total+=num2;
						kill1 = true;
						break;
					}
					else if (tmp1>num2){
						break;
					}
				}
				if (kill1==true){
					break;
				}
			}
		}
		
		
	}
	cout<<total;
	return 0;
}
