#include <vector>
#include <iostream>
using namespace std;

vector<int> merge(vector<int> A, vector<int> B){	
	vector<int> C;	
	int i = 0;
	int j = 0;	
	int a_lth = A.size();
	int b_lth = B.size();	
	while (!(i==a_lth&&j==b_lth)){
		if (i==a_lth){
			C.push_back(B[j]);
			j+=1;
		}
		else if (j==b_lth){
			C.push_back(A[i]);
			i+=1;
		}
		else{
			
			if (A[i]<=B[j]){
				C.push_back(A[i]);
				i+=1;
			}
			else{
				C.push_back(B[j]);
				j+=1;
			}
		}
	}
	return C;	
}

vector<int> mergeSort(vector<int> arr){
	int lth = arr.size();
	if (lth==1){
		return arr;
	}
	
	int q = lth/2;
	
	vector<int> half1;
	vector<int> half2;
	
	for (int i = 0;i<q;i++){
		half1.push_back(arr[i]);
	}
	for (int i = q;i<lth;i++){
		half2.push_back(arr[i]);
	}
	vector<int> h1 = mergeSort(half1);
	vector<int> h2 = mergeSort(half2);
	return merge(h1,h2);
}



int main(){
	
	vector<int> start = {1,17,2,7,88,3,4,7,2,5,16,12,4,2,2,1,8,19};
	
	vector<int> srtd = mergeSort(start);
	
	for (int i =0;i<srtd.size();i++){
		cout<<srtd[i]<<" ";
	}
	return 0;
}
