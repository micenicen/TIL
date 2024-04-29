package Day3;

public class code04_15 {
    public static void main(String[] args) {

        String str = "난생처음 자바를 처음 학습 중입니다. 자바는 처음이지만 재미있네요.";

        System.out.println(str.indexOf("처음"));
        System.out.println(str.indexOf("처음"));
        System.out.println(str.indexOf("처음",4));

    }
}
// 처음을 인덱스 위치부터 찾게 설정할 수 있다.