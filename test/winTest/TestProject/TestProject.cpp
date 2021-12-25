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

class NewSort {
public:
	//重载 () 运算符
	bool operator ()(const std::string& a, const std::string& b) {
		//按照字符串的长度，做升序排序(即存储的字符串从短到长)
		return  (a.length() < b.length());
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
		char pre = '1';
		for (char chr : s) {
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
			if (dct_magazine[*i] == 0) {
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
		std::vector<std::pair<int, int>> lst_dfs = { {row,col} };
		int main_color = grid[row][col];
		int searched_color = -1;

		std::vector<std::pair<int, int>> lst_direction{ {1,0} ,{-1,0},{0,1},{0,-1} };

		while (lst_dfs.size()) {
			std::pair<int, int> pair = lst_dfs[lst_dfs.size() - 1];
			lst_dfs.pop_back();
			bool is_edge = false;
			for (auto itr = lst_direction.begin(); itr != lst_direction.end(); ++itr) {
				std::pair<int, int> pair1{ pair.first + itr->first,pair.second + itr->second };

				if ((0 <= pair1.first && pair1.first < m) && (0 <= pair1.second && pair1.second < n) && grid[pair1.first][pair1.second] == main_color) {
					lst_dfs.emplace_back(std::make_pair(pair1.first, pair1.second));
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
				lst_edge_node.emplace_back(std::make_pair(pair.first, pair.second));
			}
			else {
				lst_searched_node.emplace_back(std::make_pair(pair.first, pair.second));
			}
			grid[pair.first][pair.second] = searched_color;

		}
		while (lst_edge_node.size()) {
			auto pair = lst_edge_node[lst_edge_node.size() - 1];
			lst_edge_node.pop_back();
			grid[pair.first][pair.second] = color;

		}
		while (lst_searched_node.size()) {
			auto pair = lst_searched_node[lst_searched_node.size() - 1];
			lst_searched_node.pop_back();
			grid[pair.first][pair.second] = main_color;

		}
		return(grid);
	}

	std::vector<int> maxSumOfThreeSubarrays(std::vector<int>& nums, int k) {

		std::vector<std::pair<int, std::vector<int>>> f3{};
		std::vector<std::pair<int, std::vector<int>>> f2{};
		std::vector<std::pair<int, std::vector<int>>> f1{};

		for (int i = -k - 1; i != 0; ++i) {
			f3.emplace_back(std::make_pair(INT_MIN, std::vector<int>{ i,i,i }));
			f2.emplace_back(std::make_pair(INT_MIN, std::vector<int>{ i,i }));
			f1.emplace_back(std::make_pair(INT_MIN, std::vector<int>{ i }));
		}

		for (int i = 0; i != nums.size() - k + 1; ++i) {
			f1.erase(f1.begin());
			f2.erase(f2.begin());
			f3.erase(f3.begin());
			// f1
			auto tmp = std::accumulate(nums.begin() + i, nums.begin() + i + k, 0);
			if (tmp > f1[f1.size() - 1].first) {
				f1.emplace_back(std::make_pair(tmp, std::vector<int>{i}));
			}
			else {
				f1.emplace_back(f1[f1.size() - 1]);
			}
			// f2
			if (tmp+f1[0].first > f2[f2.size() - 1].first) {
				std::vector<int> vtr_tmp = f1[0].second;
				vtr_tmp.emplace_back(i);
				
				f2.emplace_back(std::make_pair(tmp + f1[0].first, vtr_tmp));
			}
			else {
				f2.emplace_back(f2[f2.size()-1]);
			}
			// f2
			if (tmp + f2[0].first > f3[f3.size() - 1].first) {
				std::vector<int> vtr_tmp = f2[0].second;
				vtr_tmp.emplace_back(i);

				f3.emplace_back(std::make_pair(tmp + f2[0].first, vtr_tmp));
			}
			else {
				f3.emplace_back(f3[f3.size() - 1]);
			}
		}

		return f3[f3.size() - 1].second;
	}
	bool validTicTacToe(std::vector<std::string>& board) {
		int num_X = 0, num_O = 0;
		std::unordered_map<char, int> counter;
		for (int i = 0; i != 3; ++i) {
			for (int j = 0; j != 3; ++j) {
				counter[board[i][j]]++;
			}
		}

		bool win_O = (board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O') || (board[0][2] == 'O' && board[1][1] == 'O' && board[2][0] == 'O')
			|| (board[0][0] == 'O' && board[0][1] == 'O' && board[0][2] == 'O') || (board[1][0] == 'O' && board[1][1] == 'O' && board[1][2] == 'O') || (board[2][0] == 'O' && board[2][1] == 'O' && board[2][2] == 'O')
			|| (board[0][0] == 'O' && board[1][0] == 'O' && board[2][0] == 'O') || (board[0][1] == 'O' && board[1][1] == 'O' && board[2][1] == 'O') || (board[0][2] == 'O' && board[1][2] == 'O' && board[2][2] == 'O');

		bool win_X = (board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X') || (board[0][2] == 'X' && board[1][1] == 'X' && board[2][0] == 'X')
			|| (board[0][0] == 'X' && board[0][1] == 'X' && board[0][2] == 'X') || (board[1][0] == 'X' && board[1][1] == 'X' && board[1][2] == 'X') || (board[2][0] == 'X' && board[2][1] == 'X' && board[2][2] == 'X')
			|| (board[0][0] == 'X' && board[1][0] == 'X' && board[2][0] == 'X') || (board[0][1] == 'X' && board[1][1] == 'X' && board[2][1] == 'X') || (board[0][2] == 'X' && board[1][2] == 'X' && board[2][2] == 'X');

		if (!(counter['O'] == counter['X'] || counter['O'] + 1 == counter['X']) || (
			counter['O'] == counter['X'] && win_X) || (win_O and win_X) || (
				counter['O'] + 1 == counter['X'] and win_O)) {
			return false;
		}
		else {
			return true;
		}
	}
	std::string shortestCompletingWord(std::string licensePlate, std::vector<std::string>& words) {
		std::stable_sort(words.begin(), words.end(), NewSort());
		std::unordered_map<char, int> counter_plate;
		for (auto itr = licensePlate.begin(); itr != licensePlate.end(); ++itr) {
			if (*itr >= 'a' && *itr <= 'z') {
				counter_plate[*itr]++;
			}
			else if (*itr >= 'A' && *itr <= 'Z') {
				counter_plate[*itr-'A'+'a']++;
			}
		}
		for (auto& word : words) {
			std::unordered_map<char, int> counter_tmp(counter_plate);
			for (auto itr = word.begin(); itr != word.end(); ++itr) {

				if (counter_tmp.find(*itr)!= counter_tmp.end()) {
					if (--counter_tmp[*itr] == 0) {
						counter_tmp.erase(*itr);
						if (counter_tmp.size() == 0) {
							return word;
						}
					}
				}
			}
		}
		return words[words.size() - 1];

	}
	std::string toLowerCase(std::string s) {
		for (auto& chr : s) {
			chr = std::tolower(chr);
		}
		
		for (auto& chr:s) {
			if (chr >= 'A' && chr <= 'Z') {
				chr = chr + 'a' - 'A';
			}
		}

		for (auto itr = s.begin(); itr != s.end();++itr) {
			if (*itr >= 'A' && *itr <= 'Z') {
				*itr = *itr + 'a' - 'A';
			}
		}
		return(s);
	}
	int maxIncreaseKeepingSkyline(std::vector<std::vector<int>>& grid) {
		int l1 = grid.size(), l2 = grid[0].size();
		std::vector<int> max_x(l1, 0);
		std::vector<int> max_y(l2, 0);
		int rt_sum = 0;
		for (auto x = 0; x != l1; ++x) {
			for (auto y = 0; y != l2; ++y) {
				max_y[y] = std::max(grid[x][y], max_y[y]);
				max_x[x] = std::max(grid[x][y], max_x[x]);
			}
		}
		for (auto x = 0; x != l1; ++x) {
			for (auto y = 0; y != l2; ++y) {
				rt_sum+= std::min(max_x[x], max_y[y])- grid[x][y];
			}
		}
		return rt_sum;
	}

	int scheduleCourse(std::vector<std::vector<int>>& courses) {
		sort(courses.begin(), courses.end(), [](const auto& c0, const auto& c1) {return c0[1] < c1[1]; });
		std::priority_queue<int> q;
		int total = 0;
		for (const auto& course : courses) {
			int ti = course[0], di = course[1];
			if (total + ti <= di) {
				total += ti;
				q.push(ti);
			}
			else if (!q.empty() && q.top() > ti) {
				total -= q.top() - ti;
				q.pop();
				q.push(ti);
			}
		}
		return q.size();
	}
	std::vector<int> loudAndRich(std::vector<std::vector<int>>& richer, std::vector<int>& quiet) {
		int n = quiet.size();
		std::vector<std::vector<int>> g;
		std::vector<int> inDeg(n,0);
		std::vector<int> ans;
		for (int i = 0; i < n; ++i) {
			g.push_back({});
			ans.push_back(i);
		}
		for (const auto& r : richer) {

			g[r[0]].emplace_back(r[1]);
			inDeg[r[1]] += 1;
		}
		std::deque<int> q;
		for (int i = 0; i < n; ++i) {
			if (inDeg[i] == 0) {
				q.emplace_back(i);
			}
		}
		while (!q.empty()) {
			int x = q.front();
			q.pop_front();
			for (auto& y : g[x]) {
				if (quiet[ans[x]] < quiet[ans[y]]) {
					ans[y] = ans[x];
				}
				inDeg[y] -= 1;
				if (inDeg[y] == 0) {
					q.emplace_back(y);
				}
			}
		}
		return ans;
	}
	int visiblePoints(std::vector<std::vector<int>>& points, int angle, std::vector<int>& location) {
		std::vector<double>lst_angle;
		int x1 = location[0], y1 = location[1];
		int equal_point = 0;
		double PI = acos(-1);
		for (const auto& point : points) {
			if (x1 == point[0] && y1 == point[1]) {
				++equal_point;
			}
			else {
				lst_angle.emplace_back(atan2(point[1] - y1, point[0] - x1) * 180 / PI + 180);
			}
		}
		std::sort(lst_angle.begin(), lst_angle.end());
		int length = lst_angle.size();
		int max_window = 0, window_length = 0;
		int left = 0, right = 0;
		while (length) {
			
			while (std::fmod((lst_angle[right] - lst_angle[left] + 360), 360) <= angle) {
				++window_length;
				++right;
				right %= length;
				if (right == left) {
					break;
				}
			}
			max_window = std::max(max_window, window_length);
			++left;
			left %= length;
			--window_length;
			if (left == 0) {
				break;
			}
		}
		return max_window + equal_point;
	}
	int countBattleships(std::vector<std::vector<char>>& board) {
		int ans = 0;
		int m = board.size(), n = board[0].size();
		for (int x = 0; x < m; ++x) {
			for (int y = 0; y < n; ++y) {
				if (board[x][y] == 'X') {
					if (x > 0 && board[x - 1][y] == 'X') {
						continue;
					}
					else if(y > 0 && board[x][y - 1] == 'X') {
						continue;
					}
					ans++;
				}
			}
		}
		return ans;
	}
	int findJudge(int n, std::vector<std::vector<int>>& trust) {
		if (n == 1) {
			return n;
		}
		std::vector<int> dct_counter_giver(n, 0);
		std::vector<int> dct_counter_receiver(n, 0);
		std::vector<int> lst_candidate;
		for (const auto& vec : trust) {
			dct_counter_giver[vec[0]-1]++;
			dct_counter_receiver[vec[1]-1]++;
			if(dct_counter_receiver[vec[1] - 1] == n - 1 && dct_counter_giver[vec[1] - 1] == 0){
				lst_candidate.emplace_back(vec[1] - 1);
			}
		}
		for (auto& i : lst_candidate) {
			if (dct_counter_receiver[i] == n - 1 && dct_counter_giver[i] == 0){
				return i+1;
			}
		}
		return -1;
	}
	int strStr(std::string haystack, std::string needle) {
		int n = haystack.size(), m = needle.size();
		if (m == 0) {
			return 0;
		}
		std::vector<int> pi(m);
		for (int i = 1, j = 0; i < m; ++i) {
			while (j > 0 && needle[i] != needle[j]) {
				j = pi[j - 1];
			}
			if (needle[i] == needle[j]) {
				j++;
			}
			pi[i] = j;
		}
		for (int i = 0, j = 0; i < n; i++) {
			while (j > 0 && haystack[i] != needle[j]) {
				j = pi[j - 1];
			}
			if (haystack[i] == needle[j]) {
				j++;
			}
			if (j == m) {
				return i - m + 1;
			}
		}
		return -1;
	}
	int eatenApples(std::vector<int>& apples, std::vector<int>& days) {
		int num_days = apples.size();
		int eaten = 0;
		std::priority_queue<std::vector<int>> pq;
		for (int day = 1; day < num_days + 1; ++day) {
			pq.push({ -days[day - 1] - day, apples[day - 1] });
			auto i = pq.empty();
			while (!pq.empty()) {
				auto top = pq.top();
				pq.pop();
				if (top[1] > 0 && -top[0] > day) {
					top[1]--;
					eaten++;
					if(top[1]!=0)pq.push(top);
					break;
				}
			}
		}
		int day = num_days + 1;
		while (!pq.empty()) {
			auto top = pq.top();
			pq.pop();
			if (top[1] > 0 && -top[0] > day) {
				top[1]--;
				eaten++;
				if (top[1] != 0)pq.push(top);
			}
			else {
				continue;
			}
			day++;
		}
		return eaten;
	}
	bool isEvenOddTree(TreeNode* root) {
		int MAX_INT = 1e6 + 1;
		int	MIN_INT = 0;
		int pre_val = MIN_INT, pre_depth = 0;
		std::deque<std::pair<TreeNode*, int>> lst_bfs_ndoe{ {root,0} };
		while (!lst_bfs_ndoe.empty()) {
			auto ptr_pair = lst_bfs_ndoe.begin();

			if (ptr_pair->second != pre_depth) {
				if (ptr_pair->second % 2 == 0) {
					pre_val = MIN_INT;
				}
				else {
					pre_val = MAX_INT;
				}
			}

			if (ptr_pair->second % 2 == 0 && ptr_pair->first->val > pre_val && ptr_pair->first->val % 2 == 1) {
				;
			}
			else if(ptr_pair->second % 2 == 1 && ptr_pair->first->val < pre_val && ptr_pair->first->val % 2 == 0) {
				;
			}
			else {
				return false;
			}

			pre_val = ptr_pair->first->val;
			pre_depth = ptr_pair->second;
			if (ptr_pair->first->left) {
				lst_bfs_ndoe.emplace_back(std::make_pair(ptr_pair->first->left, ptr_pair->second + 1));
			}
			if (ptr_pair->first->right) {
				lst_bfs_ndoe.emplace_back(std::make_pair(ptr_pair->first->right, ptr_pair->second + 1));
			}
			lst_bfs_ndoe.pop_front();
		}
		return true;
	}
};

int Solution::a = 0;

void Solution::Test() {
	//std::string st = "[['X','.','.','X'],['.','.','.','X'],['.','.','.','X']]";
	//std::cin >> st;
	//for (auto& chr : st) {
	//	if (chr == '[') {
	//		chr = '{';
	//	}
	//	else if (chr == ']') {
	//		chr = '}';
	//	}
	//	else if (chr == '\"') {
	//		chr = '\'';
	//	}
	//}
	std::vector<int> aplles{ 2, 1, 10 };
	std::vector<int> days{ 2, 10, 1 };
	printf("%d", this->eatenApples(aplles, days));
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

class TopVotedCandidate {
private:
	std::vector<std::pair<int, int>> time_win;
public:
	TopVotedCandidate(std::vector<int>& persons, std::vector<int>& times) {
		std::unordered_map<int, int> person_score; // {person:score}
		std::vector<int> winner{ NULL,0 };
		for (int i = 1; i != persons.size() + 1; ++i) {
			if (++person_score[persons[i - 1]] >= winner[1]) {
				winner[0] = persons[i - 1];
				winner[1] = person_score[persons[i - 1]];
			}
			time_win.emplace_back(std::make_pair(times[i - 1], winner[0]));
		}
	}

	int q(int t) {
		int left = 0, right = time_win.size() - 1;
		if (t >= time_win[right].first) {
			return(time_win[right].second);
		}
		else if (t <= time_win[left].first) {
			return(time_win[left].second);
		}
		else {
			while (left <= right) {
				int mid = left + ((right - left) >> 1);
				if (time_win[mid].first == t) {
					return(time_win[mid].second);
				}

				else if (time_win[mid].first > t) {
					if (time_win[mid - 1].first <= t) {
						return(time_win[mid - 1].second);
					}
					right = mid;
				}
				else {
					if (time_win[mid + 1].first > t) {
						return(time_win[mid].second);
					}
					left = mid + 1;
				}
			}
			return -1;
		}

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
