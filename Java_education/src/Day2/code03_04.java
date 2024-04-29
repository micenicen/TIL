package Day2;

public class code03_04 {
    public static void main(String[] args) {
        double a = 2, b = 4, c = 6;
        System.out.println(a / b * c);
        System.out.println(a * c / b);
        System.out.println(c / b * a);
    }
}
// 여기서 3으로 전부 일치한다. 재밌는 점은 int가 아니라 double이다.
// int로 기재하면 0, 3, 12가 각각 나올 것이다.  double인 지금은 3.0, 3.0, 3.0으로 나올 것이다.
// 정수인지, 실수인지에 따라 결과가 아예 다르다.
