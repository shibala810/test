data = []

count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line.strip())
        count +=1
        if count % 1000 ==0:
            print(count)
print('檔案讀取完畢，共有',len(data),'筆資料')
