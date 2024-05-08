package Day6;

public class _8_10incrementDemo {
    public static void main(String[] args) {
        int[] x = {0};
        System.out.println("호출전의 x[0] = " + x[0] );

        increment(x);
        System.out.println("호출 후의 x[0] = " +x[0]);

    }
    public  static  void  increment(int[] n){
        System.out.print("increment() 매서드 안에서 ");
        System.out.print("n[0] = " + n[0] + " --> ");
        n[0]++;
        System.out.println("n[0] = " + n[0]);
    }
}
// 원래는 1로 안바뀌어야 정상이다. 하지만 바뀌었다.
// 왜냐하면 객체 자체를 전달했기 때문에 객체 자체가 변해서 숫자가 변한 것이다.