import java.util.Map;
import java.util.HashMap;

public class wordLen{
    public static Map<String, Integer> method(String[] strings) {
        Map<String, Integer> map = new HashMap<String, Integer>();
        for (String s:strings) {
            map.put(s, s.length());
        }
        return map;
    }
    public static void main(String[] args){
        System.out.println(method("hello there hello".split(" ")));
    }
}
