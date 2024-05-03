package Day5;

public class _8_1StringDemo {
    public static void main(String[] args) {
        String s1 = "Hi, Java";
        String s2 = "Hi, Java";
        String s3 = new String("Hi, Java");
        String s4 = new String("Hi, Java");

        System.out.println("s1 == s2 -> " + (s1 == s2)); // 문자열의 객체 자체는 동일하다 그렇기에 True가 나올 것이다.
        System.out.println("s1 == s2 -> " + (s1 == s3)); // 객체로 싸여져있는 s3은 s1과 같지 않다.
        System.out.println("s1 == s2 -> " + (s3 == s4)); // 컴퓨터 입장에서는 s3과 s4의 주소가 다르기에 같지 않다고 판단한다.

        s1 = s3;
        System.out.println("s1 == s3 -> " + (s1 == s3)); // s3과 s1의 주소가 같다. 그렇기에 같다고 판단한다.
        // 여기서 s1은 참조변수가 없기에 가비지컬렉터로 이동하게 된다.
    }
}
