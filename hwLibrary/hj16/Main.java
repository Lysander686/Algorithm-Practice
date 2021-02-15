import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {


    public static boolean getInput(String str, String[] command) {

        

        Pattern r = Pattern.compile("^([ASWD])(\\d+)$");
        Matcher matchRes = r.matcher(str);

        if (matchRes.find()) {

            command[0] = matchRes.group(1);
            command[1] = matchRes.group(2);

            return true;
        }


        return false;


    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str;
        int x = 0, y = 0;

        // 移动步长
        int length;
        // 移动方向
        String direction;

        str = br.readLine();

        String[] commands = str.split(";");

        String[] command = new String[2];

        for (String each : commands) {

            if (!getInput(each, command)) {
                continue;
            }

            direction = command[0];
            length = Integer.parseInt(command[1]);

            switch (direction) {
                case "A":
                    x -= length;
                    break;
                case "D":
                    x += length;
                    break;
                case "S":
                    y -= length;
                    break;
                case "W":
                    y += length;
                    break;


            }

        }

        System.out.println(String.valueOf(x) + "," + String.valueOf(y));

    }
}