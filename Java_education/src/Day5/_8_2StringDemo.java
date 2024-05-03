package Day5;

public class _8_2StringDemo {
    public static void main(String[] args) {
        String s1 = "Hi, Java";
        String s2 = new String("Hi, Java");
        String s3 = "Hi, Code";
        String s4 = "Hi, java";

        System.out.println(s1.equals(s2));  // 이퀄은 s2스트링 객체 내부의 값과 s1의 값이 같은지 확인해준다.
        System.out.println(s1.equals(s3));  // s3객체는 아예 스펠링이 다르다.
        System.out.println(s1.equals(s4));  // s4객체는 대소문자가 하나 다르다.
        System.out.println(s1.equalsIgnoreCase(s4)); // 대소문자를 무시하면 서로 같다.

        System.out.println(s1.compareTo(s3));// 애초에 j는 c보다 뒤에 나오는 요소이다. 사전순서대로 볼 때에는 양수가 나올 것이다.
        System.out.println(s1.compareToIgnoreCase(s4)); // j가 대문자, 소문자 여부는 무시한다면 같을 것이다.
        System.out.println(s3.compareTo(s4));           // c가 훨씬 앞에 나온다. 마이너스가 나올 것이다.
        System.out.println("Hi, Java".compareToIgnoreCase("hi, java")); // 대소문자를 무시한다면 같은 결과일 것이다.
    }
}

