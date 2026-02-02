#include <iostream>

int main()
{
	int max = 0;
	int n = 0;
	for (int i=2;i<1000000;i++)
	{
		int steps = 1;
		long long num = i;
		while (num>1)
		{
			if (num%2==0)
			{
				steps+=1;
				num/=2;
			}
			else
			{
				steps+=1;
				num = 3*num + 1;
			
			}
		}
		if (steps>max){
			max=steps;
			n = i;
		}
	}
	std::cout<<n;
	return 0;
}
