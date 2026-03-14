class Solution {
    public int divide(int dividend, int divisor) {
        
        if(dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        
        long a = Math.abs((long) dividend);
        long b = Math.abs((long) divisor);
        
        int result = 0;
        
        while(a >= b) {
            
            int shift = 0;
            
            while(a >= (b << shift)) {
                shift++;
            }
            
            shift--;
            a -= (b << shift);
            result += (1 << shift);
        }
        
        if((dividend > 0) ^ (divisor > 0)) {
            result = -result;
        }
        
        return result;
    }
}
