using System;
using System.Collections.Generic;
using System.Linq;

namespace day_4
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines("input.txt");
            int[] drawnNumbers = Array.ConvertAll(lines[0].Split(','), int.Parse);

            List<Board> boards = new List<Board>();
            Board board = new Board(5, 5);

            for (int i = 2; i < lines.Length; i++)
            {
                string line = lines[i];
                if (line == "")
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


            Console.WriteLine($"Number of Numbers: {drawnNumbers.Length}");
            Console.WriteLine($"Number of Boards: {boards.Count}");
            bool isGameOver = false;
            foreach (int n in drawnNumbers)
            {
                Console.Write($"{n}, ");
                for(int i=0; i < boards.Count; i++)
                {
                    Board b = boards[i];
                    b.checkNumber(n);
                    if (b.isWinner() == true)
                    {
                        Console.WriteLine();
                        b.print();
                        int reward = b.getReward(n);
                        Console.WriteLine($"Reward of board {i}: {reward}");
                        isGameOver = true;
                        break;
                    }
                }
                if (isGameOver == true)
                {
                    break;
                }
            }
        }
    }
}