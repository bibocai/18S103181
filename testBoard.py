import unittest
from chessOrGo import ChessBoard
#指定顺序
class CheckChessBoard(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        super(CheckChessBoard,self).__init__(*args,**kwargs)
        self.board = ChessBoard()#棋子已经按照国际象棋规则摆放好
    def test_getGridLenghth(self):
        self.assertEqual(8,self.board.getGridLength())
    def test_isPositionHavePiece(self):
        self.assertEqual(1, self.board.isPositionHavePiece(1,1))
        self.assertEqual(0, self.board.isPositionHavePiece(1,3))
    def test_isPositionBelongToPlayer(self):
        self.assertEqual(1, self.board.isPositionBelongToPlayer(0,0,0))
        self.assertEqual(0, self.board.isPositionBelongToPlayer(0,0,1))
    #def test_addPiece(self):
    #    self.assertEqual(1, self.board.addPiece())
    #    self.assertEqual(0, self.board.addPiece())
    #def test_deletePiece(self):
    #    self.assertEqual(1, self.board.deletePiece())
    #    self.assertEqual(0, self.board.deletePiece())
    def test_countPlayerPieceNum(self):
        self.assertEqual((16,16), self.board.countPlayerPieceNum())
    def test_isValidPosition(self):
        self.assertEqual(1, self.board.isValidPosition(7,7))
        self.assertEqual(0, self.board.isValidPosition(8,8))
  

unittest.main()
