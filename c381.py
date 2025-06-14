while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    # 讀取索引位置（先讀取以節省記憶體）
    text_lines = []
    for i in range(a):
        text_lines.append(input().strip())
    
    indices = list(map(int, input().split()))
    
    # 將所有文字合併成一個字串（而非列表）
    text = ''.join(text_lines)
    del text_lines  # 釋放記憶體
    
    # 建立結果
    result = []
    for k in range(b):
        idx = indices[k] - 1  # 轉換為 0-based 索引
        if 0 <= idx < len(text):
            result.append(text[idx])
    
    print(''.join(result))
