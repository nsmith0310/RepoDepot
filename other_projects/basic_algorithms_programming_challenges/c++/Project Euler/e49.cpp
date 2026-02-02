#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;


bool check(int n){
	if (n%2==0){
		return false;
	}
	for (int j = 3;j<=sqrt(n);j++){
		if (n%j==0){
			return false;
		}
	}
	return true;
}
int main(){	
	
	vector<string> n;	
	vector<vector<int>> m;
	vector<string> n1;
	
	string line;	
	ifstream myfile("C:\\Users\\nicho\\Desktop\\include\\Auxillery\\primes.txt");
  	if (myfile.is_open())  		
  		{
    	while ( getline (myfile,line) )
    		{   
    			
				if (line.length()==4){				
					n.push_back(line);					
				}
				else if (line.length()>4){
					break;
				}			
    		}    	
  	}
	myfile.close();
	
	for (int i = 0;i<10000;i++){
		vector<int> tmp1;
    	m.push_back(tmp1);
	}
	
	for (int i = 0;i<n.size();i++){
		
		vector<string> tmp;
		
		for (int j = 0;j<4;j++)
		{
			tmp.push_back(string(1,n[i][j]));
		}
		
		do
		{
			if (tmp[0]!="0")
			{
				string s = "";
				for (int j=0;j<4;j++)
				{
					s+=tmp[j];
				}
				
				
				int val2 = stoi(s);
				if (check(val2)){
					m[stoi(s)].push_back(stoi(n[i]));
					m[stoi(n[i])].push_back(stoi(s));	
				}
				
				
			}
			
		}
		while (next_permutation(tmp.begin(),tmp.end()));
		
	}
	
	
	
	for (int i = 0;i<m.size();i++){
		if (m[i].size()>=4){
			
			sort(m[i].begin(),m[i].end());
			
			vector<vector<int>> start = {{m[i][1]}};
			
			for (int j=1;j<3;j++){
				vector<vector<int>> tmp2;
				for (int k=0;k<start.size();k++){
					for (int l = 2;l<m[i].size();l++){
						vector<int> tmp4 = start[k];
						tmp4.push_back(m[i][l]);
						tmp2.push_back(tmp4);
					}
				}
				if (j==2){
					for (int k = 0;k<tmp2.size();k++){
						if (tmp2[k][1]-tmp2[k][0]==tmp2[k][2]-tmp2[k][1]&&tmp2[k][2]-tmp2[k][1]!=0){
							if (tmp2[k][0]!=1487){
								cout<<to_string(tmp2[k][0])+to_string(tmp2[k][1])+to_string(tmp2[k][2]);
								return 0;
							}
						}
					}
				}
				else{
					start = tmp2;
				}
			}
			
			
		}
	}
	
	return 0;
}
