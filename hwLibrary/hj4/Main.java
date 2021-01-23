import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;

        while ((str = br.readLine()) != null) {
            parse(str);
        }
    }

    static void parse(String str) {
        if (str.length() > 8) {
            System.out.println(str.substring(0, 8));
            // remove the first 8 digit
            String remaining = str.substring(8, str.length());
            parse(remaining);

        }else{
            int appendLen = 8 - str.length();
            str += String.join("", Collections.nCopies(appendLen, "0"));
            System.out.println(str);
        }
    }
}


