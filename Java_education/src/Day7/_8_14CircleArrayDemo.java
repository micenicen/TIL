package Day7;

public class _8_14CircleArrayDemo {
    public static void main(String[] args) {
        Circle c1 = new Circle(10.0);
        Circle c2 = new Circle(10.0);

        zero(c1);
        System.out.println("원(c1)의 반지름 : "+ c1.radius);

        zero(c2.radius);
        System.out.println("원(c2)의 반지름 : "+ c2.radius);
    }
    public static void zero(Circle c) {
        c.radius= 0.0;
    }
    public static void zero(double r){
        r = 0.0;
    }
}

// c2는 c.radius와 r은 별개이므로 10.0이 나왔으며 c1은 double r이 적용되여 0으로 할당되었다.