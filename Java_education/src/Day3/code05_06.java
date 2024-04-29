package Day3;

import java.util.Scanner;

public class code05_06 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int num;
        System.out.print("숫자입력 ==> ");
        num = s.nextInt();

        if (num > 100){
            if (num < 1000) {
                System.out.println("100보다 크고 1000보다 작습니다.");
            } else {
                System.out.println("1000보다 큽니다.");
            }
        }else{
            System.out.println("100보다 작습니다. ");
        }

    s.close();

    }
}
// 중첩 if문은 위와 깉이 중괄호 파티로 작성한다.

