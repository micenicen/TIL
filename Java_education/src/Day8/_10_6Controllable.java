package Day8;

public interface  _10_6Controllable {
    default void repair(){
        show("장비를 수리한다.");
    }
    // 디폴트 메서드를 나타낸다.

    static void reset() {
        System.out.println("장비를 초기화한다.");
    }
    // 정적 메서드를 말한다.

    private void show(String s) {
        System.out.println(s);
    }
    // 도우미 메서드로 사용된다.

    void turnOn();
    void turnOff();
    // 둘은 추상메서드이다.
}
