package Day6;

public class _8_6StringDemo {
    public static void main(String[] args) {
        String version = String.format("%s %d ","JDK",14);
        System.out.println(version);
        // 문자열과 정수를 포멧 명시자에 맞춰 문자열을 배치한 것이다.

        String fruits = String.join(", ","apple","banana","cherry","durian");
        System.out.println((fruits));
        // 마지막 인수의 문자열을 첫번째 인수인 따옴포료 연결한 문자열을 반환했다.

        String pi = String.valueOf(3.14);
        System.out.println(pi);
        // 실수를 문자열로 반환하였다.
    }
}