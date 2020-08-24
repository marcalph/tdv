
public class javaArrays {
    public static void main(String[] args) {

        int[]     ages     = {17, 21, 18, 19};
        boolean[] students = new boolean[4];
        students[0] = true;
        students[1] = false;
        students[2] = false;
        students[3] = true;

        for(int i = 0; i<ages.length; i++) {
            System.out.println(ages[i]);
        }
    }
}