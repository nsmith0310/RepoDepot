#include <vector>
#include <iostream>
#include <string>
#include <map>
using namespace std;

//long 402 ~1 minute
int main(){
	int limit = 1000000;
	int total = 0;
	vector<long long> fact = {1,1};
	
	int idx = 1;
	for (int j=2;j<10;j++){
		long long num = fact[idx]*j;
		fact.push_back(num);
		idx+=1;
	}
	
	for (int i=2;i<limit;i++){
		int count = 1;
		map<long long,int> m;
		m[i]=1;
		int prev = i;
		while (1==1){
			long long t = 0;
			string s = to_string(prev);
			int lth = s.length();
			for (int k=0;k<lth;k++){
				char x = s[k]-48;
				t+=fact[x];
			}
			if (m[t]==1){
				break;
			}
			else{
				count+=1;
				if (count==60){
					total+=1;
					break;
				}
				prev = t;
				m[prev]=1;
			}
		}
		
	}
	
	
	cout<<total;
	return 0;
	
}
