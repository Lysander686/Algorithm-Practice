import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String s = input.readLine();
        int[] a = new int[128];
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char b = s.charAt(i);
            if (a[b] == 0) {
                count++;
                a[b] = 1;
            }
        }
        System.out.println(count);
    }
}