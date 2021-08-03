

class Wage():
    def init(self,P,Q,R,S,W):
        self.P = P
        self.Q = Q
        self.R = R
        self.S = S
        self.W = W
    def A(self,W,P):
        wage = W * P
        return wage
    def B(self, W,Q, R ,S):
        if W <= R :
            wage = Q 
        else:
            wage = Q + (W-R)*S
        return wage
    
a = int(input())
for i in range(a):
    P = int(input())
    Q = int(input())
    R = int(input())
    S = int(input())
    W = int(input())
    x = (P,Q,R,S,W)
