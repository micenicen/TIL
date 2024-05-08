package Day6;

public class _8_11MainArgumentDemo {
    public static void main(String[] args) {
        if (args.length == 2) {
            int i = Integer.parseInt(args[1]);
            nPrintln(args[0], i);
        } else
            System.out.println("어이쿠!");
    }
    public static void nPrintln(String s, int n){
        for (int i = 0; i < n; i++)
            System.out.println(s);
    }
}
// 오류가 나는 이유를 알아보자.