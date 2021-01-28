import csv

def search() :
    f = open("kimetsu2.csv","w")

    writer = csv.writer(f,lineterminator="\n")
    writer.writerow(["ねづこ","たんじろう","きょうじゅうろう","ぎゆう","げんや","かなお","ぜんいつ"])
    
    f.close()

    result = []
    f = open("kimetsu2.csv","r")
    reader = csv.reader(f)
    for row in reader:
        for col in row:
            result.append(col)

    f.close()

    word=input("鬼滅の登場人物を入力してください>>>")

    if word in result :
        print("{}が見つかりました".format(word))
    else:
        print("{}が見つかりませんでした".format(word))
      # text.append(word)
        print("{}を追加しました".format(word))

search()
