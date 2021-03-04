public class Lintcode31 {
    /**
     * @param nums: The integer array you should partition
     * @param k: An integer
     * @return: The index after partition
     */
    public int partitionArray(int[] nums, int k) {
        // write your code here
        int low = 0, high = nums.length - 1;
        while (low < high){
            while (low < high && nums[high] <=k) high --;

            while (low < high && nums[low] >k) low ++;
            if (low < high){
                int temp = nums[low];
                nums[low] = nums[high];
                nums[high] = temp;
            }

        }
        return low;
    }
}
