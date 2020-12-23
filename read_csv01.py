import csv

def search():
  with open('kimetsu.csv', mode="r") as f:
    reader = csv.reader(f)
    text = '' 
    for r in reader:
      tex = ','.join(r)
      text += tex
# if __name__=="__main__":
  a = search()
    # print(text,end=",")

  # f.close()

  word=input("鬼滅の登場人物を入力してください>>>")
  
  if word in a:
      print("{}が見つかりました".format(word))
  else:
      print("{}が見つかりませんでした".format(word))
      # text.append(word)
      # print("{}を追加しました".format(word))
