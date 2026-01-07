#include <iostream>
#include <vector>
#include <cmath>

//uses a sieve to generate primes 
int main()
{
	
	std::vector<bool> numbers={false,false};
	int limit = 7071;
	for (int i=0;i<=limit-2;i++)
	{
		numbers.push_back(true);
	}
	for (int i=2;i<=limit;i++)
	{
		int k = 2;
		while (i*k<=limit)
		{
			numbers[i*k]=false;
			k+=1;
		}
	}
	std::vector<bool> counts;
	for (int i=0;i<=50000000;i++)
	{
		counts.push_back(false);
	}	
	
	int count = 0;
	for (int i=0;i<=7071;i++)
	{
		for (int j=0;j<=369;j++)
		{
			for (int k=0;k<=83;k++)
			{
				if (numbers[i]&&numbers[j]&&numbers[k])
				{
					long long val = pow(i,2)+pow(j,3)+pow(k,4);
					if (val<50000000)
					{
						counts[val]=true;
					}
					
				}
				
			}
		}
	}
	for (int i=0;i<=50000000;i++)
	{
		if (counts[i])
		{
			count+=1;
		}
	}
	
	std::cout<<count;
	return 0;
	
}
