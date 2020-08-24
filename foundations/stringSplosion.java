public class stringSplosion{
    public static String method(String str) {
        String res = "";
        for(int i = 1; i<=str.length(); i++) {
            res = res.concat(str.substring(0,i));
            }
        return res;
    }

    public static void main(String[] args){
        System.out.println(method("Code"));
        System.out.println(method("abc"));
        System.out.println(method("ab"));
    }
}
