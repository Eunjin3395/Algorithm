import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String t = br.readLine();

        String temp1 = "";
        String temp2 = "";

        for (int i = 0; i < t.length(); i++) {
            temp1 += s;
        }
        for (int i = 0; i < s.length(); i++) {
            temp2 += t;
        }

        if (temp1.equals(temp2)) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}
