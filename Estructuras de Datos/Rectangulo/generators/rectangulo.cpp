#include <stdio.h>

#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

int main() {
  freopen("10.in", "w", stdout);
  srand(time(NULL));
  int x = rand() % 1000000;
  x++;
  cout << x << endl;
  for (int i = 0; i != x; i++) {
    cout << rand() % 1000000 << " ";
  }
}
