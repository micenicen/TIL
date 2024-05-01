package Day4;

class Circle2{
    double radius;                                          // 디폴드는 0.0이다. 대부분의 요소는 0이나 null등이 디폴트이다.

    double findArea(){
        return  3.14 * radius * radius;
    }
    void show(double x, double y){
        System.out.printf("반지름 = %.1f, 넓이 = %.1f\n", x,y);
    }
}

public class _7_3circleDemo {
    public static void main(String[] args) {
        Circle2 myCircle = new Circle2();
        myCircle.radius = 10.0;
        myCircle.show(myCircle.radius,myCircle.findArea());
    }
}