class list_file():

    def __init__(self, list_data,filename):
        self.list_data = list_data
        self.filename = filename

    def file2list(self):
        with open(self.filename, 'r') as f1:
            list1 = f1.readlines()
            
        print( '数据记录有%s'%(len(list1)))

    def list2file(self):
        f = open(self.filename, 'w')  # 若是'wb'就表示写二进制文件

        for str in self.list_data:
            f.write(str)
            f.write('\n');
        f.close()


#把字符串list写入文件 一个一行
list_test=["1", "2", "3"]
myobj = list_file(list_test, "text.log")
myobj.list2file()

#读取文件到list中
list_data_read = []
myread = list_file(list_test, "text.log")
myread.file2list()
print(myread.list_data)

