package Day9;

class Mouse{
    String name;

    public  Mouse(String name){
        this.name = name;
    }
}

class Keyboard{
    String name;

    public Keyboard(String name){
        this.name = name;
    }

    public  boolean equals(Object obj){
        if (obj instanceof Keyboard) {
            Keyboard k= (Keyboard) obj;
            if (name.equals(k.name))
                return true;
        }
        return false;
    }
    public String toString() {
        return "키보드입니다.";
    }
}

// 패키지는 파이썬에서 배웠던 Import의 개념으로 보면 된다.
// 패키지는 상호 관련이 있는 클래스와 인텊이스를 한 곳에 묶어놓은 것들이다.
// 모듈은 밀접한 관계가 있는 패키지와 리소스를 묶어놓은 것이다.
// 자바에서 외부 유틸, 랭귀지, 텍스트등을 불러서 import하고 처리하는 것으로 우리가 그동안에 썼던 Scanner도 여기에 해당된다.
// 다음과 같은 패키지가 존재한다.
// java.awt : 그래픽, java.io : 입출력, java.lang : 필수요소, java.math : 수학
// java.net : 네트워크, java.text : 문자열, java.time : 시간, java.util 유틸리티, javax.swing : 스윙 컴포넌트