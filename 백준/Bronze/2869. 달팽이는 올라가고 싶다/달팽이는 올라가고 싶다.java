import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        br.close();
        long A = Long.parseLong(st.nextToken()); //낮에 올라갈 수 있는 미터
        long B = Long.parseLong(st.nextToken()); //밤에 자는 동안 미끄러지는 미터
        long V = Long.parseLong(st.nextToken()); // 총 나무 막대 미터

        long dayDist = A - B; 
        long goalDest = V -B; 
        
        
        if(goalDest%dayDist != 0){ 
            System.out.println(goalDest/dayDist + 1);
        }else{ 
            System.out.println(goalDest/dayDist);
        }

    }
}