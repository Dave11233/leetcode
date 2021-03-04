import java.util.Arrays;

public class Lintcode59 {
    public int threeSumClosest(int[] numbers, int target) {
        // write your code here
        if (numbers.length < 3){
            return 0;
        }
        int ans = Integer.MAX_VALUE;
//        System.out.println();
        Arrays.sort(numbers);
//        System.out.println(numbers);

        for (int i = 1; i < numbers.length - 1; i++) {
            int left = 0;
            int right = numbers.length - 1;

            while (left < i && right > left && right > i){
                int threeSum = numbers[left] + numbers[i] + numbers[right];
                System.out.println(left +"\t"+i+"\t"+right+"\t"+threeSum);
                if (threeSum == target){
                    return target;
                }else if (threeSum > target){
                    if (Math.abs(threeSum - target) < Math.abs(ans - target)){
                        ans = threeSum;
                    }
                    right --;
                }else {
                    if (Math.abs(threeSum - target) < Math.abs(ans - target)){
                        ans = threeSum;
                    }
                    left ++;
                }


            }
        }

        return ans;
    }

    public static void main(String[] args) {
        System.out.println(
                new Lintcode59().threeSumClosest(
                        new int[]{-2,-3,5,-1,-4,5,-11,7,1,2,3,4,-7,-1,-2,-3,-4,-5},45
                )
        );
    }
}
