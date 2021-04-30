#include "CMakeProject1.h"

//C++ Lib
#include <iostream>
#include <algorithm>
#include <set>

//C Lib
#include <math.h>
#include <string.h>
using namespace std;


#define PI acos(-1)
#define MAP_REFERENCE_X 13478345.471 // 13478345.471
#define MAP_REFERENCE_Y 3665872.257 // 3665872.257
#define NET_REFERENCE_X 13478345.471
#define NET_REFERENCE_Y 3665872.257
#define EARTH_RADIUS 6378137
#define CORRECTION_FACTOR_MERCATOR 1.001120232


typedef struct VehicleSize {
  long width;
  long length;
  long *height /* OPTIONAL */;
} VehicleSize_t;

class Solution {
public:
  bool wordPattern(string pattern, string str) {
    unordered_map<string, char> str2ch;
    unordered_map<char, string> ch2str;
    int m = str.length();
    int i = 0;
    for (auto ch : pattern) {
      if (i >= m) {
        return false;
      }
      int j = i;
      while (j < m && str[j] != ' ')
        j++;
      const string &tmp = str.substr(i, j - i); //作为引用，减少内存消耗
      if (str2ch.count(tmp) && str2ch[tmp] != ch) {
        return false;
      }
      if (ch2str.count(ch) && ch2str[ch] != tmp) {
        return false;
      }
      str2ch[tmp] = ch;
      ch2str[ch] = tmp;
      i = j + 1;
    }
    return i >= m;
  }
  char findTheDifference(string s, string t) {
      char exor = 0;
      for (char c : s + t) {
          exor ^= c;
      }
      return exor;
  }
  int firstUniqChar(string s) {
      //for (int i = 0; i < s.length(); i++) {
      //    if (s.rfind(s[i],s.length()) == s.find(s[i])) 
      //        return i;
      //}
  }

  int hammingWeight(uint32_t n) {
      int hanming = 0;
      while (n) {
          n &= (n - 1);
          hanming++;
      }
      return hanming;
  }

  bool find132pattern(vector<int>& nums) {
      int n = nums.size();
      if (n < 3) {
          return false;
      }

      // 左侧最小值
      int left_min = nums[0];
      // 右侧所有元素
      multiset<int> right_all;

      for (int k = 2; k < n; ++k) {
          right_all.insert(nums[k]);
      }

      for (int j = 1; j < n - 1; ++j) {
          if (left_min < nums[j]) {
              auto it = right_all.upper_bound(left_min);
              if (it != right_all.end() && *it < nums[j]) {
                  return true;
              }
          }
          left_min = min(left_min, nums[j]);
          right_all.erase(right_all.find(nums[j + 1]));
      }
      return false;
  }
};



int main() {
  try {
    // test solution
    Solution so;
    // string s =
    // "yekbsxznylrwamcaugrqrurvpqybkpfzwbqiysrdnrsnbftvrnszfjbkbmrctjizkjqoxqzddyfnavnhqeblfmzqgsjflghaulbadwqsyuetdelujphmlgtmkoaoijypvcajctbaumeromgejtewbwqptotrorephegyobbstvywljboeihdliknluqdpgampjyjpinxhhqexoctysfdciqjbzilnodzoihihusxluqoayenluziobxiodrfdkinkzzozmxfezfvllpdvogqqtquwcsijwachefspywdgsohqtlquhnoecccgbkrzqcprzmwvygqwddnehhi";
    // s = "cc";
    // int result = so.firstUniqChar(s);
    // vector<int> nums = { 1,3,2,4,5,6,7,8,9,10 };

    //cout << so.find132pattern(nums) << endl;
    vector<int> Lst = { 1,2,3,4 };
    for (int i : Lst) {
        printf("%d",i);
    }

    cout << endl;
  }
    catch (exception e)
    {
        cout << e.what();
    }
#ifdef _MSC_VER
  _CrtDumpMemoryLeaks();
#endif
  return 0;
}
