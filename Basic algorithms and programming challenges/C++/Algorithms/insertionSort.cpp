#include <vector>
#include <iostream>
using namespace std;


vector<int> insertionSort(vector<int> arr){
	
	
	for (int i=1;i<arr.size();i++){
		int idx = i;
		for (int j = i-1;j>=0;j--){
			if (arr[i]<=arr[j]){
				idx = j;
			}
			else{
				break;
			}
			
		}
		int val = arr[i];
		arr.erase(arr.begin()+i);
		arr.insert(arr.begin()+idx,val);
	}
	return arr;
	
}

int main(){
	vector<int> start = {1,17,2,7,88,3,4,7,2,5,16,12,4,2,2,1,8,19};
	
	vector<int> srtd = insertionSort(start);
	
	for (int i =0;i<srtd.size();i++){
		cout<<srtd[i]<<" ";
	}
	return 0;	
	
}
