package Day8;

class _10_2Circle extends _10_1Shape {
    int radius;

    public _10_2Circle(int radius){
        this.radius = radius;
    }

    public void draw(){
        System.out.println("원을 그리다.");
    }
    // 부모클래스에서 추상매서드로 선언했던 것은 자식클래스에서 반드시 구현해야 한다.

    public double findArea() {
        return pi*radius*radius;
    }
    // 이 부분은 부모클래스의 매서드를 오버라이딩 했다.
}
