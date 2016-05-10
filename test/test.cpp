#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm> // std::sort
#include <utility> // std::pair

int main()
{
  int ints1[] = {5,4,2,1,3};
  int ints2[] = {9,7,6,8,10};

  std::vector<std::pair<int, int> > myvector;

  for(int i=0; i<5; i++)
    myvector.push_back(std::make_pair(ints2[i], ints1[i]));

  for(size_t i=0; i<myvector.size(); i++)
    std::cout << myvector[i].first << ", " << myvector[i].second << "\n";
  std::cout << "\n";

  std::sort(myvector.begin(), myvector.end());

  for(size_t i=0; i<myvector.size(); i++)
    std::cout << myvector[i].first << ", " << myvector[i].second << "\n";
  std::cout << "\n";

  return 0;
}

