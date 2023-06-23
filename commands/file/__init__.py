import os
def wr_file(file,data):
    #写入数据
    open(file,mode="a").write(data).close()
def rm_file(file):
    #删除文件
    if os.path.exists(file):
        os.remove(file)
def re_file(file):
    #读文件
    if os.path.exists(file):
        return open(file,'r').read()
def mk_dir(dir):
    #创建目录
    if not os.path.exists(dir):
        os.makedirs(dir)
def rm_dir(dir):
    #删除目录
    if os.path.exists(dir):
        shutil.rmtree(dir)
def ls_dir(dir):
    #列出目录中的文件和子目录
    lsfile=""
    for i in os.listdir(dir):
        lsfile+=i+"\n"
    return lsfile