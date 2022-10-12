import os
import hashlib
import sys
def file_t(path,Sz,w_file):
    ft1 = open(w_file, mode='w', encoding='utf-8')
    all_dir = os.listdir(path)
    max_file_size = []
    #轮询所有文件名
    for file in all_dir:
        if file != '$RECYCLE.BIN':
                file_path = path+file
                #判断文件
                if os.path.isfile(file_path):
                    print(file_path)
                    with open(file_path, 'rb') as fd:
                        #md5
                        md5obj = hashlib.md5()
                        md5obj.update(fd.read())
                        hashv1 = md5obj.hexdigest()
                        print(hashv1)
                        #文件大小
                        file_size = (os.path.getsize(file_path)/ (1024 * 1024)  )
                        sfile_size = str(file_size )
                        str_xx = str(hashv1)
                        #写入
                        ft1.write(file_path)
                        ft1.write("\n")
                        ft1.write("文件大小:"+sfile_size+"M")
                        ft1.write("\n")
                        ft1.write("文件哈希值:"+str_xx)
                        ft1.write("\n")
                        ft1.write("\n")
                    #比大小
                    if  file_size > Sz:
                        max_file_size.append(file_path)
        else:
            continue
    ft1.write("*************************************大于%sM的文件****************************************"%Sz)
    ft1.write("\n")
    for i in max_file_size:
        i=str(i)
        ft1.write(i)
        ft1.write("\n")
    ft1.write("*************************************大于%sM的文件****************************************"%Sz)
    ft1.close()
path = "E:\\"
w_file = 't2.txt'
#搜索大小
Sz= int(input("请输入要搜索的最小值:"))
file_t(path,Sz,w_file)
