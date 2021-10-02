import java.util.Scanner;

public class Main{
	public static int solution(int n, int m){
		//이 아래 필요한 변수 및 필요한 코드를 작성하세요
		int answer=0;
		while(n!=0){
			n--;
			answer++;
			if (answer%m == 0) //처음 0일째를 제외해야하니까 뒤에 넣는다
				n++;
			
			
		}
		
		
		return answer;
	}


   public static void main(String[] args) {
      Scanner scanner=new Scanner(System.in);
      int n=scanner.nextInt();
      int m= scanner.nextInt();
      int answer=solution(n,m);
		 
      System.out.println(answer);
   }

}
