import java.util.*;

public class Lintcode57 {
    /**
     * @param numbers: Give an array numbers of n integer
     * @return: Find all unique triplets in the array which gives the sum of zero.
     */
    public List<List<Integer>> threeSum(int[] numbers) {
        // write your code here
        if (numbers.length < 3){
            return null;
        }
        Arrays.sort(numbers);
        Set<List<Integer>> set = new HashSet<>();
        for (int i = 1; i < numbers.length - 1; i++) {
            int left = 0;
            int right = numbers.length - 1;
            while (left < i && right > i){
                if (numbers[left] + numbers[i] + numbers[right] == 0){
                    set.add(Arrays.asList(numbers[left],numbers[i],numbers[right]));
                    left ++;
                    right --;
                }else if (numbers[left] + numbers[i] + numbers[right] > 0){
                    right --;
                }else {
                    left ++;
                }
            }
        }
        return new ArrayList<>(set);
    }
}
