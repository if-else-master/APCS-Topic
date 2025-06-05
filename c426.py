num = int(input())
str_a = input()
list_str = list(str_a)

def ch(list_str, num, temp=None, cut=None, k=0, ans=None):
    if ans is None:
        ans = []
    if cut is None:
        cut = []
    if k + num > len(list_str):
        return cut
    
    # 取得當前窗口的字符
    current_window = list_str[k:k+num]
    
    if ''.join(current_window).islower():  # 修正語法錯誤：加上冒號
        word = "lower"
        if temp != word:
            cut.append(k + num)
            return ch(list_str, num, word, cut, k + num, ans)
        else:
            return ch(list_str, num, word, cut, k + num, ans)
    else:
        word = "upper"
        if temp != word:
            cut.append(k + num)
            return ch(list_str, num, word, cut, k + num, ans)
        else:
            return ch(list_str, num, word, cut, k + num, ans)

max_length = 0
for i in range(len(list_str)):
    result = ch(list_str, num, None, None, i, None)
    if result:
        # 計算從起始位置到最後一個切點的長度
        length = result[-1] - i
        max_length = max(max_length, length)

print(max_length)
