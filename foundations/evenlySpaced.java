import java.lang.Math;
import java.util.Arrays;

public class evenlySpaced{
    public static boolean method(int a, int b, int c) {
        int[] nums = new int[] {a, b, c};
        nums =  Arrays.stream(nums).sorted().toArray();
        a = nums[0];
        b = nums[1];
        c = nums[2];
        return Math.abs(a-b)==Math.abs(c-b);
    }
    public static void main(String[] args){
        System.out.println(method(5, 7, 6));
        System.out.println(method(5, 6, 6));
    }
}
