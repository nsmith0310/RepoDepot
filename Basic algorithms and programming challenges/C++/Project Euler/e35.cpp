#include <iostream>
#include <vector>
#include <string>
#include <math.h>

//prime check
bool prime(int s){
	if (s%2==0){
		return false;
	}
	for (int j = 3;j<=sqrt(s)+1;j++){
		if (s%j==0){
			return false;
		}
	}
	return true;
}
int main()
{
	//prime sieve
	std::vector<bool> numbers={false,false};
	int limit = 1000000;
	for (int i=0;i<limit-2;i++){numbers.push_back(true);}
	for (int i=2;i<limit;i++){
		int k = 2;
		while (i*k<limit){
			numbers[i*k]=false;
			k+=1;
		}
		
	
	}
	int c = 5;
	//for each prime generated above, perform rotations and check each for primality: if all are prime, increment count
	for (int i=13;i<1000000;i++)
	{
		if(numbers[i]==true){
			std::string s = std::to_string(i);
			bool checked = false;
			int lth = s.length();
			std::string new_s = s[lth-1]+s.substr(0,lth-1);
			while (s!=new_s){
				
				if (!prime(stoi(new_s))){
					checked = true;
					break;
				}
				new_s = new_s[lth-1]+new_s.substr(0,lth-1);
			}
			if (!checked)
			{
				c+=1;
			}
			
		}
	}
	std::cout<<c;
	return 0;
}
