public class Leetcode460 {
    /**
     * @param A: an integer array
     * @param target: An integer
     * @param k: An integer
     * @return: an integer array
     */
    public int[] kClosestNumbers(int[] A, int target, int k) {
        // write your code here
        int abs_min = Integer.MAX_VALUE;
        int index = 0;
        for (int i = 0; i < A.length; i++) {
            if (abs_min > Math.abs(A[i] - target)){
                index = i;
                abs_min = Math.abs(A[i] - target);
            }
        }
        int counter = 1;
        int res[] = new int[k];
        res[0] = A[index];
        int left = index - 1;
        int right = index + 1;
        while (counter < k){
            if (left >= 0 && right <= A.length - 1){
                if (Math.abs(A[left]-target) < Math.abs(A[right]-target)){
                    res[counter++] = A[left--];
                }else{
                    res[counter++] = A[right++];
                }
            }
            else if(left < 0){
                res[counter++] = A[right++];
            }
            else if(right > A.length - 1){
                res[counter++] = A[left--];
            }else{
                break;
            }

        }
        return res;
    }
}
