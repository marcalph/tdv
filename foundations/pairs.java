import java.util.Map;
import java.util.HashMap;

public class pairs{
    public static Map<String, String> method(String[] strings) {
        Map<String, String> map = new HashMap<String, String>();
        for (String s:strings) {
            map.put(s.substring(0,1), s.substring(s.length()-1, s.length()));
        }
        return map;
    }
    public static void main(String[] args){
        System.out.println(method("hello there general kenobi".split(" ")));
    }
}
