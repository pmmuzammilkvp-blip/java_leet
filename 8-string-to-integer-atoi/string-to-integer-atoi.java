class Solution {
    public int myAtoi(String s) {
        // Handle empty or null string
        if (s == null || s.length() == 0) {
            return 0;
        }
        
        int i = 0;
        int n = s.length();
        
        // Skip leading whitespace
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }
        
        // If we've reached the end after whitespace
        if (i >= n) {
            return 0;
        }
        
        // Check for sign
        int sign = 1;
        if (s.charAt(i) == '-') {
            sign = -1;
            i++;
        } else if (s.charAt(i) == '+') {
            i++;
        }
        
        // Convert digits to integer
        int result = 0;
        while (i < n && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';
            
            // Check for overflow before adding the digit
            if (result > Integer.MAX_VALUE / 10 || 
                (result == Integer.MAX_VALUE / 10 && digit > Integer.MAX_VALUE % 10)) {
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            
            result = result * 10 + digit;
            i++;
        }
        
        return sign * result;
    }
    
    // Test method to verify the implementation
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test cases
        System.out.println("Input: \"42\" → Output: " + solution.myAtoi("42"));                    // 42
        System.out.println("Input: \"   -042\" → Output: " + solution.myAtoi("   -042"));          // -42
        System.out.println("Input: \"1337c0d3\" → Output: " + solution.myAtoi("1337c0d3"));        // 1337
        System.out.println("Input: \"   -42\" → Output: " + solution.myAtoi("   -42"));            // -42
        System.out.println("Input: \"4193 with words\" → Output: " + solution.myAtoi("4193 with words")); // 4193
        System.out.println("Input: \"words and 987\" → Output: " + solution.myAtoi("words and 987"));   // 0
        System.out.println("Input: \"-91283472332\" → Output: " + solution.myAtoi("-91283472332"));      // -2147483648
        System.out.println("Input: \"91283472332\" → Output: " + solution.myAtoi("91283472332"));        // 2147483647
        System.out.println("Input: \"\" → Output: " + solution.myAtoi(""));                              // 0
        System.out.println("Input: \"   \" → Output: " + solution.myAtoi("   "));                        // 0
        System.out.println("Input: \"+-12\" → Output: " + solution.myAtoi("+-12"));                      // 0
        System.out.println("Input: \"00000-42a1234\" → Output: " + solution.myAtoi("00000-42a1234"));    // 0
        System.out.println("Input: \"   +0 123\" → Output: " + solution.myAtoi("   +0 123"));            // 0
        System.out.println("Input: \"21474836460\" → Output: " + solution.myAtoi("21474836460"));        // 2147483647
        System.out.println("Input: \"-2147483649\" → Output: " + solution.myAtoi("-2147483649"));        // -2147483648
        System.out.println("Input: \"2147483648\" → Output: " + solution.myAtoi("2147483648"));          // 2147483647
        System.out.println("Input: \"-2147483648\" → Output: " + solution.myAtoi("-2147483648"));        // -2147483648
    }
}