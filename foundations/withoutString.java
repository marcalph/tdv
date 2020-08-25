public class withoutString{
    public static String method(String base, String remove) { 
        int remIdx = base.toLowerCase().indexOf(remove.toLowerCase());
        if (remIdx == -1)
            return base;
        return base.substring(0, remIdx ) + 
            method(base.substring(remIdx + remove.length()) , remove);
    }
    public static void main(String[] args){
        System.out.println(method("hello there", "llo"));
    }
}
