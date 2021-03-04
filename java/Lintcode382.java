import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Lintcode382 {
    public int triangleCount(int[] S) {
        if (S.length < 3){
            return 0;
        }
        Arrays.sort(S);
        int ans = 0;
        for (int i = 1; i < S.length - 1; i++) {
            int left = 0;
            int right = i - 1;

            while (left < right){
                if (S[left] + S[right] > S[i]){
                    ans += right - left;
                    right --;
                }else {
                    left ++;
                }
            }
        }
        return ans;


    }
}
