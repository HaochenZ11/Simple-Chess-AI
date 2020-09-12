class chessBoard:
    def __init__(self):
        self.board = [13,11,12,15,14,12,11,13,10,10,10,10,10,10,10,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,20,20,20,20,20,20,23,21,22,25,24,22,21,23]
  
    def getBoard(self):
        return self.board
    
    def printBoard(self):
        cnt=7
        end=64
        p=[]
        test=[]
        for k in range(0,8,1):
            p=[cnt]
            for i in reversed (range(end-8,end,1)):       
                if self.board[i]==0:
                    p=p+["_ "]
                elif self.board[i]==10:
                    p=p+["WP"]
                elif self.board[i]==11:
                    p=p+["WN"]
                elif self.board[i]==12:
                    p=p+["WB"]
                elif self.board[i]==13:
                    p=p+["WR"]
                elif self.board[i]==14:
                    p=p+["WQ"]
                elif self.board[i]==15:
                    p=p+["WK"]
                elif self.board[i]==20:
                    p=p+["BP"]
                elif self.board[i]==21:
                    p=p+["BN"]
                elif self.board[i]==22:
                    p=p+["BB"]
                elif self.board[i]==23:
                    p=p+["BR"]
                elif self.board[i]==24:
                    p=p+["BQ"] 
                else:
                    p=p+["BK"]
                test=test+[self.board[i]]
            cnt=cnt-1
            end=end-8
            for j in range(9):
                print(p[j], end = " ")
                #print(test[j], end = " ")
            print("")
        print("")   
        
    def move(self, current, new):
        temp=self.board[current]
        self.board[new]=temp
        self.board[current]=0

class Queue:
    def __init__(self):
        self.list=[]
        self.length=len(self.list)

    def enqueue(self, data):
        self.list=self.list+[data]
        self.length=self.length+1

    def dequeue(self):
        if self.list == []:
            return [False]
        else:
            val=self.list[0]
            self.list=self.list[1:]
            self.length=self.length-1
            return [True, val]

    def empty(self):
        if (self.list==[]):
            return True
        else:
            return False
        
class Stack:
    def __init__(self):
        self.list=[]
        self.length=len(self.list)
    
    def push(self, dataElement):
        self.list =self.list + [dataElement]
        self.length=self.length+1
    
    def pop(self):
        val=self.list[self.length-1]
        self.list=self.list[0:self.length-1]
        self.length=self.length-1
        return val
    
    def empty(self):
        if(self.list==[]):
            return True
        else:
            return False
        
class tree:
    def __init__(self,x):
        self.store = [x,[]]

    def AddSuccessor(self,x):
        if type(x)==type(self):
            self.store[1] = self.store[1] + [x]
        else:
            self.store[1] = self.store[1]+ [tree(x)]
        return True

    def Print_DepthFirst(self):
        pstack=Stack()
        pstack.push(self)
        while(pstack.empty()==False):
            #print("in loop")
            r=pstack.pop()
            try:
                print(r.store[0])
                #print("loop")
                for i in reversed(r.store[1]):
                    pstack.push(i)
            except AttributeError:
                print(r)
        return True
    
    def Get_LevelOrder(self):
        x=Queue()
        x.enqueue(self)
        l=[]
        while x.empty()==False:
            r=x.dequeue()
            l=l+[r[1].store[0]]
            for i in r[1].store[1]:
                x.enqueue(i)
        return l

