package Day5;

class Person {
    String name;
    int age;

    public Person setName(String name){
        this.name = name;
        return this;
    }
    public Person setAge(int age){
        this.age = age;
        return this;
    }
    public void sayHello(){
        System.out.println("안녕, 나는 " + name + "이고 " + age + "살이야.");
    }
}
public class _7_8MethodChainDemo {
    public static void main(String[] args) {
        Person person = new Person();
        person.setName("민국").setAge(21).sayHello();
    }
}
// 마지막은 연속호출을 통해서 부른 예시이다.
