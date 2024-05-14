package Day8;
interface Coin{
    int PENNY = 1, NICKEL = 5 , DIME = 10 , QUARTER = 25;
    // 사실 그냥 int만 써도 public static final로 표시되어버린다.
}
public class _10_4coin1Demo {
    public static void main(String[] args){
        System.out.println("Dime은 " + Coin.DIME + "센트입니다." );
    }
}
