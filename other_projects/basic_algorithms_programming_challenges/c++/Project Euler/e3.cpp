#include <iostream>
#include <cmath>

int main()
{
	int max =0;
	
	long long n = 600851475143;

	while (n%2==0)
	{
		if (2>max)
		{
			max = 2;
		}
		n/=2;
	}
	for (int i=3;i<sqrt(n);i+=2)
	{
		while (n%i==0)
		{
			if (i>max)
			{
				max = i;
			}
		n/=i;
		}
	}
	if (n>2 && n>max)
	{
		max = n;
	}
	return max;
}
