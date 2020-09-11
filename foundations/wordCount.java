import java.util.Map;
import java.util.HashMap;

public class wordCount{
    public static Map<String, Integer> method(String[] strings) {
        Map<String, Integer> map = new HashMap<String, Integer>();
        for (String s:strings) {
            if (map.containsKey(s)){
            map.put(s, map.get(s)+1);
            }
            else {
            map.put(s, 1); 
            }
        }
        return map;
    }
    public static void main(String[] args){
        System.out.println(method("hello there hello".split(" ")));
    }
}
