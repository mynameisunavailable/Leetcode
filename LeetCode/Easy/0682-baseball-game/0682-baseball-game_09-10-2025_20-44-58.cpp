#include <iostream>
#include <vector>
#include <cctype>
#include <cstdlib>
using namespace std;

class Solution {
public:
    int calPoints(vector<string>& operations)
    {
        string op;
        vector<int> scores;
        int num, len;
        for (size_t i = 0; i < operations.size(); i++)
        {
            op = operations[i];
            // cout << operations[i];
            len = scores.size();
            if (isdigit(op[op.size() - 1]))
            {
                scores.push_back(stoi(op));
            }
            else if (op == "+")
            {
                num = scores[len - 1] + scores[len - 2];
                scores.push_back(num);
            }
            else if (op == "D")
            {
                num = scores[len - 1] * 2;
                scores.push_back(num);
            }
            else if (op == "C")
            {
                scores.pop_back();
            }
        }
        //add all in scores
        num = 0;
        for (size_t i = 0; i < scores.size(); i++)
        {
            num += scores[i];
        }
        return num;
    }
};