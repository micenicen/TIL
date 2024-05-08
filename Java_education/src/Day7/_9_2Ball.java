package Day7;

public class _9_2Ball extends _9_1Circle{
    private String color;

    public _9_2Ball(String color) {
        this.color = color;
    }

    public void findColor() {
        System.out.println(color + " 공이다.");
    }

    public void findVolume() {
        System.out.println("부피는 4/3*(ㅠ*반지름*반지름*반지름)이다. ");
    }

}
