public class Lintcode1870 {
    public int stringCount(String str) {
        int[] dp = new int[str.length()];
        int res = 0;
        if (str.charAt(0) == '0'){
            dp[0] = 1;
            res += 1;
        }

        for (int i = 1; i < str.length(); i++) {
            if (str.charAt(i) == '0'){
                dp[i] = dp[i-1] + 1;
                res += dp[i];
            }
        }
        return res;

    }
}
