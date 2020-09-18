public class makeBricks {
    public static boolean method(int small, int big, int goal){
        int bigs = goal/5;
        if (big>= bigs){
            int smalls = (goal-bigs*5);
            if (small>=smalls){
            return true;
            }
            else {
            return false;
            }
        }
        else{
            int smalls = (goal-big*5);
            if (small>=smalls){
            return true;
            }
            else {
            return false;
            }
        }
    }

    public static void main(String[] args){
        System.out.println(method(3,1,8));
        System.out.println(method(3,1,9));
    }

}