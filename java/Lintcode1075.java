public class Lintcode1075 {
    /**
     * @param nums: an array
     * @param k: an integer
     * @return: the number of subarrays where the product of all the elements in the subarray is less than k
     */
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int ans = 0;
        int total = 1;
        int left=0, right = 0;
        while(left < nums.length){
            if(right < nums.length){
                total *= nums[right++];
                if(total < k){
                    if (right - left != 1){
                        ans += 1;
                    }

                }else {
                    if (nums[left] < k) {
                        ans += 1;
                    }
                    total /= nums[left];
                    if (total < k){
                        ans ++;
                    }
                    left++;
                }
            }else{

                    if (nums[left] < k){
                        ans ++;
                    }
                    total /= nums[left ++];
                    if(total < k){
                        ans ++;
                    }

            }

        }


        return ans;
    }

    public static void main(String[] args) {
        Lintcode1075 lintcode1075 = new Lintcode1075();
        System.out.println(lintcode1075.numSubarrayProductLessThanK(
                new int[]{10,2,2,5,4,4,4,3,7,7}, 289
        ));
    }
}
