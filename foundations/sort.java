import java.util.Arrays;
public class sort{
    public static int[] method(int[] nums){
        return Arrays.stream(nums).distinct().sorted().toArray();
    }
    public static void main(String[] args){
        System.out.println(Arrays.toString(method(new int[] {})));
        System.out.println(Arrays.toString(method(new int[] {1})));
        System.out.println(Arrays.toString(method(new int[] {1,2,3,2,1})));
    }
}