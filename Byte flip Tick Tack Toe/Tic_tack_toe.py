class project :
    board = None
    turn = None
    @staticmethod
    def  checkWinner() :
        a = 0
        while (a < 8) :
            line = None
            if (a==0):
                line = project.board[0] + project.board[1] + project.board[2]
            elif(a==1):
                line = project.board[3] + project.board[4] + project.board[5]
            elif(a==2):
                line = project.board[6] + project.board[7] + project.board[8]
            elif(a==3):
                line = project.board[0] + project.board[3] + project.board[6]
            elif(a==4):
                line = project.board[1] + project.board[4] + project.board[7]
            elif(a==5):
                line = project.board[2] + project.board[5] + project.board[8]
            elif(a==6):
                line = project.board[0] + project.board[4] + project.board[8]
            elif(a==7):
                line = project.board[2] + project.board[4] + project.board[6]
            if (line=="XXX") :
                return "X"
            elif(line=="OOO") :
                return "O"
            a += 1
        a = 0
        while (a < 9) :
            if str(a+1) in project.board :
                break
            elif(a == 8) :
                return "draw"
            a += 1
        print(project.turn + "\'s turn; enter a slot number to place " + project.turn + " in:")
        return None
    @staticmethod
    def printBoard() :
        print("| " + project.board[0] + " | " + project.board[1] + " | " + project.board[2] + " |")
        print("| " + project.board[3] + " | " + project.board[4] + " | " + project.board[5] + " |")
        print("| " + project.board[6] + " | " + project.board[7] + " | " + project.board[8] + " |")
    @staticmethod
    def main() :
        project.board = [None]*9
        project.turn = "X"
        winner = None
        a=0
        while (a<9) :
            project.board[a]=str(a+1)
            a=a+1
        print("Welcome to 3x3 Tic Tac Toe.")
        project.printBoard()
        print("X will play first. Enter a slot number to place X in:")
        while (winner == None) :
            numInput = 0
            numInput = int(input())
            if (numInput == -1) :
                print(" SORRY game up")
                project.printBoard()
                break
            elif(project.board[numInput - 1]==str((numInput))) :
                project.board[numInput - 1] = project.turn
                if (project.turn=="X") :
                    project.turn = "O"
                else :
                    project.turn = "X"
                project.printBoard()
                winner = project.checkWinner()
            else :
                print("Slot already taken; re-enter slot number:")
        if(winner==None):
            None

        elif (winner.lower() == ("draw").lower()) :
            print("It\'s a draw! Thanks for playing.")
        else :
            print("Congratulations! " + winner + "\'s have won! Thanks for playing.")
    

if __name__=="__main__":
    project.main()