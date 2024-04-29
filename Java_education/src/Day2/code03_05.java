package Day2;

public class code03_05 {
    public static void main(String[] args) {
        int a = 3, b = 4, c = 5;
        System.out.println(a * b + c);
        System.out.println(c + a * b);
    }
}
// 곱하기가 먼저 계산되기 때문에 우선순위에 따라 계산되었다. 17로 값이 동일하다.