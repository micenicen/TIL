package Day3;

import java.util.Scanner;

public class code06_14 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int hap = 0;
        int num1, num2;

        while (true){
            System.out.print("숫자1 ==> ");
            num1 = s.nextInt();
            if (num1 == 0)
                break;
            System.out.print("숫자2 ==> ");
            num2 = s.nextInt();

            hap = num1 +num2;
            System.out.println(num1 + " + " + num2 + " = " + hap);
        }
        System.out.println("종료코드");
        s.close();
    }
}
// 숫자가 0으로 입력되면 나가는 코드이다.
// 그 외에는 무한하게 작동하는 덧셈기계가 만들어졌다.
