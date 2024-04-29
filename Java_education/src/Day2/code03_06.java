package Day2;

public class code03_06 {
    public static void main(String[] args) {
        double num;
        num = Math.pow(3,2);
        System.out.println(num);
        num = Math.pow(4,3);
        System.out.println(num);

    }
}
// 제곱을 하기 위해서는 double을 사용하는데 리턴이 실수형이기 때문이다. int를 쓰면 바로 애러난다.
// 제곱은 좀 불편한데 Math.pow를 써야 제곱을 할 수 있다.
// Math.에 무엇을 붙이냐에 따라 다른 결과가 나온다.
// abs는 절댓값, log는 로그, max는 최댓값, min은 최솟값이다.
// sin, cos, tan을 붙여서 삼각함수를 계산할 수 있다.

