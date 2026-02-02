// next_permutation example

#include <iostream>     // std::cout

#include <algorithm>    // std::next_permutation, std::sort

#include <string>

int main () {

  int myints[] = {0,1,2,3,4,5,6,7,8,9};

 

  std::sort (myints,myints+10);

 

  int i = 1;

  do {

    i+=1;

  } while ( std::next_permutation(myints,myints+10) &&i<1000000);

 

  std::string s="";

  for (int j=0;j<10;j++){

    s+=std::to_string(myints[j]);

  }

  std::cout<<s;

  return 0;

}
