#include <iostream>

#include <vector>

#include <map>

using namespace std;

int main()

{

    vector<int> abundant;

    map<int,int> m;

    int lth =0;

    for (int i=2;i<28124;i++)

    {

       

        long long total = 0;

        for (int j = 1;j<=i/2;j++)

        {

            if (i%j==0)

            {

                total+=j;

            }

        }

        if (total>i)

        {

            abundant.push_back(i);

            m[i]=1;

            lth+=1;

            //cout<<lth<<" "<<i<<"\n";

        }

       

    }

   

    int t =0;

    for (int i=1;i<28124;i++){

       

        int kill = 0;

        for (int j=0;j<lth;j++){

            if (m.count(i-abundant[j])){

                kill=1;    

                break;

            }

        }

        if (kill==0){

            t+=i;

        }

    }

   

    cout<<t;

    return 0;

}
