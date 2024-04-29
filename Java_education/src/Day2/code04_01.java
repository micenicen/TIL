package Day2;

public class code04_01 {
    public static void main(String[] args){
        byte age = 127;
        short birth = 32767;
        int money = 2147483647;

        System.out.println((byte)(age+1));
        System.out.println((short)(birth+1));
        System.out.println((int)(money+1));
    }
}
// 각각의 숫자를 제공하고 오버플로우를 시켜보자.
// 한계치에 다다르면 마이너스로 변하는 상황이 생긴다.