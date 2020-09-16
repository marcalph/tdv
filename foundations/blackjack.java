import java.lang.Math;
public class blackjack{
    public static int method(int a, int b){
        int maxab = Math.max(a,b);
        int minab = Math.min(a,b);
        if (maxab>21){
            if(minab>21){
                return 0;  
            }
            else{
                return minab;
            }
        }
        else{
            return maxab;
        }
    }
    public static void main(String[] args){
        System.out.println(method(19,21));
        System.out.println(method(22,23));
    }
}