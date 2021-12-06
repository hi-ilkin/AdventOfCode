using System;
using System.Collections.Generic;
using System.Linq;

namespace day_4
{
    class Program
    {

        private static List<Board> createBoardsFromStrings(string[] lines, string board_seperator)
        {
            List<Board> boards = new List<Board>();
            Board board = new Board(5, 5);

            for (int i = 2; i < lines.Length; i++)
            {
                string line = lines[i];
                if (line == board_seperator)
                {
                    boards.Add(board);
                    board = new Board(5, 5);
                }
                else
                {
                    board.addRow(line);
                }
            }
            boards.Add(board);

            return boards;
        }


        static void solve_part_1(List<Board> boards, int[] drawnNumbers)
        {
            foreach (int n in drawnNumbers)
            {
                List<int> winnerBoardIds = new List<int>();
                Console.Write($"{n}, ");
                for (int i = 0; i < boards.Count; i++)
                {
                    Board b = boards[i];
                    b.checkNumber(n);
                    if (b.isWinner() == true)
                    {
                        Console.WriteLine();
                        b.print();
                        int reward = b.getReward(n);
                        Console.WriteLine($"Reward of board {i}: {reward}");
                        return;
                    }
                }
            }
        }

        static void solve_part_2(List<Board> boards, int[] drawnNumbers)
        {
            bool isGameOver = false;
            foreach (int n in drawnNumbers)
            {
                Console.Write($"{n}, ");
                List<int> winnerBoardIds = new List<int>();

                for (int i = 0; i < boards.Count; i++)
                {
                    Board b = boards[i];
                    b.checkNumber(n);
                    if (b.isWinner() == true)
                    {
                        winnerBoardIds.Add(i);
                        if (boards.Count == 1)
                        {
                            Console.WriteLine();
                            b.print();
                            int reward = b.getReward(n);
                            Console.WriteLine($"Reward of board {i}: {reward}");
                            isGameOver = true;
                            break;
                        }
                    }
                }
                if (isGameOver == true)
                {
                    break;
                }
                for (int idx = winnerBoardIds.Count - 1; idx >= 0; idx--)
                {
                    boards.RemoveAt(winnerBoardIds[idx]);
                }
            }
        }

        static void Main(string[] args)
        {

            if (args.Length != 2)
            {
                Console.WriteLine("Program past have two inputs: part number and input file. Example: dotnet run 1 input.txt");
                return;
            }

            string part = args[0];
            string input_path = args[1];

            string[] lines = System.IO.File.ReadAllLines(input_path);
            int[] drawnNumbers = Array.ConvertAll(lines[0].Split(','), int.Parse);

            List<Board> boards = createBoardsFromStrings(lines, "");

            Console.WriteLine($"Number of Numbers: {drawnNumbers.Length}");
            Console.WriteLine($"Number of Boards: {boards.Count}");

            switch (part)
            {
                case "1":
                    solve_part_1(boards, drawnNumbers);
                    break;
                case "2":
                    solve_part_2(boards, drawnNumbers);
                    break;
                default:
                    Console.WriteLine($"Invalid part : {part} was choosen. Please choose either 1 or 2.");
                    break;
            }
        }
    }
}