from chessOrGo import ActionControl,Piece,GoBoard
import unittest
class CheckActionCtl(unittest.TestCase):

    def __init__(self,*args,**kwargs):
            super(CheckActionCtl,self).__init__(*args,**kwargs)
            self.board = GoBoard()
            self.board.addPiece(1,1,self.board.piecePool[0])#在1，1位置处摆放一颗白棋
            self.board.addPiece(2,2,self.board.piecePool[1])#在2，2位置处摆放一颗黑棋
            self.actionCtl = ActionControl(self.board)
            
    def test_checkPositionNotOutOfBoard(self):
        self.assertEqual(1,self.actionCtl.checkPositionNotOutOfBoard(18,18))
        self.assertEqual(0,self.actionCtl.checkPositionNotOutOfBoard(19,18))
        self.assertEqual(0,self.actionCtl.checkPositionNotOutOfBoard(1,19))
        self.assertEqual(0,self.actionCtl.checkPositionNotOutOfBoard(-1,19))
        self.assertEqual(1,self.actionCtl.checkPositionNotOutOfBoard(0,1))


    
    def test_checkPositionIsBelongToPlayer(self):
        self.assertEqual(1,self.actionCtl.checkPositionIsBelongToPlayer(1,1,0))
        self.assertEqual(0,self.actionCtl.checkPositionIsBelongToPlayer(1,1,1))
    
    def test_checkPositionIsNotBelongToPlayer(self):
        self.assertEqual(1,self.actionCtl.checkPositionIsNotBelongToPlayer(1,1,1))
        self.assertEqual(0,self.actionCtl.checkPositionIsNotBelongToPlayer(1,1,0))
    
    def test_checkTargetPositionNotHavePiece(self):
        self.assertEqual(0,self.actionCtl.checkTargetPositionNotHavePiece(2,2))
        self.assertEqual(1,self.actionCtl.checkTargetPositionNotHavePiece(0,1))
    
    def test_checkOriginPositionHavePiece(self):
        self.assertEqual(1,self.actionCtl.checkOriginPositionHavePiece(1,1))
        self.assertEqual(0,self.actionCtl.checkOriginPositionHavePiece(0,3))
    
    def test_checkOriginPosNotEqualTargetPlace(self):
        self.assertEqual(1,self.actionCtl.checkOriginPosNotEqualTargetPlace(1,2,1,3))
        self.assertEqual(0,self.actionCtl.checkOriginPosNotEqualTargetPlace(1,2,1,2))
    
    def test_checkIfSelectPieceBelongToPlayer(self):
        self.assertEqual(1,self.actionCtl.checkIfSelectPieceBelongToPlayer(1,1))
        self.assertEqual(0,self.actionCtl.checkIfSelectPieceBelongToPlayer(1,0))
    
    def test_checkPieceNotOnBoard(self):
        self.assertEqual(0,self.actionCtl.checkPieceNotOnBoard(self.board.piecePool[0]))
        self.assertEqual(1,self.actionCtl.checkPieceNotOnBoard(self.board.piecePool[2]))

    #def test_moving(self):    
    #def test_putting(self):
    #def test_taking(self):
    #def test_eating(self):
    #def test_calculating(self):

unittest.main()

