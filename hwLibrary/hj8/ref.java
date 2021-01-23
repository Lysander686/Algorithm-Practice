import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.io.StreamTokenizer; /*
    read input from terminal
*/ 

/**
 * 合并表记录,先输入键值对的个数
 * 然后输入成对的index和value值，以空格隔开
 * 4
 * 0 1
 * 0 2
 * 1 2
 * 3 4
 *
 * 0 3
 * 1 2
 * 3 4
 *
 * time complexity: O(n)
 */
public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        st.nextToken();      // 分隔符
        int n = (int) st.nval;   // 强转
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            st.nextToken();
            int key = (int) st.nval;
            st.nextToken();
            int value = (int) st.nval;
            arr[key] = arr[key] + value;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length ; i++) {
            if(arr[i] != 0){
                sb.append(i).append(" ").append(arr[i]).append("\n");
            }
        }
        System.out.println(sb.toString());
    }
}
