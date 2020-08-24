
public class javaStrings {
    public static void main(String[] args) {

        String message = "Goodbye World!";

        message = message.concat(" Lovely day, innit?");
        message = message.replace("o", "0");
        message = message.replace("e", "3");
        message = message.toUpperCase();

        System.out.println(message);

        char[] characters = message.toCharArray();

        for(char c: characters) {

            System.out.println(c);

        }

    }
}