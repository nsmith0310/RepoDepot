#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
int main(){
	int lim = 100000;
	vector<string> master;
	map<string,int> mp;
		
	for (int i=1;i<lim;i++){		
		string tmp = to_string(i*(i+1)/2);
		int lth = tmp.length();
		if (lth<4){
			continue;
		}
		else if (lth==4){
			master.push_back(tmp);
			mp[tmp]=0;	
		}
		else{
			break;
		}
	}
	for (int i=1;i<lim;i++){		
		string tmp = to_string(i*i);
		int lth = tmp.length();
		if (lth<4){
			continue;
		}
		else if (lth==4){
			master.push_back(tmp);
			mp[tmp]=1;	
		}
		else{
			break;
		}
	}
	for (int i=1;i<lim;i++){		
		string tmp = to_string(i*(3*i-1)/2);
		int lth = tmp.length();
		if (lth<4){
			continue;
		}
		else if (lth==4){
			master.push_back(tmp);
			mp[tmp]=2;	
		}
		else{
			break;
		}
	}
	for (int i=1;i<lim;i++){		
		string tmp = to_string(i*(2*i-1));
		int lth = tmp.length();
		if (lth<4){
			continue;
		}
		else if (lth==4){
			master.push_back(tmp);
			mp[tmp]=3;	
		}
		else{
			break;
		}
	}
	for (int i=1;i<lim;i++){		
		string tmp = to_string(i*(5*i-3)/2);
		int lth = tmp.length();
		if (lth<4){
			continue;
		}
		else if (lth==4){
			master.push_back(tmp);
			mp[tmp]=4;	
		}
		else{
			break;
		}
	}
	for (int i=1;i<lim;i++){		
		string tmp = to_string(i*(3*i-2));
		int lth = tmp.length();
		if (lth<4){
			continue;
		}
		else if (lth==4){
			master.push_back(tmp);
			mp[tmp]=5;	
		}
		else{
			break;
		}
	}
	
	
	vector<vector<string>> current;
	for (int i=0;i<master.size();i++){
		vector<string> app = {master[i]};
		current.push_back(app);
	}
	int ct = 1;
	
	
	while (ct<7){
		vector<vector<string>> tmp;
		//cout<<current.size()<<"\n";
		for (int i = 0;i<current.size();i++){
			for (int j=0;j<master.size();j++){
				for (int k=0;k<ct;k++){
					if (current[i][k]==master[j]||mp[current[i][k]]==mp[master[j]]){
						break;
					}
					else{
						char a = current[i][k][2];
						char b = master[j][0];
						char c = current[i][k][3];
						char d = master[j][1];
						if (a==b&&c==d){
							vector<string> chain = current[i];
							chain.push_back(master[j]);
							tmp.push_back(chain);
						}
						
					}
				}
			}
		}
		ct+=1;
		current = tmp;
		
	}
	
	for (int i=0;i<current.size();i++){
		char a = current[i][5][2];
		char b = current[i][0][0];
		char c = current[i][5][3];
		char d = current[i][0][1];
		if (a==b&&c==d){
			int total = 0;
			for (int j=0;j<6;j++){
				total+=stoi(current[i][j]);
			}
			cout<<total;
			return 0;
		}
	}
	
								
							
	
	return 0;
	
}
