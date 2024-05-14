package Day8;

public class _10_3AbstractClassDemo {
    public static void main(String[] args) {
        // Shape s = new Shape();

        _10_2Circle c = new _10_2Circle(3);
        c.draw();
        System.out.printf("원의 넓이는 %.1f\n", c.findArea());
    }
}
