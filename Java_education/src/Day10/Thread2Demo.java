package Day10;

public class Thread2Demo {
    public static void main(String[] args){
        new Thread(new MyRunnable(){
            public void run() {
                for (int i = 0; i < 5; i++) {
                    System.out.print("잘가. ");
                    try {
                        Thread.sleep(500);
                    } catch (InterruptedException e) {
                    }
                }
            }
        }).start();

    }

}