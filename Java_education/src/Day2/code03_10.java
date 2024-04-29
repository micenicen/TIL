package Day2;
import java.util.Scanner;
public class code03_10 {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int score;

        System.out.print("필기시험 점수를 입력하세요: ");
        score = s.nextInt();
        System.out.println(score >=70);

        s.close();
    }
}
// 사실 s.close는 가비지컬렉터가 있어서 쓸 필요는 없다.