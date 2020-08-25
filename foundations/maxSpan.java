import java.util.HashMap;
import java.util.List; 
import java.util.ArrayList;
import java.util.Map;


public class maxSpan{
    public static int method(int[] nums) { 
        int max = 0;
        for(int i = 0; i < nums.length; i++) {
            int j = nums.length - 1;
            while(nums[i] != nums[j])
                j--;

            int span = j - i + 1;

            if(span > max)
                max = span;
        }
        return max;
    }
    public static void main(String[] args){
        System.out.println(method(new int[] {1, 2, 3,2,17}));
    }
}
