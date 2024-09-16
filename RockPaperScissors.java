import java.util.*;

public class RockPaperScissors {
    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        Random rand = new Random();
        user(kb,rand);
    }
    public static void user(Scanner kb, Random rand){
        String again = "";
        int rounds = 0;
        double won = 0;
        do {
            boolean userRock = false;
            boolean userPaper = false;
            boolean userScissors = false;

            int choice = rand.nextInt(3);
            boolean rock = false;
            boolean paper = false;
            boolean scissors = false;

            System.out.println("Choose an option: ");
            System.out.print("(R)ock, (P)aper, or (S)cissors: ");
            String user = kb.nextLine();

            switch (user.toUpperCase()) {
                case "R":
                    userRock = true;
                    break;
                case "P":
                    userPaper = true;
                    break;
                case "S":
                    userScissors = true;
                    break;
            }
            if (choice == 0) {
                rock = true;
                System.out.println("They got rock");
            } else if (choice == 1) {
                paper = true;
                System.out.println("They got paper");
            } else if (choice == 2) {
                scissors = true;
                System.out.println("They got scissors");
            }
            if ((rock && userScissors) || (paper && userRock) || (scissors && userPaper))
                System.out.println("You Lost!");
            else if ((userRock && scissors) || (userPaper && rock) || (userScissors && paper)) {
                System.out.println("You Won!");
                won++;
            }
            else
                System.out.println("Draw");
            rounds++;
            System.out.print("Do you want to play again (y/n): ");
            again = kb.nextLine();
        }while(again.equals("y"));
        System.out.println();
        System.out.println("Total rounds: " + rounds);
        System.out.println("Total wins: " + (int)won);
        System.out.println("Average wins/round: " + won/rounds);
    }
}
