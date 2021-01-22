import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;

        while ((str = br.readLine()) != null) {
            boolean[] flags = new boolean[1001];
            StringBuilder sb = new StringBuilder();

//          输入个数
            int n = Integer.parseInt(str);

            for (int i = 0; i < n; i++) {
        flags[Integer.parseInt(br.readLine())] = true;
            }

            for (int i = 1; i < 1001; i++) {
                if (flags[i]) {
                    sb.append(i).append("\n");
                }
            }

            sb.deleteCharAt(sb.length() - 1);
            System.out.println(sb.toString());
        }
    }
}


