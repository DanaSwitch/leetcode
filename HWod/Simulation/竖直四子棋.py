import sys

# 检查从(r,c)这个位置落子后，是否形成四连
def check(board, r, c, color, H, W):
    # 四个方向：横、竖、两条斜线
    dirs = [(0,1),(1,0),(1,1),(1,-1)]
    for dr,dc in dirs:
        # 每个方向进来时, cnt都会重新置1
        cnt = 1   # 当前落子本身算一个
        # 向正方向统计连续棋子
        nr,nc = r+dr,c+dc
        while 0<=nr<H and 0<=nc<W and board[nr][nc]==color:
            cnt+=1
            nr+=dr
            nc+=dc
        
        # 向反方向统计连续棋子
        nr,nc = r-dr,c-dc
        while 0<=nr<H and 0<=nc<W and board[nr][nc]==color:
            cnt+=1
            nr-=dr
            nc-=dc
        
        # 如果某个方向连续>=4，说明赢了
        if cnt>=4:
            return True
    
    return False


def solve():
    W,H = map(int,sys.stdin.readline().split())  # 读取棋盘宽和高
    steps = list(map(int,sys.stdin.readline().split()))  # 读取所有落子步骤 
    board = [[0]*W for _ in range(H)]  # 初始化棋盘，0表示空
     
    for i,col in enumerate(steps):  # 依次模拟每一步落子    
        step = i+1   # 当前是第几步
        
        # 非法情况1：列号超出范围
        if col<1 or col>W:
            print(f"{step},error")
            return
        
        col = col - 1   # 转换为数组下标
        row = -1  # 行(高度)
        
        # 从底往上找第一个空位（模拟重力）
        for r in range(H-1,-1,-1):
            if board[r][col]==0:
                row=r
                break
        
        # 非法情况2：该列已经满了
        if row==-1:
            print(f"{step},error")
            return
        
        # 判断当前落子颜色
        # 奇数步 红方
        # 偶数步 蓝方
        color = 1 if step%2==1 else 2  # 1:红, 2:蓝
        # 放入棋子
        board[row][col]=color
        # 检查是否四连
        if check(board,row,col,color,H,W):  
            if color==1:
                print(f"{step},red")
            else:
                print(f"{step},blue")
            return
    
    # 如果所有步骤结束都没人赢
    print("0,draw")


if __name__=="__main__":
    solve()