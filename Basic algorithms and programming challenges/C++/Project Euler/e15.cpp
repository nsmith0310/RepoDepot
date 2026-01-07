#include <iostream>

#include <vector>

int limit = 20;

 

std::vector<std::vector<long long>> build(int lim)

{

   

 

    std::vector<std::vector<long long>> dp;

 

    int i=0;

    while (i<=limit)

    {

        std::vector<long long> tmp;

        int j = 0;

        while (j<=limit)

   

        {

            tmp.push_back(-1);

            j+=1;

        }

        dp.push_back(tmp);

        i+=1;

    }

    return dp;

}

std::vector<std::vector<long long>> dp = build(limit);

long long r(int x, int y)

{

    if (dp[x][y]!=-1){return dp[x][y];}

   

    if (x==limit&&y==limit)

    {

        return 1;

    }

    else

    {

        long long t =  0;

        if (x<limit&&y<limit)

        {

            t+=r(x+1,y)+r(x,y+1);

        }

        else if (x<limit&&y==limit)

        {

            t+=r(x+1,y);

        }

        else if (y<limit&&x==limit)

        {

            t+=r(x,y+1);

        }

        dp[x][y]=t;

        return t;

    }

}

 

int main()

{

    std::cout<<r(0,0);

 

    return 0;

}
