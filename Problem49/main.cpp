// An initial problem solution, meant to test out leetcode difficulty.
// Problem was to find all words that could be anagrams in a list of strings, then return them as a list of lists of strings.

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ret;
        for (int i = 0; i < strs.size(); i++) {
            bool successfullyFoundList = false;
            for (int j = 0; j < ret.size(); j++) {
                if (makeAlpha(strs.at(i)) == makeAlpha(ret.at(j).front())) {
                    successfullyFoundList = true;
                    ret.at(j).push_back(strs.at(i));
                }
            }

            if (!successfullyFoundList) {
                vector<string> newList;
                newList.push_back(strs.at(i));
                ret.push_back(newList);
            }
            
        }
        return ret;
    }

    string makeAlpha(string str) {
        std::sort(str.begin(), str.end());
        return str;
    }
};
