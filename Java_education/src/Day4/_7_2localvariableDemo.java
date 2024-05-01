package Day4;

public class _7_2localvariableDemo {
    public static void main(String[] args) {
        int a = 0;
        double b;

        //System.out.print(b);   초기화가 안되어있기에 사용할 수 없을 것이다.
        //System.out.print(a+c); c변수는 선언되지 않았기에 사용될 수 없을 것이다.
        int c = 0;

        //public double d = 0.0; 지역변수는 public으로 지정할 수 없다.

        for (int e =0; e < 10; e++){
            //int a = 1          이미 5행에서 선언된 적이 있다. 블록이 다를지라도 같은 이름으로 선언이 불가하다.
            System.out.print(e);
        }
    }
}