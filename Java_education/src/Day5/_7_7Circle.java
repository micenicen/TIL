package Day5;

class Circle {
    double radius;
    String color;

    public Circle(double radius, String color){
        this.radius = radius;
        this.color = color;
    }

    public  Circle(double radius){
        this(radius,"파랑");
    }
    public Circle(String color){
        this(10.0, color);
    }
    public Circle(){
        this(10.0,"빨강");
    }
}
public class _7_7Circle {
}
// 이러한 식으로 함수를 짤 수 있다. 디폴트를 설정하는 것이다.