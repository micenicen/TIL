package Day1;

import java.util.Scanner;

public class HelloNextLine {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("이름은 : ");
        String s = stdIn.nextLine();                   //띄어쓰기가 될 것이다. 공백문자를 포함할 수 있다.

        System.out.println("안녕하세요 " + s + "씨!");
    }
}
