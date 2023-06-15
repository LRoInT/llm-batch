def write_file(file,data):
    #写入数据
    open(file,mode="a").write(data).close()
def remove_file(file):
    #删除文件
    if os.path.exists(file):
        os.remove(file)
def create_dir(dir):
    #创建目录
    if not os.path.exists(dir):
        os.makedirs(dir)
def delete_dir(dir):
    #删除目录
    if os.path.exists(dir):
        shutil.rmtree(dir)
def list_dir(dir):
    #列出目录中的文件和子目录
    return [os.path.join(dir,i) for i in os.listdir(dir)]