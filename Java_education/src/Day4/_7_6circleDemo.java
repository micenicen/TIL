package Day4;
class Circle4{

    double radius;
    String color;

    public Circle4(double r, String c){
    radius = r;
    color = c;
    } //임의의 반지름과 색상을 가진 객체 생성자이다.


    public Circle4(double r) {
        radius = r;
        color = "파랑";
    }// 파랑 객체 생성자이다.

    public Circle4(String c){
        radius = 10.0;
        color = c;
    } // 반지름이 10.0인 객체 생성자이다.

    public Circle4() {
        radius = 10.0;
        color = "빨강";
    } // 반지름 10인 빨강 객체를 생성한다.
}

public class _7_6circleDemo {
    public static void main(String[] args) {
        Circle4 c1 = new Circle4(10.0, "빨강");

        Circle4 c2 = new Circle4(5.0);

        Circle4 c3 = new Circle4( "노랑");

        Circle4 c4 = new Circle4();
    }
}
// 각각은 다른 값을 호출할 것이다. 입력값에 디폴트를 설정하면 r과 c가 무엇이 입력되어도 전부 대응할 수 있다.
// 오버로딩은 다시 공부해보자.