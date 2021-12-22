using System;
using System.Linq;

namespace day_4
{
    class Board
    {
        private int width;
        private int height;
        private int[,] board;
        private int rowCount = 0;
        private bool boardWon = false;

        public Board(int width, int height)
        {
            this.width = width;
            this.height = height;
            board = new int[width, height];
        }

        public bool didBoardWin(){
            return this.boardWon;
        }

        private int[] Str2Int(string row)
        {
            string[] arr = row.Split(' ').Where(x => !string.IsNullOrWhiteSpace(x)).ToArray();
            return Array.ConvertAll(arr, int.Parse);
        }
        public void addRow(string strRow)
        {
            int[] row = Str2Int(strRow);
            for (int i = 0; i < width; i++)
            {
                this.board[rowCount, i] = row[i];
            }
            rowCount++;
        }

        public void checkNumber(int number)
        {
            for (int r = 0; r < this.width; r++)
            {
                for (int c = 0; c < this.height; c++)
                {
                    if (this.board[r, c] == number)
                    {
                        this.board[r, c] = -1; // marking drawn numbers by setting to -1
                    }
                }
            }
        }

        public bool isWinner()
        {
            /*
            * Potential improvement is skipping column if positive value seen on a row
            */
            int counter;
            for (int r = 0; r < this.width; r++)
            {
                counter = 0;
                for (int c = 0; c < this.height; c++)
                {
                    if (this.board[r, c] < 0)
                    {
                        counter++;
                    }
                    else
                    {
                        break;
                    }
                }
                if (counter == width)
                {
                    this.boardWon = true;
                    return true;
                }
            }

            for (int c = 0; c < this.height; c++)
            {
                counter = 0;
                for (int r = 0; r < this.width; r++)
                {
                    if (this.board[r, c] < 0)
                    {
                        counter++;
                    }
                    else
                    {
                        break;
                    }
                }
                if (counter == height)
                {
                    this.boardWon = true;
                    return true;
                }
            }
            return false;

        }

        public int getReward(int lastNumber)
        {
            int reward = 0;
            for (int r = 0; r < this.width; r++)
            {
                for (int c = 0; c < this.height; c++)
                {
                    if (this.board[r, c] > 0)
                    {
                        reward += this.board[r, c];
                    }
                }
            }
            return reward*lastNumber;
        }

        public void print()
        {
            for (int r = 0; r < this.width; r++)
            {
                for (int c = 0; c < this.height; c++)
                {
                    Console.Write(String.Format("{0, -4}", this.board[r, c]));
                }
                Console.WriteLine();
            }
        }
    }
}
