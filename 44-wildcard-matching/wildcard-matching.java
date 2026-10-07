class Solution {
    public boolean isMatch(String s, String p) {
        int sIdx = 0, pIdx = 0;
        int starIdx = -1;   // index of last seen '*' in pattern
        int sMatch = 0;    // index in s to retry when '*' backtracks

        while (sIdx < s.length()) {
            // Direct match or '?'
            if (pIdx < p.length() && (p.charAt(pIdx) == '?' || p.charAt(pIdx) == s.charAt(sIdx))) {
                sIdx++;
                pIdx++;
            }
            // Found a '*' — remember its position and current sIdx
            else if (pIdx < p.length() && p.charAt(pIdx) == '*') {
                starIdx = pIdx;
                sMatch = sIdx;
                pIdx++;
            }
            // Mismatch: backtrack to last '*' and let it consume one more char
            else if (starIdx != -1) {
                pIdx = starIdx + 1;
                sMatch++;
                sIdx = sMatch;
            }
            // No match and no '*' to backtrack on
            else {
                return false;
            }
        }

        // Consume any remaining '*' in pattern (they can match empty string)
        while (pIdx < p.length() && p.charAt(pIdx) == '*') {
            pIdx++;
        }

        // Match if pattern is fully consumed
        return pIdx == p.length();
    }
}