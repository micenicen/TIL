package Day8;

public class _10_9ControllableDemo {
    public static void main(String[] args){
        _10_8TV tv = new _10_8TV();
        tv.turnOn();
        tv.turnOff();
        tv.repair();
        _10_6Controllable.reset();
    }
}
// 이와같이 인터페이스를 불러서 운영이 가능하다.