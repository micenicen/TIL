package Day3;
import java.util.Scanner;

public class code05_07 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int score;
        System.out.print("점수입력 ==> ");
        score = s.nextInt();

        if (score >= 90)
            System.out.print(("A"));
        else
            if(score >=80)
                System.out.print("B");
            else
                if(score >= 70)
                    System.out.print("C");
                else
                    if(score >=60)
                        System.out.print("D");
                    else
                        System.out.print(("F"));
        System.out.println("학점입니다.");
        s.close();

    }
}
// 아무리 생각해도 이 행동은 컴퓨터에게 죄를 짓는 행동이라는 것이 명확하게 보인다.