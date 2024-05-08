package Day7;

public class _8_12VarArgsDemo {
    public static void main(String[] args) {
        printSum(1,2,3,4,5);
        printSum(10,20,30);
    }
    public  static void printSum(int... v){
        int sum = 0;
        for (int i : v) // 변수에 주어진 모든 인수를 차례대로 정수 i로 대입해 본체를 실행한다.
            sum += i;
        System.out.println(sum);
    }
}
// ...은 가변 개수 데이터 타입을 나타낸다. 즉 여러개의 개수가 들어갈 때에 사용한다.