import csv

f = open("kimetsu.csv","r")
reader = csv.reader(f)
for row in reader:
    for col in row:
        print(col,end=",")

f.close()

def search():
  word=input("鬼滅の登場人物を入力してください>>>")
  # for word in source:
  if word in reader:
      print("{}が見つかりました".format(word))
  else:
      print("{}が見つかりませんでした".format(word))
      reader.append(word)
      print("{}を追加しました".format(word))

if __name__=="__main__":
  search()