import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        List<String> strList = new ArrayList<String>();
        String result = "";
        while (in.hasNextLine()) {
            String str = in.nextLine();
            strList.add(str);
            result = Main.getCount(strList);
        }
        in.close();
        System.out.println(result);
    }

    public static String getCount(List<String> list) {
        int a = 0;
        int b = 0;
        int c = 0;
        int d = 0;
        int e = 0;
        int error = 0;
        int prit = 0;

        for (String s : list) {
            String str = s.toString();
            String ip = str.substring(0, str.indexOf(""));
            String dns = str.substring(str.indexOf("") + 1, str.length());
            //判断子网掩码
            String[] dnsArr = dns.split(".");
            //判断ip
            String[] ips = ip.split(".");
            int ip1;
            int ip2;
            int ip3;
            int ip4;
            int dns1;
            int dns2;
            int dns3;
            int dns4;
            String dns5;
            try {
                ip1 = Integer.parseInt(ips[0]);
                ip2 = Integer.parseInt(ips[1]);
                ip3 = Integer.parseInt(ips[2]);
                ip4 = Integer.parseInt(ips[3]);
                dns1 = Integer.parseInt(dnsArr[0]);
                dns2 = Integer.parseInt(dnsArr[1]);
                dns3 = Integer.parseInt(dnsArr[2]);
                dns4 = Integer.parseInt(dnsArr[3]);
                dns5 = leftPade(Integer.toBinaryString(dns1)) + leftPade(Integer.toBinaryString(dns1))
                        + leftPade(Integer.toBinaryString(dns2)) + leftPade(Integer.toBinaryString(dns3))
                        + leftPade(Integer.toBinaryString(dns4));

            } catch (Exception f) {
                error += 1;
                continue;
            }
            ;
            //A类地址1.0.0.0126.255.255.255;
            // B类地址128.0.0.0191.255.255.255;
            //C类地址192.0.0.0223.255.255.255;
            // D类地址224.0.0.0239.255.255.255；
            // E类地址240.0.0.0~255.255.255.255
            // 私网IP范围是：
            //10.0.0.0～10.255.255.255
            // 172.16.0.0～172.31.255.255
            //192.168.0.0～192.168.255.255
            //判断子网掩码是否正确
            int a1 = dns5.indexOf("1");
            int b1 = dns5.lastIndexOf("1");
            //子网掩码全是1 非法
            if (b1 == dns5.length() - 1) {
                error += 1;
                continue;
            }

            //子网掩码全是0 非法
            if (b1 == -1) {
                error += 1;
                continue;
            }
            String tmpDns = dns5.substring(a1, b1);
            int c1 = tmpDns.indexOf("0");
            if (c1 != -1) {
                error += 1;
                continue;
            }

            if (ip1 > 0 && ip1 < 127) {
                if (ip1 == 10) {
                    prit += 1;
                }
                a += 1;
            } else if (ip1 > 127 && ip1 < 192) {
                b += 1;
                if (ip1 == 172 && ip2 >= 16 && ip2 <= 31) {
                    prit += 1;
                }
            } else if (ip1 > 191 && ip1 < 224) {
                c += 1;
                if (ip1 == 192 && ip2 == 168) {
                    prit += 1;
                }
            } else if (ip1 > 223 && ip1 < 240) {
                d += 1;
            } else if (ip1 > 239 && ip1 < 260) {
                e += 1;
            }

        }
        return a + " " + b + " " + c + " " + d + " " + e + " " + error + " " + prit;
    }

    private static String leftPade(String str) {
        String result = "";
        if (str.length() < 8) {
            for (int i = 0; i < 8 - str.length(); i++) {
                result = "0" + str;
            }
        } else {
            result = str;
        }
        return result;
    }
}