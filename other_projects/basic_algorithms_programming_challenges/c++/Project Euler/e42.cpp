#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>
#include <map>
using namespace std;

int main () {
	map<long long,int> m;
	
	for (int i=1;i<1000;i++){
		m[((i*(i+1))/2)]=1;
	}
	
	vector<string> words;
    string line;
    ifstream myfile ("p042_words.txt");
    int lth =0;
    if (myfile.is_open())
    {
    	while ( getline (myfile,line) )
    {
    	string s = line;
    	regex regex("\\,");
    	vector<string> out(sregex_token_iterator(s.begin(), s.end(), regex, -1),sregex_token_iterator());
    	for (auto &s: out){
    		string s1 = "";
    		int tmp_lth=s.length();
    		
    		for (int j=1;j<tmp_lth-1;j++){
    			s1+=s[j];
			}
    		
    		words.push_back(s1);
    		lth+=1;
		}
    }
    myfile.close();
    }
	int total = 0;
	for (int i=0;i<lth;i++){
		int t = 0;
		for (int j=0;j<words[i].length();j++){
			char x = words[i][j];
			t+=int(x)-64;
		}
		//cout<<t<<"\n";
		if (m[t]){
			total+=1;
		}
	}
	cout<<total;
	return 0;
}
