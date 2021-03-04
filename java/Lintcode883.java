public class Lintcode883 {
    /**
     * @param nums: a list of integer
     * @return: return a integer, denote  the maximum number of consecutive 1s
     */
    public int findMaxConsecutiveOnes(int[] nums) {
        // write your code here
        int ans = 0;
        int left = 0, right = 0;
        int zeroCounter = 0;
        while(right < nums.length){
            if (nums[right] == 0){
                zeroCounter ++;
                if (zeroCounter > 1){
                    while (left < right && zeroCounter != 1){
                        if (nums[left] == 0){
                            zeroCounter --;
                        }
                        left += 1;
                    }
                }
                right += 1;
            } else {
                right += 1;
                ans = Math.max(ans, right - left);

            }

        }

        return ans;
    }
}
