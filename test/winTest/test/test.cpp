#include "test.h"

//C++ Lib
#include <iostream>
#include <algorithm>
#include <set>
#include <list>
#include <unordered_map>
#include <map>
#include <memory>
#include <iostream>
#include <vector>
#include <list>
#include <numeric>

//C Lib
#include <math.h>
#include <string.h>
#include <stdlib.h>


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
    long* height /* OPTIONAL */;
} VehicleSize_t;


typedef struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

class Solution {
public:
    bool wordPattern(std::string pattern, std::string str) {
        std::unordered_map<std::string, char> str2ch;
        std::unordered_map<char, std::string> ch2str;
        int m = str.length();
        int i = 0;
        for (auto ch : pattern) {
            if (i >= m) {
                return false;
            }
            int j = i;
            while (j < m && str[j] != ' ')
                j++;
            const std::string& tmp = str.substr(i, j - i); //作为引用，减少内存消耗
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
    char findTheDifference(std::string s, std::string t) {
        char exor = 0;
        for (char c : s + t) {
            exor ^= c;
        }
        return exor;
    }
    int firstUniqChar(std::string s) {
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

    bool find132pattern(std::vector<int>& nums) {
        int n = nums.size();
        if (n < 3) {
            return false;
        }

        // 左侧最小值
        int left_min = nums[0];
        // 右侧所有元素
        std::multiset<int> right_all;

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
            left_min = std::min(left_min, nums[j]);
            right_all.erase(right_all.find(nums[j + 1]));
        }
        return false;
    }

    int minPathSum(std::vector<std::vector<int> >& grid) {
        // write code here
        if (grid.empty() || grid[0].empty()) { return 0; }
        int m = grid.size();
        int n = grid[0].size();
        //printf("%d,%d",m,n);
        std::vector<std::vector<int>> searchLst = { {1,0},{0,1} };
        std::vector<std::vector<int>> dfsLst = { {grid[0][0],0} }; //value, position
        while (!dfsLst.empty()) {
            std::vector<int> pos=dfsLst[0];
			if (pos[1]/n == m - 1 && pos[1]%n == n - 1 ) {
                grid[pos[1] / n][pos[1] % n] = -1;
                return pos[0];
			}
            else if (grid[pos[1] / n][pos[1] % n] == -1) {
                ;
            }
			else {
                grid[pos[1] / n][pos[1] % n] = -1;
				for (int i = 0; i < searchLst.size(); i++) {
					int x1 = pos[1] / n + searchLst[i][0];
					int y1 = pos[1] % n + searchLst[i][1];
					if (x1 >= 0 && x1 < m && y1 >= 0 && y1 < n ) {
						dfsLst.push_back({ pos[0] + grid[x1][y1],x1 * n + y1 });
                        for (int i = dfsLst.size() - 2; i > 0; i--) {
                            if (dfsLst[i][0] > dfsLst[i + 1][0])swap(dfsLst[i], dfsLst[i + 1]);
                            else break;
                        }
					}
				}
			}
            dfsLst.erase(dfsLst.begin());
        }
        return -1;
    }

    bool judgeSquareSum(int c) {
        double left = 0;
        double right = sqrt(c - pow(left, 2));
        while (left <= right) {
            if (left == int(left) && right != int(right)) {
                right = floor(right);
                left = sqrt(c - pow(right, 2));
            }
            else if (right == int(right) && left != int(left)) {
                left = ceil(left);
                right = sqrt(c - pow(left, 2));
            }
            else return true;
        }
        return false;
    }

    int sumNumbers(TreeNode* root) {
        // write code here
        int sum = 0;
        if (!root)return 0;
        std::vector<TreeNode*> dfsLst = { root };
        while (!dfsLst.empty()) {
            auto node = dfsLst[0];
            if (!node->left && !node->right) {
                sum += node->val;
            }
            else {
                if (node->left) {
                    node->left->val += node->val * 10;
                    dfsLst.push_back(node->left);
                }
                if (node->right) {
                    node->right->val += node->val * 10;
                    dfsLst.push_back(node->right);
                }
            }
            dfsLst.erase(dfsLst.begin());
        }
        return sum;
    }

    int singleNumber(std::vector<int>& nums) {
        std::unordered_map<int, int> hashMap;
        for (int i : nums) {
            //if(hashMap.find(i)!=hashMap.end())
            hashMap[i] += 1;
            if (hashMap[i] == 3)hashMap.erase(i);
           // hashMap.insert({ i,1 });
        }
        return hashMap.begin()->first;
    }

    int leastBricks(std::vector<std::vector<int>>& wall) {
        if (!wall.size() || !wall[0].size())return 0;
        int m = wall.size();
        std::unordered_map<int,int> hashSet;
        for (int i = 0; i < m; i++) {
            int sLine = 0;
            hashSet[sLine] += 1;
            for (auto j : wall[i]) {
                sLine += j;
                hashSet[sLine] += 1;
            }
        }
        int maxs = 0;
        int maxk = std::accumulate(wall[0].begin(), wall[0].end(),0);
        for (auto i = hashSet.begin(); i != hashSet.end(); i++) {
            if (i->first != 0 && i->first != maxk && i->second > maxs)maxs = i->second;
        }
        
    return m - maxs;
    }
    std::string intToRoman(int num) {
        const std::pair<int, std::string> valueSymbols[] = {
    {1000, "M"},
    {900,  "CM"},
    {500,  "D"},
    {400,  "CD"},
    {100,  "C"},
    {90,   "XC"},
    {50,   "L"},
    {40,   "XL"},
    {10,   "X"},
    {9,    "IX"},
    {5,    "V"},
    {4,    "IV"},
    {1,    "I"},
        };
        std::string roman;
        for (auto [value, symbol] : valueSymbols) {
            while (num >= value) {
                num -= value;
                roman += symbol;
            }
            if (num == 0) {
                break;
            }
        }
        return roman;
    }
};

struct Test {
    int a = 10;
    int b = 20;
};

std::ostream& operator<<(std::ostream& out, const Test& t) {
    out << t.a << ' ' << t.b << std::endl;
    return out;
}


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
        std::vector<std::vector<int>> lst = { {1,2,2,1},{3,1,2},{1,3,2},{2,4},{3,1,2},{1,3,1,1} };
        std::vector<int> test = { 1,2,2,4,4,6 };
        const std::pair<int,std::string> valueSymbols[] = {
    {1000, "M"},
    {900,  "CM"},
    {500,  "D"},
    {400,  "CD"},
    {100,  "C"},
    {90,   "XC"},
    {50,   "L"},
    {40,   "XL"},
    {10,   "X"},
    {9,    "IX"},
    {5,    "V"},
    {4,    "IV"},
    {1,    "I"},
        };
        std::string roman;
        int num = 1994;
        for (auto [value, symbol] : valueSymbols) {
            while (num >= value) {
                num -= value;
                roman += symbol;
            }
            if (num == 0) {
                break;
            }
        }

        std::cout << std::endl;
    }
    catch (std::exception e)
    {
        std::cout << e.what();
    }
#ifdef _MSC_VER
    _CrtDumpMemoryLeaks();
#endif
    return 0;
}
