package Day9;
import java.util.StringTokenizer;

public class UnChecked1Demo {
    public static void main(String[] args) {
        String s = "Time is money";
        StringTokenizer st = new StringTokenizer(s);

        while (st.hasMoreTokens()){
            System.out.print(st.nextToken() + "+");
        }
        System.out.print(st.nextToken());
    }
}
// 실행예외를 일부러 발생시킨 케이스이다. 예외는 어디에서 끝났는지 이야기하며 예외지점이 어디인지를 보여준다.
// 또한 예외처리를 하지 않으면 작동하지 않기도 한다.
// 예외처리방법은 try ~ catch를 사용하여 예외를 실시간으로 잡아서 처리하거나 예외를 떠넘기기를 이용하여 기본 예외처리기로 넘기는
// 방법등이 선호된다. throws절을 이용하여 예외를 다른 캐치로 넘길 수 있다. 예외마다 일일히 작성하면 코드칸 낭비이다.

// 우리는 배열을 사용하면서 어느 배열요소든 집어넣을 수 있다. 그리고 그것을 실행하는데 지장이 없는 기묘한 상황이 생긴다.
// 이는 배열은 처음에 받을 자료형을 정하지 않고 추후 자료형을 건네는 쪽에 자료형을 지정해서 보내라고 하기 때문이다.
// 제네릭 타입은 하나의 코드를 다양한 타입의 객체에 재사용하는 객체지향 기법이다. 클래스, 인터페이스, 메서드를 정의할때
// 타입을 변수로 사용한다. 자식 객체를 부모타입변수에 대입하는 것은 ㅈ네릭도 예외가 아니다.
// 이 부분은 추후 인터넷 강의로 복습이 필요하다.

