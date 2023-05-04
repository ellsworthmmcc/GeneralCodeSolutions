class Solution {
public:
    bool isValid(string s) {

        // Using stack to keep track of the order of the parentheses
        stack<char> st;

        // Iterating over every element in the string
        for (char ch:s) {

            // If current element is an opening character, push onto stack
            if (ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);

            // If current element is closing character, check if there is a possible
            // matching opening character, if there is a possibility check that
            // the most recent opening character matches
            } else {
                if (st.empty() ||
                (st.top() == '(' && ch != ')') || 
                (st.top() == '[' && ch != ']') ||
                (st.top() == '{' && ch != '}')) {
                    return false;
                }

                // Opening character has found matching closing character, pop off stack
                st.pop();
            }
        }
    
        // If empty, all closing have found parentheses
        return st.empty();
    }
};
