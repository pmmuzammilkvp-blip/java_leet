import java.util.*;

class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        
        List<Integer> result = new ArrayList<>();
        if(s.length() == 0 || words.length == 0) return result;

        int wordLen = words[0].length();
        int wordCount = words.length;

        Map<String, Integer> wordMap = new HashMap<>();
        for(String w : words){
            wordMap.put(w, wordMap.getOrDefault(w, 0) + 1);
        }

        for(int i = 0; i < wordLen; i++) {

            int left = i;
            int count = 0;
            Map<String, Integer> seen = new HashMap<>();

            for(int right = i; right + wordLen <= s.length(); right += wordLen) {

                String word = s.substring(right, right + wordLen);

                if(wordMap.containsKey(word)) {

                    seen.put(word, seen.getOrDefault(word, 0) + 1);
                    count++;

                    while(seen.get(word) > wordMap.get(word)) {
                        String leftWord = s.substring(left, left + wordLen);
                        seen.put(leftWord, seen.get(leftWord) - 1);
                        left += wordLen;
                        count--;
                    }

                    if(count == wordCount) {
                        result.add(left);
                    }

                } else {
                    seen.clear();
                    count = 0;
                    left = right + wordLen;
                }
            }
        }

        return result;
    }
}
