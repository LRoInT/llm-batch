import sys
import json
import commands
from threading import Thread,Event
from call import *
import sys
import queue
response=""
conf=json.load(open("conf.json","r"))
default=conf["default"]
modelname=default
model=conf["model"][default]
argv=sys.argv[1:]
versions="""
LLM BATCH V0.0.1
"""
help="""选项：
-h, --help 显示帮助
-v --versions 显示版本
-u --use 指定运行模型
-r --run 运行单个任务
-s --setting 设置修改程序
"""
###############
print(versions)
###############
if conf["model"]=={"None":[]}:
    print("没有可调用的模型，请检查你的配置。\nNo model can use,please check your configuration.\n")
if argv==[]:
    print("Use %s" % modelname)
if "-h" in argv or "--help" in argv:
    print(help)
if "-v" in argv or "--versions" in argv:
    print(versions)
if "-u" in argv or "--use" in argv:
    modelname=argv[argv.index("-u")+1]
    model=conf["model"][modelname]
    print("Use %s" % modelname)
if "-r" in argv or "--run" in argv:
    task=argv[argv.index("-r")+1]
if "-s" in argv or "--setting" in argv:
    pass
###############
if model["type"]=="api":
    exec(open(model["path"],"r").read())
    q_model=queue.Queue()
    e_model=Event()
    e_back=Event()
    api_run=connect(q_model,e_model,e_back)
    bot=Thread(target=api_run)
    bot.start()
    while True:
        bat=input("You:")
        if bat=="!exit":
            sys.exit()
        else:
            bat="task:"+bat
            e_back.clear()
            q_model.put(bat)
            e_model.set()
            if e_back.wait():
                response=q_model.get()
                print(response)
            