package Day3;

import java.util.Scanner;

public class code05_08 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int score;
        System.out.print("점수입력 ==> ");
        score = s.nextInt();

        if (score >= 90)
            System.out.print(("A"));
        else if(score >=80)
            System.out.print("B");
        else if(score >= 70)
            System.out.print("C");
        else if(score >=60)
            System.out.print("D");
        else
            System.out.print(("F"));
        System.out.println("학점입니다.");
        s.close();

    }
}
// 사실 아까코드에서 백 스페이스를 3번 써서 else if문을 사용해도 잘 작동한다.
