package Day7;

public class _9_1Circle {
    private void secret(){
        System.out.println("클래스 내부에서만 접근을 허용한다.");
    }

    protected void findRadius(){
        System.out.println("부모와 자식 클래스만 접근을 허용한다. ");
    }

    public  void findArea(){
        System.out.println("전역변수와 비슷하다. 전체에서 사용 가능하다. ");
    }
}
