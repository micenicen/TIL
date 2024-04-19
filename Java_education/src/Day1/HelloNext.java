package Day1;

import java.util.Scanner;

public class HelloNext {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("이름은 : ");
        String s = stdIn.next();

        System.out.println("안녕하세요 " + s + "씨!");
    }
}
