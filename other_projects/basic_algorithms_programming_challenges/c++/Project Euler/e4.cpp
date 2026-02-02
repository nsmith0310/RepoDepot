#include <iostream>
#include <string>

bool pal(std::string str){
	int i = 0;
	int j = str.length()-1;
	
	while (i<=j)
	{
		if (str[i]!=str[j]){
			return false;
		}
		i+=1;
		j-=1;
	}
	return true;
	
}
int main(){
	
	int max = 0;
	
	for (int i=100;i<1000;i++){
		for (int j=100;j<1000;j++){
			int val = i*j;
			if (pal(std::to_string(val))){
			
				if (val>max){
					max = val;
				}
			}
			
			
		}
	}
	return max;
	
}
