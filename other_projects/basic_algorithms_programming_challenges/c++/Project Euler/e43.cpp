#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main(){
	long long total =0;
	string digs[]={"0","1","2","3","4","5","6","7","8","9"};
	do{
		if (digs[0]!="0"){
			
			string s1 = "";
			for (int i = 1;i<4;i++){
				s1+=digs[i];
			}
			long long num1 = stoi(s1)%2;
			if (num1==0){
				string s2 = "";
				for (int i = 2;i<5;i++){
					s2+=digs[i];
				}
				long long num2 = stoi(s2)%3;
				if (num2==0){
					string s3 = "";
					for (int i = 3;i<6;i++){
						s3+=digs[i];
					}
					long long num3 = stoi(s3)%5;
					if (num3==0){
						string s4 = "";
						for (int i = 4;i<7;i++){
							s4+=digs[i];
						}
						long long num4 = stoi(s4)%7;
						if (num4==0){
							string s5 = "";
							for (int i = 5;i<8;i++){
								s5+=digs[i];
							}
							long long num5 = stoi(s5)%11;
							if (num5==0){
								string s6 = "";
								for (int i = 6;i<9;i++){
									s6+=digs[i];
								}
								long long num6 = stoi(s6)%13;
								if (num6==0){
									string s7 = "";
									for (int i = 7;i<10;i++){
										s7+=digs[i];
									}
									long long num7 = stoi(s7)%17;
									if (num7==0){
									string s8="";
									for (int i = 0;i<10;i++){
										s8+=digs[i];
									}
				
									long long num8 = stoll(s8);
									total+=num8;	
									}	
								}
									
							}
								
						}
							
					}
					
				}	
			}
			 	
			
			
			
			
			
			
			
			
			
		}
		
		
	}
	while (next_permutation(digs,digs+10));
	cout<<total;
	return 0;
}
