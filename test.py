from PIL import Image, ImageDraw, ImageFont


def getCharList(file_path):
    """
    """
    f = open(file_path, 'r')
    charList = []
    for line in f.readlines():
        word = line.strip('\r\n')
        word = word.decode('utf-8')
        charList.append(word)
    f.close()
    return charList

def drawFont(charList, num):
    """
    """
    #build a new picture
    width = 80
    height = 80
    pic = Image.new('RGB', (width, height), 'white')
    curtain = ImageDraw.Draw(pic)
    #get a font
    if num == 1:
        fnt = ImageFont.truetype('./XIARIXIANGQI.TTF', 48)
    elif num == 2:
        fnt = ImageFont.truetype('./STKAITI.TTF', 48)
    idx = 1
    for char in charList:
        curtain.text((0,0), char, font=fnt, fill='black')
        pic.save("./Font"+str(num)+"/"+"font"+str(num)+"-No."+str(idx)+".png")
        pic = Image.new('RGB', (width, height), 'white')
        curtain = ImageDraw.Draw(pic)
        idx += 1



l = getCharList("./your_file_name.txt")
drawFont(l, 1)
drawFont(l, 2)
