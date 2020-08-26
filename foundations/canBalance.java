public class canBalance {
    public static boolean method(int[] nums){
        int lSum=0;
        for (int i = 0; i < nums.length; i++) {
            lSum += nums[i];
            int rSum = 0;
            for (int j = nums.length-1; j > i; j--) {
                rSum += nums[j];
            }
            if (rSum == lSum)
                return true;
        }
        return false;
    }

    public static void main(String[] args){
        System.out.println(method(new int[] {1, 1, 1, 2,1}));
        System.out.println(method(new int[] {2, 1, 1, 2,1}));
        System.out.println(method(new int[] {10, 10}));
    }

}