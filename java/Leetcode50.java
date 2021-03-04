public class Leetcode50 {
    public double myPow(double x, int n) {
        if(n >= 0){
            return helper(x, n);
        }
        else return 1/helper(x, -n);
    }

    public double helper(double x, int n){
        if(n == 0){
            return 1;
        }
        if(n == 1){
            return x;
        }
        if( (n & 1) == 0){
            return helper(x, n >>> 1) * helper(x, n >>> 1);
        }else{
            return x * helper(x, (n-1)>>> 1) * helper(x, (n-1)>>>1);
        }
    }

    public static void main(String[] args) {
        System.out.println(
                new Leetcode50().myPow(2.00000,
                        -2147483648)
        );
    }
}
