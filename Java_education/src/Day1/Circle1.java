package Day1;

import java.util.Scanner;

public class Circle1 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("반지름 : ");
        double r = stdIn.nextDouble();

        System.out.println("원주의 길이는 " + 2 * 3.14 * r +"입니다.");
        System.out.println("면적은 " + 3.14 * r * r +"입니다.");
    }
}
