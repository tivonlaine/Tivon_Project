/*
Name: Tivon Laine, 2002167255, 1004 & 1006, Assignment 2
Description: Solving the eight queens problem
Input: Row and coloumn of board
Output: Board with eight queens not able to attack each other
*/
#include <iostream>
using namespace std;

const int rows = 8;
const int coloumns = 8;
char letter = 'Q';
char dash = '-';

bool validmove(int i, int j, char arr[rows][coloumns], char letter);
bool putqueen(char arr[rows][coloumns], int row, int first);

bool validmove(int i, int j, char arr[rows][coloumns], char letter)
{

    for (int x = 0; x < 8; x++)//checking row
    {
        if (arr[i][x] == letter)
        {
            return false;
        }
    }
    for (int y = 0; y < 8; y++)//checking coloumn
    {
        if (arr[y][j] == letter)
        {
            return false;
        }
    }

    for (int x = j, y = i; x < rows && y < coloumns; x++, y++)   //checking lower right diagonal
    {
        if (arr[y][x] == letter)
        {
            return false;
        }
    }
    for (int x = j, y = i; x < rows && y >= 0; x++, y--)//checking upper right diagonal
    {
        if (arr[y][x] == letter)
        {
            return false;
        }
    }
    for (int x = j, y = i; x >= 0 && y >= 0; x--, y--)//checking upper left diagonal
    {
        if (arr[y][x] == letter)
        {
            return false;
        }
    }
    for (int x = j, y = i; x >= 0 && y < coloumns; x--, y++)//checking lower left diagonal
    {
        if (arr[y][x] == letter)
        {
            return false;
        }
    }
    return true;
}



bool putqueen(char arr[rows][coloumns], int row,int first)
{
    if (row >= rows)       //if it's passed the last row
    {
        return true;
    }
    if(row==first){     //if it's on the initial queen's row
       return putqueen(arr, row+1, first);  //then skip
    }

    for (int i = 0; i < coloumns; i++)
    {
        if (validmove(row, i, arr, 'Q'))    //if a queen can be placed safely
        {
            arr[row][i] = 'Q';
            if (putqueen(arr, row + 1, first))
            {
                return true;
            }
            arr[row][i] = '-';
        }
    }
    return false;
}

int main()
{

    char board[rows][coloumns];
    int first = 0;
    int second = 0;

    for (int i = 0; i < rows; i++)              //initializing board
    {
        for (int j = 0; j < coloumns; j++)
        {
            board[i][j] = '-';
        }
    }

    while (first > rows || first < 1 || second < 1 || second > rows)
    {
        cout << "Enter initial coordinates of the first queen: ";
        cin >> first >> second;
    }
    cout<<first<<" "<<second<<endl;
    cout<<endl;
    first--;        //decrementing for indexes
    second--;
    board[first][second] = 'Q';

    if (putqueen(board, 0, first))
    {
        cout << "   1 2 3 4 5 6 7 8" << endl;
        for (int i = 0; i < rows; i++)
        {
            cout << i + 1 << "  ";
            for (int j = 0; j < coloumns; j++)
            {   if(board[i][j]=='Q'){
                cout<<"Q ";
            }else{
                cout << board[i][j] << " ";

            }
            }

            cout << endl;
        }
    }else{
        cout<<"No solution found";
    }


}
