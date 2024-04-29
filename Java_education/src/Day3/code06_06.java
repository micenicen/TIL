package Day3;

public class code06_06 {
    public static void main(String[] args) {
        int hap = 0;
        for (int i=1 ; i<=10 ; i++) {
            hap += i;
        }
        System.out.println("1부터 10까지의 합계 : " + hap);
    }
}
// hap을 초기화 시키는 작업이 없으면 오류가 뜰 것이다.
// 초기화를 시키면 정상적으로 작동할 것이다.
// 이와같이 1000개를 더할 수도 있고 1000부터 2000까지 더하는 것도 가능해진다.
// 그래서 7번항목과 8번항목은 건너뛴다.