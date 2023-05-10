/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {

    // Time Complexity:  O(log(n)))
    // Space Complexity: 1

    // Base Case
    if (dividend === 0) {
        return 0;
    }

    var isNegative = false;
  
    // If only one of dividend or divisor is negative, set isNegative to true
    if ((dividend) > 0 !== (divisor > 0)) {
        isNegative = true;
    }
    
    // Gets the non-negative value of divisor and dividend
    divisor = Math.abs(divisor);
    dividend = Math.abs(dividend);

    // Res is the result to be returned at the end
    // Mul is what we alter the dividend by
    // Count is what we add onto result to detemrine divided amount
    var res = 0, 
        mul = divisor, 
        count = 1;

    // Loops until divisor is greater than dividend
    // Uses bitshifting to calculate division
    while (dividend >= divisor) {

        // Resets count and mul
        count = 1;
        mul = divisor;

        // Sets mul and count
        while (mul <= (dividend >> 1)) {
          mul = mul << 1;
          count = count << 1;
        }
        
        // Adds count to result and remove the divided amount from mul
        res += count;
        dividend -= mul;
    }

    // If ret goes over the limits of the allowed parameters, set it to the maximum possible
    if (res > ((2**31) - 1)) {
        return isNegative ? -(2**31) : 2**31 - 1
    }

    return isNegative ? -res : res
};
