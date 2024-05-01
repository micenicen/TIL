package Day4;

import java.util.Scanner;

class  Phone {
    String model;
    int value;
    void  print() {
        System.out.println(value + "만원짜리" + model + "스마트폰");
    }
}
public class _7_1PhoneDemo {
    public static void main(String[] args) {
        Phone myPhone = new Phone(); //Phone 타입의 객체를 생성한 이후 myPhone이라는 참조 변수에 대입한다.
        myPhone.model = "갤럭시 S8";  // 객체의 필드에 값을 대입한다.
        myPhone.value = 100;
        myPhone.print();             // 객체의 매서드를 호출한다.

        Phone yourPhone = new Phone();
        yourPhone.model = "G6";
        yourPhone.value = 85;
        yourPhone.print();
    }
}
// 여기서는 두 개의 객체가 생성되었다.
// 객체의 필드(model,value)는 메모리에 적재된다. 그러나 매서드(print)는 메모리에 적재되지 않는다.