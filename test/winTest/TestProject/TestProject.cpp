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
#include <string>
#include <queue>

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

class Product
{
public:
	virtual int operation(int a, int b) = 0;
};

class Add :public Product {
public:
	int operation(int a, int b) {
		return a + b;
	}
};

class Mul :public Product {
public:
	int operation(int a, int b) {
		return a * b;
	}
};

class Abs :public  Product {
public:
	int operation(int a, int b) {
		return a - b;
	}
};

class Factory
{
public:
	virtual Product* Create() = 0;
};

class Factory_Add :public Factory {
public:
	Product* Create() {
		return new Add();
	}
};

class Factory_Mul : public Factory {
public:
	Product* Create() {
		return new Mul();
	}
};

class Factory_Abs : public Factory {
public:
	Product* Create() {
		return new Abs();
	}
};


class Solution {
	static int a;
public:
	void Test();
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
			std::vector<int> pos = dfsLst[0];
			if (pos[1] / n == m - 1 && pos[1] % n == n - 1) {
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
					if (x1 >= 0 && x1 < m && y1 >= 0 && y1 < n) {
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
		std::unordered_map<int, int> hashSet;
		for (int i = 0; i < m; i++) {
			int sLine = 0;
			hashSet[sLine] += 1;
			for (auto j : wall[i]) {
				sLine += j;
				hashSet[sLine] += 1;
			}
		}
		int maxs = 0;
		int maxk = std::accumulate(wall[0].begin(), wall[0].end(), 0);
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

	int entryTime(std::string s, std::string keypad) {
		int sum = 0;
		for (int i = 1; i < s.length(); ++i) {
			auto current = keypad.find(s[i - 1]);
			auto target = keypad.find(s[i]);
			int x1 = current % 3, y1 = current / 3;
			int x2 = target % 3, y2 = target / 3;
			if (x1 == x2 && y1 == y2)sum += 0;
			else if (abs(x1 - x2) <= 1 && abs(y1 - y2) <= 1)sum += 1;
			else sum += 2;
		}
		return sum;
	}
	int MaximumArriveAtSameTime(std::vector<double>& speed, std::vector<double>& location, double destination) {
		int maxPlaton = 1;
		for (int i = location.size() - 1; i >= 1; --i) {
			for (int j = 0; j < i; ++j) {
				if (location[j] < location[j + 1]) {
					std::swap(location[j], location[j + 1]);
					std::swap(speed[j], speed[j + 1]);
				}
			}
		}
		int size = location.size();
		while (size) {

			//for (int i = 0; i <= size - 1; ++i) {
			//    std::cout << location[i];
			//}

			for (int i = 0; i <= size - 1; ++i) {
				location[i] = location[i] + speed[i];
			}
			int j = 0;
			while (j <= size - 1) {
				if (location[j] >= destination) {
					std::swap(location[j], location[size - 1]);
					std::swap(speed[j], speed[size - 1]);
					size -= 1;
				}
				else j += 1;
			}
			for (int i = 1; i <= size - 1; ++i) {
				if (location[i] >= location[i - 1]) {
					location[i] = location[i - 1];
					speed[i] = speed[i - 1];
				}
			}
			std::unordered_map<double, int> Count;
			for (int i = 0; i <= size - 1; ++i) {
				Count[location[i]] += 1;
				if (Count[location[i]] > maxPlaton)maxPlaton = Count[location[i]];
			}
			std::cout << std::endl;
		}
		return maxPlaton;
	}

	int arrangeCoins(int n) {
		int left = 0, right = n;
		while (left < right) {
			int mid = left + (right - left) / 2;
			int num_mid = (1 + mid) * mid / 2;
			if (num_mid == n) {
				return mid;
			}
			else if (num_mid > n) {
				if ((mid - 1) * mid / 2 < n) {
					return mid - 1;
				}
				right = mid - 1;
			}
			else {
				if ((mid + 2) * (mid + 1) / 2 > n) {
					return mid - 1;
				}
				left = mid + 1;
			}
			return right;
		}
	}

	std::vector<int> majorityElement(std::vector<int>& nums) {
		//O(n),O(n)
		//int min_length = nums.size() / 3;
		//std::vector<int> rtLst;
		//std::unordered_map<int, int> count;
		//for (auto & v:nums) {
		//	count[v]++;
		//}
		//for (auto& v : count) {
		//	if (v.second > min_length)rtLst.emplace_back(v.first);
		//}
		//return rtLst;

		//O(n),O(1) 摩尔投票法
		int min_length = nums.size() / 3;
		int vote1 = 0, vote2 = 0;
		int num1 = 0, num2 = 1;

		for (auto& num : nums) {
			if (vote1 >= 0 && num == num1) {
				vote1++;
			}
			else if (vote2 >= 0 && num == num2) {
				vote2++;
			}
			else if (vote1 == 0) {
				num1 = num;
				vote1++;
			}
			else if (vote2 == 0) {
				num2 = num;
				vote2++;
			}
			else {
				vote1--;
				vote2--;
			}
		}

		int count1 = 0, count2 = 0;
		for (auto& num : nums) {
			if (num == num1) { count1++; }
			else if (num == num2) { count2++; }
		}
		std::vector<int> ans;
		if (count1 > min_length)ans.emplace_back(num1);
		if (count2 > min_length)ans.emplace_back(num2);
		return ans;

	}

	int maxPower(std::string s) {
		long max_power = 1;
		long now_power = 1;
		char pre='1';
		for (char chr:s) {
			if (chr == pre) {
				++now_power;
			}
			else {
				max_power = std::max(max_power, now_power);
				now_power = 1;
			}
			pre = chr;
		}
		return std::max(now_power, max_power);
	}

	std::vector<std::string> findRelativeRanks(std::vector<int>& score) {
		int n = score.size();
		std::string price[3] = { "Gold Medal", "Silver Medal", "Bronze Medal" };
		std::vector<std::pair<int, int>> arr;
		for (int i = 0; i < n; ++i) {
			arr.emplace_back(std::make_pair(-score[i], i));
		}

		std::sort(arr.begin(), arr.end());
		std::vector<std::string> ans(n);
		for (int i = 0; i < n; ++i) {
			if (i >= 3) {
				ans[arr[i].second] = std::to_string(i + 1);
			}
			else {
				ans[arr[i].second] = price[i];
			}
		}
		return ans;
	}
	bool canConstruct(std::string ransomNote, std::string magazine) {
		std::unordered_map<char, long long> dct_magazine;
		for (auto i = magazine.begin(); i != magazine.end(); ++i) {
			dct_magazine[*i] += 1;
		}

		for (auto i = ransomNote.begin(); i != ransomNote.end(); ++i) {
			if (dct_magazine[*i] == 0){
				return false;
			}
			else {
				dct_magazine[*i] -= 1;
			}
		}
		return true;
	}
	int superPow(int a, std::vector<int>& b) {
		const int MOD = 1337;
		const long length = b.size();
		int ans = 1;
		for (auto k = b.begin(); k != b.end(); ++k) {
			printf("%d iteration is %f and %d \n", *k, std::pow(ans, 10), (int)std::pow(ans, 10) % MOD);
			ans = (((long)(std::pow(ans, 10)) % MOD) * ((long)(std::pow(a, *k)) % MOD)) % MOD;
		}
		return abs(ans);
	}
	std::vector<std::vector<int>> colorBorder(std::vector<std::vector<int>>& grid, int row, int col, int color) {
		int m = grid.size(), n = grid[0].size();
		std::vector<std::pair<int, int>> lst_edge_node;
		std::vector<std::pair<int, int>> lst_searched_node;
		std::vector<std::pair<int, int>> lst_dfs;
		int main_color = grid[row][col];
		int searched_color = -1;

		std::vector<std::pair<int, int>> lst_direction{ {1,0} ,{-1,0},{0,1},{0,-1} };

		while (lst_dfs.size()) {
			std::pair<int, int>& pair = lst_dfs[lst_dfs.size() - 1];
			lst_dfs.pop_back();
			bool is_edge = false;
			for (auto itr = lst_direction.begin(); itr != lst_direction.end(); ++itr) {
				std::pair<int, int> pair1{ pair.first + itr->second,pair.second + itr->second };

				if ((0 <= pair1.first && pair1.first < m) && (0 <= pair1.second && pair1.second < n) && grid[pair1.first][pair1.second] == main_color) {
					lst_dfs.emplace_back({ pair1.first,pair1.second });
				}
				else if ((0 <= pair1.first && pair1.first < m) && (0 <= pair1.second && pair1.second < n) && grid[pair1.first][pair1.second] == searched_color) {
				continue;
				}
				else 
				{
					is_edge = true;
				}
			}
			if (is_edge) {
				lst_edge_node.append([x, y])
			}
			else {
				lst_searched_node.append([x, y])
					grid[x][y] = searched_color
			}

		}

		while lst_edge_node :
			x, y = lst_edge_node.pop()
				grid[x][y] = color

				while lst_searched_node :
			x, y = lst_searched_node.pop()
				grid[x][y] = main_color

				return grid

	}
};

int Solution::a = 0;

void Solution::Test() {
	int a = 2;
	std::vector<int> b{ 4, 3, 3, 8, 5, 2 };
	printf("MOD is %d",this->superPow(a,b));
};

class Node {
public:
	int value;
	Node* next;
	Node() {}

	Node* reverse(Node* node) {
		if (node == NULL || node->next == NULL) {
			return node;
		}
		Node* newHead = reverse(node->next);
		node->next->next = node;
		node->next = NULL;
		return newHead;
	}
};



int main() {
	try {
		std::pair<char, int> rNum{ 'R',0 };
		std::pair<char, int> lNum{ 'L',0 };
		rNum.second++;

		// test solution
		Solution so;
		so.Test();


		std::vector<double>  speed({ 4.0,2.0,1.0,1.0 });
		std::vector<double>  location({ 3.0,5.0,2.0,1.0 });
		double destination = 10.0;

		std::cout << so.MaximumArriveAtSameTime(speed, location, destination) << std::endl;

		// string s =
		// "yekbsxznylrwamcaugrqrurvpqybkpfzwbqiysrdnrsnbftvrnszfjbkbmrctjizkjqoxqzddyfnavnhqeblfmzqgsjflghaulbadwqsyuetdelujphmlgtmkoaoijypvcajctbaumeromgejtewbwqptotrorephegyobbstvywljboeihdliknluqdpgampjyjpinxhhqexoctysfdciqjbzilnodzoihihusxluqoayenluziobxiodrfdkinkzzozmxfezfvllpdvogqqtquwcsijwachefspywdgsohqtlquhnoecccgbkrzqcprzmwvygqwddnehhi";
		// s = "cc";
		// int result = so.firstUniqChar(s);
		// vector<int> nums = { 1,3,2,4,5,6,7,8,9,10 };

		//cout << so.find132pattern(nums) << endl;
		std::vector<std::vector<int>> lst = { {1,2,2,1},{3,1,2},{1,3,2},{2,4},{3,1,2},{1,3,1,1} };
		std::vector<int> test = { 1,2,2,4,4,6 };
		uint8_t a = 255;
		int8_t b(a);
		std::cout << b;
		std::system("pause");

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
