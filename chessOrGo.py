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
        if self.board.isPositionBelongToPlayer(self,x,y,color):
            return 1
        else:
            print("temp to moving piece not own to you")
            return 0
    def checkTargetPositionNotHavePiece(self,x,y):
        if self.board.isPositionHavePiece(afterX, afterY):
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
                

        

        
#action是一个界面类 应该避免跟实体类的交互        
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
    """
    def _parsePosition(self,positionString):
        x,y = map(lambda x:int(x),positionString.split(","))
        return x,y
    def step(self,roundNum):#接收命令行输入并进行解析
        cmdInput = input("What Operation:") 
        self.actionHistory.append(cmdInput)
        parseInput = cmdInput.split()
        actionType = parseInput[0]
        if actionType=='move':
            beforeP = parseInput[1]
            afterP = parseInput[2]
            beforeX,beforeY = self._parsePosition(beforeP)
            afterX,afterY = self._parsePosition(afterP)
            error = self.actionControl.moving(beforeX,beforeY,afterX,afterY,self.color)
            return error # -1:error 0:next player 1:this player


# In[8]:


class Position(object):
    """docstring for Position"""
    def __init__(self, x,y):
        super(Position, self).__init__()
        self.x = x
        self.y = y


# In[ ]:


class Piece(object):
    """docstring for Piece"""
    # "position"
    # "valid" if the Piece is in the 
    def __init__(self, position,name,color):
        super(Piece, self).__init__()
        self.position = position
        self.name = name
        self.color =-1


# In[15]:


#记录从位置到棋子的映射
class Board(object):
    """docstring for Board"""
    def __init__(self,gridLength):
        super(Board, self).__init__()
        self.position2piece={}
        for i in range(gridLength):
            for j in range(gridLength):
                self.position2piece[(i,j)]=-1
        self.gridLength = gridLength
    def getGridLength(self):
        return self.gridLength
    def isValidPosition(self,x,y):
        if x<self.getGridLength() and y<self.getGridLength():
            return 1
        return 0
    def isPositionHavePiece(self,x,y):
        if self.position2piece[(x,y)]==-1:
            return 0
        return 1
    def isPositionBelongToPlayer(self,x,y,color):
        assert isPositionHavePiece(x,y)==1
        if self.position2piece[(x,y)].color == color:
            return 1
        return 0
    def addPiece(self,x,y,piece):
        self.position2piece[(x,y)] = piece
    def deletePiece(self,x,y):
        piece = self.position2piece[(x,y)]
        self.position2piece[(x,y)] = -1
        return piece
    def initGoBoard(self):
        return 
    def initChessBoard(self):
        return




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
        gameType=input("input game type,chess or go")
        self.gridLength = 20

        self.board = Board(self.gridLength)
        if gameType == "chess":
            self.board.initChessBoard()
        if gameType == "go":
            self.board.initGoBoard()

        player1Name=input("input the name of player1")
        player2Name=input("input the name of player2")
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
                if flag == 0: #用户此次进行的是查询操作，
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

# In[3]:

if __name__ == "__main__":
    newGame = Game()
    newGame.run()
