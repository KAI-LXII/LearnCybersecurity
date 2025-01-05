/**
 * Partial leetcode solution to Problem #273.
 * This algorithm fails in the "Teen" numbers (19, 12, 13, etc.), but otherwise can accomadate turning any positive integer from 1 to 2^31 into text.
 * All that would theorertically need to be added is an extra case with the right parameters at line 35 that looks one digit ahead, checks if it's in a valid "teening"
 * position, then removes two digits from the iteration rather than one.
 */

#include <iostream>

using namespace std;


class Solution
{
public:
    string numberToWords(int num)
    {
        return process(num);
    }

    string process(int num)
    {
        int digit;
        int iter = 1;
        string ret = "";
        string add;
        while (num != 0)
        {
            digit = num % 10;

            ret = getPrefix(iter) + (ret != "" && getPrefix(iter) != "" ? " " : "") + ret;
            if (iter % 3 == 2)
            {
                ret = getTens(digit) + (ret != "" && getTens(iter) != "" ? " " : "") + ret;
            }
            else
            {
                ret = getSingles(digit) + (ret != "" && getSingles(iter) != "" ? " " : "") + ret;
            }

            num = num - digit;
            num = num / 10;
            iter++;
        }

        return ret;
    }

    string getPrefix(int iter)
    {
        string ret;

        if (iter % 3 == 0)
        {
            return "Hundered";
        }
        switch (iter)
        {
        case 4:
            return "Thousand";
            break;

        case 7:
            return "Million";
            break;

        case 9:
            return "Billion";
            break;
        }

        return "";
    }

    string getTens(int val)
    {
        switch (val)
        {
        case 1:
            return "Ten";
            break;

        case 2:
            return "Twenty";
            break;

        case 3:
            return "Thirty";
            break;

        case 4:
            return "Fourty";
            break;

        case 5:
            return "Fifty";
            break;

        case 6:
            return "Sixty";
            break;

        case 7:
            return "Seventy";
            break;

        case 8:
            return "Eighty";
            break;

        case 9:
            return "Ninety";
            break;
        }

        return "";
    }

    string getSingles(int val)
    {
        switch (val)
        {
        case 1:
            return "One";
            break;

        case 2:
            return "Two";
            break;

        case 3:
            return "Three";
            break;

        case 4:
            return "Four";
            break;

        case 5:
            return "Five";
            break;

        case 6:
            return "Six";
            break;

        case 7:
            return "Seven";
            break;

        case 8:
            return "Eight";
            break;

        case 9:
            return "Nine";
            break;
        }

        return "";
    }
};

int main() {
    Solution s;
    cout << s.numberToWords(12345);
}


