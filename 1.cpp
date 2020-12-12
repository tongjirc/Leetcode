#include "CMakeProject1.h"
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
  vector<int> twoSum(vector<int> &nums, int target) {
    printf("输入数组大小为%d\n", nums.size());

    vector<int> so;
    for (int i = 0; i < nums.size(); i++) {
      for (int j = i + 1; j < nums.size(); j++) {
        if (nums[i] + nums[j] == target) {
          so.push_back(i);
          so.push_back(j);
          return so;
        }
      }
    }
    return so;
  }

  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> hashtable;
    for (int i = 0; i < nums.size(); ++i) {
      auto it = hashtable.find(target - nums[i]);
      if (it != hashtable.end()) {
        return {it->second, i};
      }
      hashtable[nums[i]] = i;
    }
    return {};
  }
};

int main() {

  // test ptr
  unique_ptr<VehicleSize_t> vs = unique_ptr<VehicleSize_t>(new VehicleSize_t);

  VehicleSize_t *vs1 = new VehicleSize_t();
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
  std::vector<int> nums({-1, -2, -3, -4, -5});
  std::vector<int> result = so.twoSum(nums, -8);
  printf("返回数据大小为%d\n", result.size());
  if (result.size())
    printf("返回数据为%d,%d\n", result[0], result[1]);

#ifdef _MSC_VER
  _CrtDumpMemoryLeaks();
#endif
  return 0;
}