import java.util.Map;
import java.util.HashMap;
public class mapShare {

    public static Map<String, String> method(Map<String, String> map){
        if(map.containsKey("c")) map.remove("c");
        if(map.containsKey("a")) map.put("b", map.get("a"));
        return map;
    }

    public static void main(String[] args){
        Map<String,String> map = new HashMap<String, String>();
        map.put("a","aaa");
        map.put("b","bbb");
        map.put("c","ccc");
        System.out.println(method(map));
    }

}