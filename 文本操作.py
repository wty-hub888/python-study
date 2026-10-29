#读文件
#1 打开文件
file = open("resources/望庐山瀑布.txt","r",encoding="utf-8")


#2 读取
content = file.read()
print(content)

#3 关闭
file.close()

