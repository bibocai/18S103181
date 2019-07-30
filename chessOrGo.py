#!/usr/bin/env python
# coding: utf-8

"""
actionType:moving
"""
class ActionControl(object):
    def __init__(self,board):
        super(ActionControl, self).__init__()
        self.board = board

    def checkPositionNotOutOfBoard(self,X,Y):
        if self.board.isValidPosition(X,Y):
            return 1
        else:
            print("not Valid Position,failure")
            return 0

    def checkPositionIsBelongToPlayer(self,x,y,color):
        if self.board.isPositionBelongToPlayer(x,y,color):
            return 1
        else:
            print("temp to moving piece not own to you")
            return 0
    def checkPositionIsNotBelongToPlayer(self,x,y,color):
        if self.board.isPositionBelongToPlayer(x,y,color):
            print("the piece in the place is yours")
            return 0
        else:
            return 1 
        
    def checkTargetPositionNotHavePiece(self,x,y):
        if self.board.isPositionHavePiece(x, y):
            print("target Postion already have piece,failure")
            return 0
        else:
            return 1
    def checkOriginPositionHavePiece(self,x,y):
        if self.board.isPositionHavePiece(x,y):
            return 1
        else:
            print("origin Position not have piece")
            return 0
    def checkOriginPosNotEqualTargetPlace(self,beforeX, beforeY,afterX,afterY):
        if beforeY!=afterY or beforeX!=afterX:
            return 1
        else:
            print("origin place equal to target place")
            return 0 
    def moving(self,beforeX,beforeY,afterX,afterY,color):
        if  ( self.checkPositionNotOutOfBoard(beforeX,beforeY) and  
           self.checkPositionNotOutOfBoard(afterX,afterY)   and  
           self.checkOriginPositionHavePiece(beforeX, beforeY) and  
           self.checkTargetPositionNotHavePiece(afterX,afterY) and            
           self.checkPositionIsBelongToPlayer(beforeY,beforeY,color) and 
           self.checkOriginPosNotEqualTargetPlace(beforeX,beforeY,afterX,afterY) ):
           
            piece = self.board.deletePiece(beforeX,beforeY)
            
            self.board.addPiece(afterX,afterY,piece)
            
            return 1
        else:
            return 0      
    #def put
    def checkIfSelectPieceBelongToPlayer(self,playerColor,pieceColor):
        if playerColor==pieceColor:
            return 1
        else:
           if playerColor==0:
               print("even num of piece belong to you")
           else:
               print("odd num of piece belong to you")
           return 0
    def checkPieceNotOnBoard(self,piece):
        if(piece.onBoard):
            print("select piece already on board")
            return 0
        else:
            return 1
    def putting(self,targetX,targetY,playerColor,pieceIndex):
        piece = self.board.piecePool[pieceIndex]
        if ( 
            self.checkIfSelectPieceBelongToPlayer(playerColor,piece.color) and 
            self.checkPieceNotOnBoard(piece)  and
            self.checkPositionNotOutOfBoard(targetX,targetY) and 
            self.checkTargetPositionNotHavePiece(targetX,targetY) ):

             self.board.addPiece(targetX,targetY,piece)
             return 1
        else:
            return 0
    #提子
    def taking(self,targetX,targetY,playerColor):
        if ( 
              self.checkPositionNotOutOfBoard(targetX,targetY) and
              self.checkPositionIsNotBelongToPlayer(targetX,targetY,playerColor) and               
             self.checkOriginPositionHavePiece(targetX,targetY) ):

            self.board.deletePiece(targetX,targetY)
            #提子后仍是该用户的turn
            return 1
        else:
            print("taking failure") 
            return 0

    def eating(self,originX,originY,targetX,targetY,playerColor):
        error = self.taking( targetX,targetY,playerColor)
        if error == 0:
            return 0
        else:
            error = self.moving( originX,originY,targetX,targetY,playerColor)
            return error
        
#action是一个界面类 应该避免跟实体类的交互        
    def querying(self,X,Y):
        if self.checkPositionNotOutOfBoard(X,Y):
            piece = self.board[(X,Y)] 
            if piece ==-1: 
                print("no piece in the place")
            else:
                color = piece.color
                print("the piece color is ",color)
    def calculating(self):
        x,y=self.board.countPlayerPieceNum()
        print("white ",x)
        print("black ",y)
class Action(object):
    """docstring for Action"""
    def __init__(self,color,actionControl):
        super(Action, self).__init__()
        self.color = color # 黑棋/白棋
        self.beforeX = -1
        self.afterX = -1
        self.beforeY = -1
        self.afterY = -1
        self.actionHistory = []
        self.actionControl = actionControl
        
    """
    接收命令行输入并进行解析
    cmdInput: actionType:move -1,-1 -2,-2
    put -1,-1 3
    eat -1,1, -2,-2
    """
    def _parsePosition(self,positionString):
        x,y = map(lambda x:int(x),positionString.split(","))
        return x,y
    def step(self,roundNum):#接收命令行输入并进行解析
        if self.color==0:
            print("white ",end="")
        else:
            print("black ",end="")
        cmdInput = input("Operation>") 
        error = -2
        self.actionHistory.append(cmdInput)
        parseInput = cmdInput.split()
        actionType = parseInput[0]
        if actionType=='move':
            beforeP = parseInput[1]
            afterP = parseInput[2]
            beforeX,beforeY = self._parsePosition(beforeP)
            afterX,afterY = self._parsePosition(afterP)
            error = self.actionControl.moving(beforeX,beforeY,afterX,afterY,self.color)
        if actionType =='put':
            targetP = parseInput[1]
            pieceIndex = int(parseInput[2])
            targetX,targetY = self._parsePosition(targetP)
            error = self.actionControl.putting(targetX,targetY,self.color,pieceIndex)
        if actionType == 'eat':
            beforeP = parseInput[1]
            afterP = parseInput[2]
            beforeX,beforeY = self._parsePosition(beforeP)
            afterX,afterY = self._parsePosition(afterP)
            error = self.actionControl.eating(beforeX,beforeY,afterX,afterY,self.color)
        if actionType == 'take':
            targetP = parseInput[1]
            targetX,targetY = self._parsePosition(targetP)
            self.actionControl.taking(targetX,targetY,self.color)
            error = 0
        if actionType == 'query':
            targetP = parseInput[1]
            targetX,targetY = self._parsePosition(targetP)
            self.actionControl.querying(targetX,targetY) 
            error =0
        if actionType == 'calculate':
            self.actionControl.calculating()
            error =  0
        if actionType == 'pass':
            error = 1
        if actionType == 'end':
            error= -1
# In[8]:
        if error !=1:
            self.actionHistory.pop()
        if error == -2:
            
            print("wrong input")
            return 0 
        return error


class Position(object):
    """docstring for Position"""
    def __init__(self, x,y):
        super(Position, self).__init__()
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    def getY(self):
        return self.y

class Piece(object):
    """docstring for Piece"""
    # "position"
    # "valid" if the Piece is in the 
    def __init__(self,color):
        super(Piece, self).__init__()
        self.color =color
        self.onBoard=0

class ChessPiece(Piece):
    def __init__(self,name,color):
        super(ChessPiece,self).__init__(color)
        self.name = name

class GoPiece(Piece):
    def __init__(self,color):
        super(GoPiece,self).__init__(color)
        

# In[15]:


#记录从位置到棋子的映射
class Board(object):
    """docstring for Board"""
    def __init__(self,gridLength):

        super(Board, self).__init__()
        self.piecePool=[]
        self.position2piece={}
        for i in range(gridLength):
            for j in range(gridLength):
                self.position2piece[(i,j)]=-1
        self.gridLength = gridLength

    def getGridLength(self):
        return self.gridLength
       
    def isPositionHavePiece(self,x,y):
        if self.position2piece[(x,y)]==-1:
            return 0
        return 1
    def isPositionBelongToPlayer(self,x,y,color):
        assert self.isPositionHavePiece(x,y)==1
        if self.position2piece[(x,y)].color == color:
            return 1
        return 0
   
    def addPiece(self,x,y,piece):
        self.position2piece[(x,y)] = piece
        piece.onBoard=1

    def deletePiece(self,x,y):
        piece = self.position2piece[(x,y)]
        self.position2piece[(x,y)] = -1
        piece.onBoard=0
        return piece
    def countPlayerPieceNum(self):
        count0 =0
        count1 =0
        for value in self.position2piece.values():
            if value != -1:
                if value.color ==0:
                    count0+=1
                elif value.color ==1:
                   count1+=1
        return count0,count1

    def isValidPosition(self,x,y):
        pass 
class GoBoard(Board):
    def __init__(self):
        super(GoBoard,self).__init__(18)
        for i in range(180):
            self.piecePool.append(GoPiece(0))# white is even
            self.piecePool.append(GoPiece(1))# black is odd
    def isValidPosition(self,x,y):
        if x<=self.getGridLength() and y<=self.getGridLength() and  x>=0 and y>=0:
            return 1
        return 0
                
class ChessBoard(Board):
    def __init__(self):
        super(ChessBoard,self).__init__(8)
        # 将国际象棋的棋子放在棋盘上
        pieceName = ["rook","rook","knight","knight","bishop","bishop","king","queen"]
        whitePiecePosition=[(0,0),(7,0),(1,0),(6,0),(2,0),(5,0),(4,0),(3,0)]
        blackPiecePosition=[(0,7),(7,7),(1,7),(6,7),(2,7),(5,7),(4,7),(3,7)]
        for name,position in zip(pieceName,whitePiecePosition):
            self.addPieceFromMeta(*position,name,0)
        for name,position in zip(pieceName,blackPiecePosition):
            self.addPieceFromMeta(*position,name,1)
        #pawn
        for i in range(8):
            self.addPieceFromMeta(i,1,"pawn",0)
            self.addPieceFromMeta(i,6,"pawn",1)
        num1,num2=self.countPlayerPieceNum() 
        print("init finish,the num is ",num1," ",num2)
# just used for add piece
    def addPieceFromMeta(self,x,y,name,color):
        piece=ChessPiece(name,color)
        self.piecePool.append(piece)
        self.addPiece(x,y,piece)

    def isValidPosition(self,x,y):
        if x<self.getGridLength() and y<self.getGridLength() and x>=0 and y>=0:
            return 1
        return 0
 
        
class Player(object):
    """docstring for Player"""
    def __init__(self, name,color):
        super(Player, self).__init__()
        self.name =name 
        self.color = color


class Game(object):
    """docstring for Game"""
    def __init__(self):
        super(Game, self).__init__()
        gameType=input("input game type,chess or go ")
        self.gridLength = 20

        if gameType == "chess":
            self.board=ChessBoard()
        elif gameType == "go":
            self.board=GoBoard()
        
        player1Name=input("input the name of player1 ")
        player2Name=input("input the name of player2 ")
        self.player1 = Player(player1Name,0)
        self.player2 = Player(player2Name,1)
        self.actionCtl = ActionControl(self.board)

        self.player1Act = Action(0,self.actionCtl)
        self.player2Act = Action(1,self.actionCtl)
        
    def run(self):
        roundNum =0
        while(1):
            while(True):
                flag = self.player1Act.step(roundNum)
                if flag == -1: #用户要求终止
                    return
                if flag == 1:
                    break # 用户的本轮操作完成
                if flag == 0: #用户此次进行的是查询操作或操作无效，重新操作
                    print("still player1's turn")
            while(True):
                flag =self.player2Act.step(roundNum)
                if flag == -1: #用户要求终止
                    return
                if flag == 1:
                    break # 用户的本轮操作完成
                if flag == 0:
                    print("still player2's turn")
            roundNum+=1
    def printRecord(self):
        play1His = self.player1Act.actionHistory
        play2His = self.player2Act.actionHistory
        print("history of player1")
        print(play1His)
        print("history of player2")
        print(play2His)

# In[3]:

if __name__ == "__main__":
    newGame = Game()
    newGame.run()
    newGame.printRecord() 
