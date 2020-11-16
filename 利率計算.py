"""
程式名稱: 利率計算
作者: Lexaul
日期: 16/11/2020

"""

# 使用者輸入本金、年利率、日月計息、總額
balance = input('請輸入本金: ')
annualrate = input('請輸入年利率(%): ')
cycle = input('請輸入計算週期: ')
mode = input('日計息請輸入d/月計息請輸入m:')

# 將輸入資料轉成浮點數
try:
    balance = float(balance)
    annualrate = float(annualrate)
    cycle = float(cycle)
except:
    print('輸入有誤, 請輸入數值資料!')
    exit()

# 檢查輸入資料是否大於0
if balance<=0 or cycle<=0:
    print('輸入有誤, 請輸入大於0的數值資料!')
    exit()

# 檢查日月計息參數
if mode!='d' and mode!='m':
    print('日月計息輸入錯誤，請輸入m或d')
    exit()

# 計算總額
if mode == 'd' :
    total = balance * (1+(annualrate*0.01/365))**cycle
if mode == 'm' :
    total = balance * (1+(annualrate*0.01/12))**cycle

# 總額取小數4位, 四捨五入
total = round(total, 4)

# 印出total
print('total=', total)