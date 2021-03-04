public class Leetcode1712 {
    public int searchLocation(int[] prefix, int start){
        int high = prefix.length - 1;
        int low = start+1;
        while(low <= high){
            int mid = low + (high - low) >>> 1;
            if (prefix[mid] - prefix[start - 1] > prefix[start - 1]){
                high = mid - 1;
            }else if (prefix[mid] - prefix[start - 1] == prefix[start - 1]){
                return mid;
            }else {
                low = mid + 1;
            }
        }
        return low;
    }
    public int waysToSplit(int[] nums) {
        if (nums == null || nums.length < 3){
            return 0;
        }
        int ans = 0;
        int[] prefix_sum = new int[nums.length];
        prefix_sum[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            prefix_sum[i] = prefix_sum[i-1] + nums[i];
        }

        int total = prefix_sum[prefix_sum.length - 1];

        int i = 1;
        do {
            int location = searchLocation(prefix_sum, i);
            while (location < nums.length){
                int mid = prefix_sum[location] - prefix_sum[i-1];
                if (mid < total - prefix_sum[location]){
                    break;
                }
                ans += 1;
                location += 1;
            }
            i++;
        }while (i < nums.length - 1);
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(
                new Leetcode1712().waysToSplit(new int[] {1,1,1})
        );
    }
}
