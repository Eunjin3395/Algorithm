import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] st = br.readLine().split("");
        int[] arr = new int[10];

        for (String s: st){
            int n = Integer.parseInt(s);
            if (n==6) {
                arr[9]++;
            }else{
                arr[n]++;
            }

        }

        arr[9]=(int) Math.ceil(arr[9]/2.0);

        int answer = 0;

        for (int i : arr){
            if(i>answer){
                answer = i;
            }
        }
        System.out.println(answer);
    }
}
