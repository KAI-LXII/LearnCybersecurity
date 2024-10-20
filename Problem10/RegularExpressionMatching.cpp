// Implement pattern matching for . and *,
// Where . matches any single character.
// * Matches zero ormore of the preceeding element.


#include <string>
#include <iostream>
using namespace std;

class Solution
{
    // A kind of hacky solution I wrote. Should be O(n).
public:
    bool isMatch(string s, string p)
    {
        // Create a char for selected characters by *.
        char selectedStar;

        // For each character of the string.
        for (int i = 0; i < s.size(); i++)
        {
            // If the character is a star, look behind the current character, and loop forward as long as that character is repeated.
            if (p[i] == '*')
            {
                selectedStar = s[i - 1];
                while ((s[i] == selectedStar || selectedStar == '.') && i != s.size())
                {
                    i++;
                }
            }
            // If it's a period, simply iterate forward and do nothing.
            else if (p[i] == '.')
            {
            }
            // If it's a character (Only other option), compare the characters. if they aren't the same, return false.
            else
            {
                if (s[i] != p[i])
                {
                    return false;
                }
            }
        }
        return true;
    }
};

int main() {
    Solution* s = new Solution();

    cout << s->isMatch("aa", "a") << endl;
    cout << s->isMatch("aa", "a*") << endl;
    cout << s->isMatch("ab", ".*") << endl;
}