import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int K = Integer.parseInt(br.readLine());
		int count = 0;
		
		for(int i = 1; i <= N; i++) {
			int now = i;
			int max = 0;
			//현재 나눌 값인 i의 루트 값(Math.sqrt)이하 정수로 연산
			for(int j = 2; j <= Math.sqrt(i);) {
				//나누어떨어진면 같으 값으면 나누어떨어지지 않을때까지 연산
				if(now % j == 0) {
					now /= j;
					max = j;
				//나누어떨어지지 않으면 j +1
				}else {
					j++;
				}
			}
			//해당 반복문이 끝나면 최종 값이 1이 아니면 현재 값을 최댓값에 저장
			if(now != 1) max = now;
			//최댓값이 K보다 작거나 같으면 조건에 맞는 값이다.
			if(max <= K) count++;
		}
		System.out.println(count);
	}

}