public class Lintcode1375 {
    public long kDistinctCharacters(String s, int k) {
        // Write your code here
        int[] map = new int[26];
        int count = 0;

        int left = 0, right = 0;

        int len = s.length();

        long sum = 0;

        while (left <=right && right < len) {
            char newChar = s.charAt(right);
            map[newChar - 'a']++;

            if (map[newChar - 'a'] == 1) {
                // When new right char does not exist in the window
                count++;

                if (count == k) {
                    // When the occurrence of new right char makes the window meet the criteria, do the count.
                    sum += len - right;

                    // And shrink the window by moving left pointer
                    while (left < len && count >= k) {
                        char charToRemove = s.charAt(left);

                        map[charToRemove - 'a']--;
                        if (map[charToRemove - 'a'] == 0) {
                            // Windows is shrinked to have only k-1 item, can start to move right again.
                            count--;
                            right++;
                        } else {
                            // Without the current leftmost char, the remaining sub-window is still valid. do the count.
                            sum += len - right;
                        }
                        left++;
                    }
                } else {
                    // Otherwise, keep expanding window by moving right pointer
                    right++;
                }
            } else {
                // When new right char exists in the window, increase the count of its occurrence
                right++;
            }
        }

        return sum;
    }
}
