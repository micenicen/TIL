package Day8;

public class _10_8TV implements _10_6Controllable{

    @Override
    public  void turnOn(){
        System.out.println("TV를 켠다.");
    }
    @Override
    public void turnOff(){
        System.out.println("TV를 끈다.");
    }
}
