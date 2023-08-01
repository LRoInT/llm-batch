from sys import exit
def connect(q,e,b,s): #模型连接脚本事例
    def script():
        print("Start Running")
        while True:
            if e.wait():
                task=q.get()
                if task[:5]=="task:":
                    response="model return"
                    q.put(response)
                    b.set()
                elif task=="!exit":
                    b.set()
                    exit()
                else:
                  b.set()
                e.clear()
    return script