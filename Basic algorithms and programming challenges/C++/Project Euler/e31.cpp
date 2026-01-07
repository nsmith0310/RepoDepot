#include <vector>
#include <iostream>

using namespace std;

vector<long long> coins = {1,2,5,10,20,50,100,200};

vector<vector<long long>> init_dp()
{
	vector<vector<long long>> dp;
	
	for (int i=0;i<=200;i++)
	{
		vector<long long> tmp;
		for (int j=0;j<8;j++)
		{
			tmp.push_back(-1);
		}
		
		dp.push_back(tmp);
	}
	
	return dp;
}

vector<vector<long long>> dp = init_dp();


long long r(long long val,int idx)
{
	if (val>200){return 0;}
	if (dp[val][idx]!=-1)
	{
		return dp[val][idx];
	}
	if (val==200)
	{
		return 1;
	}
	else if (val<200)
	{	
		long long t = 0;
		for (int i=idx;i<8;i++)
		{
			t+=r(val+coins[i],i);
		}
		dp[val][idx]=t;
		return t;
	}
}

int main(){
	cout<<r(0,0);
	return 0;
}
