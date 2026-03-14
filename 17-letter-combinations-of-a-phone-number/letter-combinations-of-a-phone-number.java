import java.util.*;

class Solution {

    public List<String> letterCombinations(String digits) {

        List<String> result = new ArrayList<>();

        if (digits.length() == 0) return result;

        String[] map = {
            "", "", "abc", "def", "ghi", "jkl",
            "mno", "pqrs", "tuv", "wxyz"
        };

        backtrack(result, digits, map, "", 0);

        return result;
    }

    public void backtrack(List<String> result, String digits, String[] map, String current, int index) {

        if (index == digits.length()) {
            result.add(current);
            return;
        }

        String letters = map[digits.charAt(index) - '0'];

        for (char c : letters.toCharArray()) {
            backtrack(result, digits, map, current + c, index + 1);
        }
    }
}
