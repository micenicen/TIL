package Day7;

public class _9_5ball extends _9_1Circle {
    private String color;

    public _9_5ball(String color){
        this.color = color;
    }

    public  void findColor(){
        System.out.println(color + " 공이다. ");
    }

    public void findArea(){
        findRadius();

        super.findArea();
        //super.secret();  부모클래스의 private는 호출할 수 없다.

        System.out.println("넓이는 4*(ㅠ*반지름*반지름)이다.");
    }
    public  void findVolume(){
        System.out.println(("부피는 4/3*(ㅠ*반지름*반지름*반지름)이다."));
    }
}
