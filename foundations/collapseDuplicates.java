public class collapseDuplicates{
    public static String method(String a) {
        if (a.length()<1) return "";
        String result = ""+a.charAt(0);
        for  (int i=1; i< a.length(); i++){
            char ch = a.charAt(i); 
            if (ch != result.charAt(result.length()-1)) result += ch;
        }
        return result;
    }

    public static void main(String[] args){
        System.out.println(method("ccooodeee"));
        System.out.println(method("abc"));
        System.out.println(method("abbbbb"));
    }
}
