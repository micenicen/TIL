package Day3;

public class code04_13 {
    public static void main(String[] args) {

        String str = "    한글    ABCD    efgh    ";
        String cutStr;

        cutStr = str.trim();

        System.out.println("기존 문자열  ==> [" + str + "]");
        System.out.println("공백 제거  ==> [" + cutStr + "]");

    }
}
// 좌우의 공백을 제거하는 용도로 사용된다.