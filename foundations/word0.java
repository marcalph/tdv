import java.util.Map;
import java.util.HashMap;

public class word0{
    public static Map<String, Integer> method(String[] strings) {
        Map<String, Integer> map = new HashMap();
        for (String s:strings) {
            map.put(s, 0);
        }
        return map;
    }
    public static void main(String[] args){
        System.out.println(method("hello there hello".split("")));
    }
}
