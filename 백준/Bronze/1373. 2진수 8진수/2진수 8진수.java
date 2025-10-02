import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = br.readLine();
        StringBuilder sb = new StringBuilder();

        if(input.length()%3!=0)
            for(int i=0;i<input.length()%3;i++)
                input = "0" + input;
        for(int i=0;i<input.length();i+=3){
            sb.append( Character.getNumericValue(input.charAt(i+2)) + 
            Character.getNumericValue(input.charAt(i+1)) * 2
                    +Character.getNumericValue(input.charAt(i)) * 4);
        }
        bw.write(sb.toString());	//8진수 BufferedWriter 저장
        bw.flush();		//결과 출력
        bw.close();
        br.close();
    }
}