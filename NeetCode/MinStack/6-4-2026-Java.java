// Encoded Stack
// Space Complexity: O(n)
class MinStack {
    long min;
    private Stack<Long> stack;

    public MinStack() {
        // Time Complexity:  O(1)
        // Space Complexity: O(1)

        stack = new Stack<>();
    }
    
    public void push(int val) {
        // Time Complexity:  O(1)
        // Space Complexity: O(1)

        if (stack.isEmpty()) {
            stack.push(0L);
            min = val;
        } else {
            stack.push(val - min);
            if (val < min) min = val;
        }
    }
    
    public void pop() {
        // Time Complexity: O(1)
        // Space Complexity O(1)

        if (stack.isEmpty()) return;

        long top = stack.pop();

        if (top < 0) min = min - top;
    }
    
    public int top() {
        // Time Complexity: O(1)
        // Space Complexity O(1)

        long top = stack.peek();
        if (top > 0) {
            return (int) (top + min);
        } else {
            return (int) min;
        }
    }
    
    public int getMin() {
        // Time Complexity: O(1)
        // Space Complexity O(1)

        return (int) min;
    }
}

// Two Stacks
// Space Complexity: O(n)
class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;

    public MinStack() {
        // Time Complexity:  O(1)
        // Space Complexity: O(1)

        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        // Time Complexity:  O(1)
        // Space Complexity: O(1)

        stack.push(val);
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }
    
    public void pop() {
        // Time Complexity: O(1)
        // Space Complexity O(1)

        if (stack.isEmpty()) return;

        int top = stack.pop();

        if (top == (int) minStack.peek()) {
            minStack.pop();
        }
    }
    
    public int top() {
        // Time Complexity: O(1)
        // Space Complexity O(1)

        return stack.peek();
    }
    
    public int getMin() {
        // Time Complexity: O(1)
        // Space Complexity O(1)

        return minStack.peek();
    }
}
