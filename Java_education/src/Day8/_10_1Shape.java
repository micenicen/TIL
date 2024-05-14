package Day8;

abstract class _10_1Shape {
    double pi = 3.14;       // 추상클래스도 멤버필드가 포함할 수 있다.

    abstract void draw();   // 추상 메서드는 본체가 없다.
    // 추상 메서드는 추상클래스 내에서만 만들 수 있다.
    // 얘는 상속받은애가 구현해야한다는 것을 추상메서드로 설정한다.

    public  double findArea(){
        return 0.0;
    }
}
// 추상 클래스의 가장 큰 특징은 객체생성이 안된다는 것이다.
// 추상클래스는 상속하려고 만든다.
// 추상매서드는 일반클래스에서는 만들 수 없다.

//인터페이스는 추상클래스 이상이다.
// 필드는 전부 상수다. 변수는 쓸 수 없다.
// 메서드도 전부 추상메서드이다.
// 인터페이스는 다중 상속을 이유로 사용한다. 클래스는 다중상속이 되지 않는다.
// 자바는 다중상속을 막아놨다. 그럼에도 다중상속이 필요한 상황이 있는데 이때에 인터페이스를 사용한다.