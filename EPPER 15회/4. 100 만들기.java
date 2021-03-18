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
	 
	 if ( b+1 == a ){
		 for ( int i = a+1 ; i < 8 ; i++ ){
			 answer[i-2] = numbers[i];
		 }
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
