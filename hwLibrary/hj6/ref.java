import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // inputted value
        int val = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 2; i * i <= val; i++) {
            if (val % i == 0) {
                sb.append(i).append(" ");
                val /= i;
                i--;
            }
        }
        sb.append(val).append(" ");
        System.out.println(sb);
        br.close();
    }
}