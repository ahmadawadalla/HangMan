import java.util.*;
public class SlotMachine {
   public static void main(String[] args) {
      Random rand = new Random();
      Scanner kb = new Scanner(System.in);
      menu();
      System.out.print("How much money do you have ($5 / spin): ");
      while (!kb.hasNextDouble()) {
         System.out.print("How much money do you have ($5 / spin): ");
         kb.nextLine();
      }
      double money = kb.nextDouble(); // how much money you have
      double start = money; // how much you started with
      double oldMoney; // how much money you have right after you spend $5 on the spin
      int count = 0; // counts how many spins you did
      boolean again = lever(kb, money); // checks if the user wants to play again
      while (again) {
         count++;
         System.out.println("Spin # " + count);
         money -= 5;
         oldMoney = money;
         double machine = machine(money, rand);
         if (oldMoney < machine) {
            System.out.println("JACKPOT!!!");
            System.out.print("Balance: " + machine + "  + $" + (machine - oldMoney));
         } else {
            System.out.println("You Lost :(");
            System.out.print("Balance: " + machine + "  - $5");
         }
         System.out.println();
         money = machine;
         again = lever(kb, money);
      }
      System.out.println("Start Balance: $" + start);
      System.out.print("End Balance: $" + money);
      if(money > start)
         System.out.print("  + $" + (money - start));
      else if(start > money)
         System.out.print("  - $" + (start - money));
   }
   // This method gets the Slot Machine numbers, and checks to see if they are winning numbers.
   public static double machine(double money, Random random) {
      int rand = random.nextInt(900) + 100;
      System.out.println("You rolled " + rand);
      if (rand == 999)
         money += 999;
      else if (rand == 888)
         money += 888;
      else if (rand == 777)
         money += 777;
      else if (rand == 666)
         money += 666;
      else if (rand == 555)
         money += 555;
      else if (rand == 444)
         money += 444;
      else if (rand == 333)
         money += 333;
      else if (rand == 222)
         money += 222;
      else if (rand == 111)
         money += 111;
      else {
         if ((rand / 100) == (rand / 10) % 10)
            money += 50;
         if ((rand / 10) % 10 == (rand % 10))
            money += 50;
         if ((rand / 100) == rand % 10)
            money += 10;
      }
      return money;
   }
   // This method asks the user if they want to keep playing.
   public static boolean lever(Scanner kb, double money) {
      boolean again;
      System.out.println();
      System.out.print("Do you want to spin (you have " + (int)(money / 5) + " spins left) (Y/N)? ");
      String ask = kb.next();
      System.out.println();
      if (ask.equalsIgnoreCase("Y")) {
         again = true;
         if (money < 5) {
            again = false;
            System.out.println("You lost all of your money due to gambling!!!");
         }
      } else {
         again = false;
      }
      return again;
   }
   // This method shows the Prizes the user can win
   public static void menu(){
      System.out.println("99.99% of gamblers stop gambling before they hit BIG!!!");
      System.out.println("If you roll: ");
      System.out.println("3 consecutive numbers, you win whatever number that is.");
      System.out.println("2 consecutive numbers, you win $50.");
      System.out.println("A number that is repeated, but not consecutive, you win $10.");
      System.out.println();
   }
}
