#include "CMakeProject1.h"

//C++ Lib
#include <iostream>
#include <algorithm>
#include <set>

//C Lib
#include <string.h>
using namespace std;

extern "C" {
typedef struct VehicleSize {
  long width;
  long length;
  long *height /* OPTIONAL */;
  ~VehicleSize() { delete height; }
} VehicleSize_t;
}

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
};

int main() {
    try {
        // test ptr
        unique_ptr<VehicleSize_t> vs = unique_ptr<VehicleSize_t>(new VehicleSize_t);

        VehicleSize_t* vs1 = new VehicleSize_t();
        vs->width = 100;
        vs->length = 100;
        vs->height = new long(100);
        delete vs1;

        // int* p=nullptr;
        // p = (int*)malloc(sizeof(int));
        // *p = 1;

        // if (p == NULL)cout << "p si null" << endl;
        // if (*p == 0)cout << "p is 0" << endl;
        // delete p;
        // p = NULL;

        // test solution
        Solution so;
        string s = "yekbsxznylrwamcaugrqrurvpqybkpfzwbqiysrdnrsnbftvrnszfjbkbmrctjizkjqoxqzddyfnavnhqeblfmzqgsjflghaulbadwqsyuetdelujphmlgtmkoaoijypvcajctbaumeromgejtewbwqptotrorephegyobbstvywljboeihdliknluqdpgampjyjpinxhhqexoctysfdciqjbzilnodzoihihusxluqoayenluziobxiodrfdkinkzzozmxfezfvllpdvogqqtquwcsijwachefspywdgsohqtlquhnoecccgbkrzqcprzmwvygqwddnehhi";
        s = "cc";
        int result = so.firstUniqChar(s);
        cout << result << endl;
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
