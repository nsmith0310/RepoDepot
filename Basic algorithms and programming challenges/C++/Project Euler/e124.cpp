#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

long long rad(int n){
    long long t = 1;
    if (n%2==0){
        t*=2;
        while (n%2==0){
            n/=2;
        }
    }
    for (int j = 3; j<=sqrt(n);j+=2){
        if (n%j==0){
            t*=j;
            while (n%j==0){
                n/=j;
            }
        }
    }
    if (n>2){
        t*=n;
    }
    return t;
}

int main(){
    int limit = 100000;
    int ret = 10000;
    vector<vector<long long>> nums = {};
    for (int i = 1;i<=limit;i++){
        vector<long long> tmp={rad(i),i};
        nums.push_back(tmp);
    }
    sort(nums.begin(),nums.end());
    
    cout <<nums[ret-1][1];
    return 0;
}
