package Day7;

class Circle {
    double radius;

    public  Circle(double radius){
        this.radius = radius;
    }
    public double getRadius() {
        return  radius;
    }

    double findArea(){
        return 3.14 * radius * radius;
    }
}


public class _8_13CircleArrayDemo {
    public static void main(String[] args) {
        Circle[] circles = new Circle[5];                       // 여기서 객체를 가진 배열변수를 선언하였다.

        for (int i  = 0; i < circles.length; i++) {             //객체 배열 크기가 i보다 작을때 작동한다.
            circles[i] = new Circle(i + 1.0);
            System.out.printf("원의 넓이(반지름 : %.1f) = %.2f\n",
                    circles[i].radius, circles[i].findArea());
        }
    }
}