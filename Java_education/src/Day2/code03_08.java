package Day2;

public class code03_08 {
    public static void main(String[] args) {
        int num;
        num = 100;
        num = num + 200;
        System.out.println(num);
    }
}
// 대입하기 전에 오른쪽에 있는 식을 전부 계산한 다음 이동하는 것을 볼 수 있다.
// 또는 파이썬에서 그랬듯이 num +=200으로도 표현 가능하다.
// 복합연산자는 파이썬과 비슷하다. +=는 더하기, -=는 빼기, *=는 곱하기, /=는 나누기(물론 실수냐 정수냐에 따라 차이가 존재), %=는 나머지다.
// 자바스크립트처럼 증감연산자가 존재한다. ++num과 num++, --num같이 증감이 가능하다. 이건 변수의 한칸씩 증감한다.