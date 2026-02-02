#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> m = {0,1,4,9,16,25,36,49,64,81};



long long convert(long long num){
	long long t = 0;
	
	string s = to_string(num);
	
	for (int i = 0;i<s.length();i++){
		
		t+=m[s[i]-48];
	}	
	return t;
	
} 

int main(){
	
	long long total = 0;
	
	long long limit = 10000000;
	
	vector<int> to_check;
	
	for (int i = 0;i<limit;i++){
		to_check.push_back(0);
	}
	
	for (int i=2;i<limit;i++){
		
		if (to_check[i]==0){
			to_check[i]=1;
			long long ct = 1;
			long long tmp=i;
			
			while (1==1){
				long long new_num = convert(tmp);
				if (new_num==1){
					break;
				}
				else if (new_num==89){
					total+=ct;
					
					vector<string> perm;
					string s = to_string(i);
					int lth = s.length();
					for (int k=0;k<lth;k++){
						
						perm.push_back(string(1,s[k]));
					}
					
					
					do{
						if (perm[0]!="0"){
							
							string new_s = "";
							for (int k = 0;k<perm.size();k++){
								new_s+=perm[k];
								
							}
							if (new_s.length()>0){
								
								long long new_n = stoll(new_s);
								if (new_n<limit && to_check[new_n]==0){
									to_check[new_n]=1;
									total+=1;
								}
							}
								
						}
						
					}
					while (next_permutation(perm.begin(),perm.end()));
					
					
					
					
					
					break;
				}
				else{
					tmp = new_num;
					
					if (tmp<limit&&to_check[tmp]==0){
						to_check[tmp]=1;
						ct+=1;
					}
				}
			}	
		}
		
	}
	
	cout<<total;
	return 0;
	
	
}
