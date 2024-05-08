package Day6;
import java.util.Scanner;

public class _8_7ArrayDemo {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int scores[] = new int[5];
        int sum = 0;

         for (int i = 0; i < scores.length; i++)
             scores[i] = in.nextInt();

         for (int i =0; i < scores.length; i++)
             sum += scores[i];

         System.out.println("평균 = " + sum / 5.0);
    }
}
// 다음은 키보드로 5개의 정수를 입력받아 배열 원소를 초기화하고 배열 원소의 5개의 정숫값을 합한 후 평균값을 구하는 예제이다.
//