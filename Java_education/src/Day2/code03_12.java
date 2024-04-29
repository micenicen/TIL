package Day2;

public class code03_12 {
    public static void main(String[] args){
        int num = 99;
        System.out.println((num > 100) && (num < 200));
        System.out.println((num == 99) || (num ==100));
        System.out.println(!(num == 100));

    }
}
// 신기한 점은 True거나 False인 것이 미리 계산되어서 회색글자로 표시가 되었다. 만약 위치를 바꾸면 차이가 보일 것이다.