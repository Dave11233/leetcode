public class LintCode1399 {
    /**
     * @param list: The coins
     * @param k: The k
     * @return: The answer
     */
    public int takeCoins(int[] list, int k) {
        // Write your code here
        if (k <= 0){
            return 0;
        }
        int left = 0;
        int right = k - 1;
        int sum = 0;
        int max = 0;
        for (int i = left; i <= right; i++) {
            sum += list[i];
        }
        left = list.length - 1;
        if (k >= list.length){
            return sum;
        }
        while (right >= 0){
            max = Math.max(max, sum);
            sum = sum - list[right] + list[left];
            left --;
            right --;

        }
        int sum2 = 0;
        int j = list.length - 1;
        for (int i = 0; i < k; i++, j--) {
            sum2 += list[j];
        }
        System.out.println(sum2);
        max = Math.max(max, sum2);
        return max;
    }

    public static void main(String[] args) {
        LintCode1399 lintCode1399 = new LintCode1399();
        System.out.println(lintCode1399.takeCoins(
                new int[]{639,9314,4100,2589,1895,1644,4292,1457,7371,939,2079,9594,4626,2482,2619,421,772,9812,8734,1089,4964,1369,8064,3411,1969,6818,738,940,7678,1049,6767,1048,913,1949,5378,5944,1145,3933,9960,1922,3716,1026,9319,7558,3855,2562,5968,3381,3871,8210,2769,7726,3104,2476,2061,5161,3948,9842,7952,7095,5230,6401,5278,9433,7768,1753,5483,1808,9729,1468,768,3253,291,1301,2109,3307,2148,7132,2506,7873,3523,7959,6339,4380,7462,6114,2595,2149,6290,1218,6703,2703,7322,2214,1238,8971,5563,5535,7720,8463,7160,9442,3797,9636,2737,6428,807,8863,4393,5254,4931,6771,2072,3608,5676,2245,8190,6178,8936,5824,9002,2505,3895,778,3098,8175,2081},
                47
        ));
    }

}
