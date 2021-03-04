public class Lintcode1474 {
    /**
     * @param k: The number of words in the article
     * @param lim: TThe minimum number of words a phrase should contain
     * @param str: The article
     * @return: Return the length of shortest phrase
     */
    public int getLength(int k, int lim, String[] str) {
        // Write your code here
        int[] length = new int[str.length];
        for (int i = 0; i < str.length; i++) {
            length[i] = str[i].length();
        }
        int left = 0, right = 0;
        int current_len = 0;
        int min_len = Integer.MAX_VALUE;
        while(right < str.length){
            if (right - left < k){
                current_len += length[right];
                right ++;
            }else{

                if (current_len > lim){
                    min_len = Math.min(min_len, current_len);
                    current_len -= length[left];
                    left ++;
                }else if(current_len < lim){
                    current_len += length[right];
                    right ++;
                }else {
                    return lim;
                }
            }

        }


        return min_len;
    }
}
