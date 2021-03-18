//프로그래머스에서는 main함수 및 입출력문이 필요하지 않습니다. 대신 solution함수만 작성하면 됩니다.
import java.util.Scanner;

 public class Main {
 public static int[] solution(int[] numbers) {
	 int[] answer = new int[7];
	 int sum = 0;
	 int a=0;
	 int b=0;
	 
	 for (int i = 0 ; i<9 ; i++)
		 sum += numbers[i];
	 
	 for ( int i = 0; i < 9; i++ ){
		 for ( int j = 0; j < 9; j++ ){
			 if ( sum-(numbers[i]+numbers[j]) == 100 ){
				 a = i;
				 b = j;
			 }
		 }
	 }
	 
	 for ( int i = 0 ; i < b ; i++ )
		 answer[i] = numbers[i];
	 
	 if ( a+1 == 8 )
		 answer[6] = numbers[8];
	 
	 else if ( b+1 == a ){
		 for ( int i = a+1 ; i < 8 ; i++ ){
			 answer[i-2] = numbers[i];
		 }
		 if ( answer[6] == 0 )
			 answer[6] = numbers[8];
	 }
	 
	 
	 else {
		 int bb = b;
		 for ( int i = b+1; i < a-1 ; i++ ){
			 answer[bb] = numbers[i];
			 bb++;
		 }
		 if ( a == 8 )
			 answer[6] = numbers[7];
	 }
		 
 
	 return answer;
 }
	
	public static void main(String [] args){
		int [] numbers=new int[9];
		int r[];
		Scanner input= new Scanner(System.in);
		
		for (int i = 0; i < 9; i++) {
			numbers[i]=input.nextInt();
		}
	
	r = solution(numbers);
	for (int i = 0; i < 7; i++) {
		System.out.printf("%d ", r[i]);
	}
		
		
	}
}
