class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        # Checks if it is possible for x to be palindrome,
        # cant be palindrome if negative or an even number greater than 0 ending in 0
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        
        # revX is used to become the reverse of x
        revX: int = 0

        # Loops until half point of x has been reached or passed
        while x > revX:
            revX = revX * 10 + x % 10
            x //= 10

        # Evalutes whether x and revX are equal for both odd and even cases,
        # if either is true x is a palindrome
        return (x == revX or x == revX // 10)
