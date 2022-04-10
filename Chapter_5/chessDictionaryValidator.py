dictionary = {
    'a1' : '', 'a2' : '', 'a3' : '', 'a4' : '', 'a5' : '','a6' : '', 'a7' : '', 'a8' : '',
    'b1' : '', 'b2' : '', 'b3' : '', 'b4' : '', 'b5' : '','b6' : '', 'b7' : '', 'b8' : '',
    'c1' : '', 'c2' : '', 'c3' : '', 'c4' : '', 'c5' : '','c6' : '', 'c7' : '', 'c8' : '',
    'd1' : '', 'd2' : '', 'd3' : '', 'd4' : '', 'd5' : '','d6' : '', 'd7' : '', 'd8' : '',
    'e1' : '', 'e2' : '', 'e3' : '', 'e4' : '', 'e5' : '','e6' : '', 'e7' : '', 'a8' : '',
    'f1' : '', 'f2' : '', 'f3' : '', 'f4' : '', 'f5' : '','f6' : '', 'f7' : '', 'f8' : '',
    'g1' : '', 'g2' : '', 'g3' : '', 'g4' : '', 'g5' : '','g6' : '', 'g7' : '', 'g8' : '',
    'h1' : '', 'h2' : '', 'h3' : '', 'h4' : '', 'h5' : '','h6' : '', 'h7' : '', 'h8' : '',
}
pieces = ['pawn' , 'knight', 'bishop', 'rook', 'queen', 'king']

def countPiece(pion, lst):
    counter = 0
    for i in range(len(lst)):
        if pion in lst:
            counter += 1
    return counter

def checkDictionary(dictionaire):
    for i in range(32):
        m = input('Enter you chess move(press Enter to stop: ')
        if m == '':
            break
        else:
            k = m[:2]
            v = m[3:]
            dictionaire[k] = v
    if k not in dictionaire.keys():
        return 'Invalid board position.'
    elif v[1:] not in pieces:
        return 'Invalid piece.'
    elif countPiece('bking', dictionaire.values()) > 1 or countPiece('wking', dictionaire.values()) > 1:
        return 'Both players can only have one king piece.'
    elif countPiece('bqueen', dictionaire.values()) > 1 or countPiece('wqueen', dictionaire.values()) > 1:
        return 'Both players can only have one queen piece.'
    elif countPiece('bknight', dictionaire.values()) > 2 or countPiece('wknight', dictionaire.values()) > 2:
        return 'Both players can only have two knight pieces.'
    elif countPiece('bbishop', dictionaire.values()) > 2 or countPiece('wbishop', dictionaire.values()) > 2:
        return 'Both players can only have two bishop pieces.'
    elif countPiece('brook', dictionaire.values()) > 2 or countPiece('wrook', dictionaire.values()) > 2:
        return 'Both players can only have two rook pieces.'
    elif countPiece('bpawn', dictionaire.values()) > 8 or countPiece('wpawn', dictionaire.values()) > 8:
        return 'Both players can only have eight pawn pieces.'


print(checkDictionary(dictionary))