package Day4;
class Circle3{
    private double radius;

    public  Circle3(double r){
        radius = r;
    } // 클래스에 다른 생성자가 하나라도 있으면 디폴트 생성자를 자동으로 추가하지 않는다.
    // 즉 Circle3 클래스에는 디폴트생성자가 없다.
}

public class _7_5circleDemo {
    public static void main(String[] args) {
        Circle3 myCircle = new Circle3(10.0);
        // Circle3 yourCircle = new Circle3();   이것은 디폴트 생성자가 없으므로 사용할 수 없다.

    }
}
