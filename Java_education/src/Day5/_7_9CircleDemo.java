package Day5;

class Circle2 {
    double radius;
    static int numOfCircles = 0;
    int numCircles = 0;

    public Circle2(double radius) {
        this.radius = radius;
        numOfCircles++;
        numCircles++;
    }
}

public class _7_9CircleDemo {
    public static void main(String[] args) {
        Circle2 myCircle = new Circle2(10.0);
        Circle2 yourCircle = new Circle2(5.0);

        //print();  여기서 main()은 정적 메서드이므로 인스턴스 메서드를 호출할 수 없다.
        System.out.println("원의 개수 : " + Circle2.numOfCircles);
        System.out.println("원의 개수 : " + yourCircle.numCircles );
    }
    void print(){
        System.out.println("인스턴스 매서드입니다.");
    }
}
