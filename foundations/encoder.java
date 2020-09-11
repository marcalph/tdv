import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;

public class encoder{
    public static String[] method(String[] raw, String[] code_words) {
    String[] res = new String[raw.length];
    Map<String, String> map = new HashMap<String, String>();
    for (int i = 0; i <raw.length; i++) {
        if (!map.containsKey(raw[i])){
        map.put(raw[i], code_words[i]);
        }
    }
    for (int i = 0; i <raw.length; i++) {          
        res[i] = map.get(raw[i]);      
    }
    return res;
    }
    public static void main(String[] args){
        System.out.println(Arrays.toString(method("hello there hello".split(" "), "1 2 3 4".split(" "))));
    }
}
