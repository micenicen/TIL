package Day7;

public class _9_3InheritanceDemo {
    public static void main(String[] args) {
        _9_1Circle c1 = new _9_1Circle();
        _9_2Ball c2 = new _9_2Ball("빨간색");

        System.out.println("원 :");
        c1.findRadius();
        c1.findArea();

        System.out.println("\n공 : ");
        c2.findRadius();
        c2.findColor();
        c2.findArea();
        c2.findVolume();
    }
}
//같은 위치에서 불러와서 적용된 모습이다.