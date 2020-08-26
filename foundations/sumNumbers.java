import java.util.Arrays;

public class sumNumbers{
    public static int method(String str) {
        if(str.length()>0){
            String[] strings= str.replaceAll("[^0-9]", " 0").trim().split("\\s+");
            int sum = Arrays.asList(strings).stream().mapToInt(Integer::parseInt).sum();
            return sum;
        }else{
            return 0;
        }
    }
    public static void main(String[] args){
        System.out.println(method("abc123xyz123"));
    }
}