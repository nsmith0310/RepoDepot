#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int main(){
	
	
	int limit = 12000;
	bool flag;
	long long total =0;
	vector<int> farey = {0,1,1,limit};
	while (farey[2]<=limit){
		int k = (limit + farey[1])/farey[3];
		farey = {farey[2], farey[3], k * farey[2] - farey[0], k * farey[3] - farey[1]};
		int a = farey[0];
		int c = farey[1];
		if (a==1 && c==3){
			flag=1;
		}
		else if (a==1 && c==2){
			flag =0;
		}
		if (flag==1){
			total+=1;
		}
	}
	cout<<total-1;
	return 0;
}
