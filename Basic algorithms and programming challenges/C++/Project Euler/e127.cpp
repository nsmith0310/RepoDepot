#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <iterator>
#include <set>
using namespace std;

//super long 6259 s, 18407904
vector<int> factor(int num){
	vector<int> factors={1};
	if (num%2==0){
		factors.push_back(2);
		while (num%2==0){
			num/=2;
		}
	}	
	
	for (int i = 3;i<=sqrt(num);i+=2){
		if (num%i==0){
			factors.push_back(i);
			while (num%i==0){
				num/=i;
			}
		}
	}
	if (num>2){
		factors.push_back(num);
	}
	return factors;
}

int main(){
	
	int limit = 120000;
	
	long long total = 0;
	
	vector<vector<int>> dp1;
	vector<int> dp2;
	
	for (int i = 0;i<limit;i++){
		vector<int> tmp = {-1};
		dp1.push_back(tmp);
		dp2.push_back(-1);
	}
	limit-=1;
	vector<int> farey = {0,1,1,limit};
	while (farey[2]<=limit){
		int k = (limit + farey[1])/farey[3];
		farey = {farey[2], farey[3], k * farey[2] - farey[0], k * farey[3] - farey[1]};
		int a = farey[0];
		int c = farey[1];
		int b = c-a;
		if (a<b&&(__gcd(a,b)==__gcd(b,c)==1)){
			if (dp2[a]==-1){
				dp2[a]=1;
				dp1[a]=factor(a);
			}
			if (dp2[b]==-1){
				dp2[b]=1;
				dp1[b]=factor(b);
			}
			if (dp2[c]==-1){
				dp2[c]=1;
				dp1[c]=factor(c);
			}
				
			set<int> unique;
				
			for (int i = 0;i<dp1[a].size();i++){
				unique.insert(dp1[a][i]);
			}
			for (int i = 0;i<dp1[b].size();i++){
				unique.insert(dp1[b][i]);
			}
			for (int i = 0;i<dp1[c].size();i++){
				unique.insert(dp1[c][i]);
			}
			long long t = 1;
			set<int>::iterator itr;	
			for (itr = unique.begin(); itr != unique.end(); itr++){
				
				t*=*itr;
			}
			if (t<c){
				total+=c;
			}
		}
	}

	cout<<total;
	return 0;
}
