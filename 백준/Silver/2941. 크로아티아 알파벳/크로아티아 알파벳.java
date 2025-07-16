import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public void solve() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        String input = st.nextToken();
        String[] arr = {"dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="};

        for (String val : arr) {
            input = input.replace(val, "*");
        }
        
        System.out.println(input.length());
    }

    public static void main(String args[]) throws Exception {
        new Main().solve();
    }
}