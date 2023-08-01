import sys
import json
from threading import Thread,Event
from call import *
import sys
import os
import queue
import argparse

response=""
conf=json.load(open("conf.json","r",encoding="utf-8"))
default=conf["default"]
modelname=default
argv=sys.argv[1:]
if not os.path.exists(conf["workspace"]):
    os.makedirs(conf["workspace"])
os.chdir(conf["workspace"])
cmdlist=conf["commands"]
versions="""
LLM BATCH V0.0.1(dev)
"""
help="""选项：
-h 显示帮助
-v 显示版本
-u 指定运行模型
-r 运行单个任务
-s 设置修改程序
"""
###############
def runret(modret):
    runlist=[]
    run_set=[]
    pattern = r'\[!(.+?)\]'
    matches = re.findall(pattern, modret)
    for match in matches:
        runlist.append(match)
    runlist_real=runlist.copy()
    for c in runlist_real:
        c1=c
        for n in cmdlist[0]:
            if n in c:
                c=c.replace(n,cmdlist[1][cmdlist[0].index(n)][1][1])
                run_set.append(cmdlist[1][cmdlist[0].index(n)][1][2])
        runlist_real[runlist.index(c1)]=c
    print(runlist,runlist_real)
    for r in range(len(runlist)):
        if run_set[r]=="allon":
            print(f"RUN {runlist_real[r]}")
            exec(runlist_real[r])
        if run_set[r]=="on":
            chose=input(f"Run {runlist_real[r]}, (Y)es/(N)o:")
            if chose=="Y" or "Yes":
                exec(runlist_real[r])
        if run_set[r]=="off":
            print(f"NOT RUN {runlist_real[r]}")
def wodir():
    if not os.path.exists(conf["workspace"]):
        os.makedirs(conf["workspace"])
    os.chdir(conf["workspace"])
###############
print(versions)
###############
if conf["model"]=={}: #配置错误检查
    print("没有可调用的模型，请检查你的配置。\nNo model can use,please check your configuration.\n")
    sys.exit()
parser = argparse.ArgumentParser()
parser.add_argument("-u","--use")
parser.add_argument("-r","--run")
parser.add_argument("-s","--setting")
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }
if "-h" in argv or "--help" in argv:
    print(help)
if "-v" in argv or "--versions" in argv:
    print(versions)
if "-u" in argv or "--use" in argv:
    modelname=command_line_args["use"]
if "-r" in argv or "--run" in argv:
    task=command_line_args["run"]
if "-s" in argv or "--setting" in argv:
    pass
try:
    model=conf["model"][modelname]
    if model["lang"]=="zh":
        setup=conf["setup"]["zh"]
    elif model["lang"]=="en":
        setup=conf["setup"]["en"]
    print("Use %s\n" % modelname)
except KeyError:
    print("模型不存在，请检查你的配置。\nThe model is not exist, please check your configuration.\n")
    sys.exit()
if model=={} or model["type"]=="" or model["path"]=="" or model["lang"]=="":
    print("模型设置异常，请检查你的配置。\nThe model Settings are abnormal, please check your configuration.\n")
    sys.exit()
###############
#启动对话
if model["type"]=="script":
    connect=None
    exec(open(model["path"],"r").read())
    q_model=queue.Queue()
    e_model=Event()
    e_back=Event()
    script_run=connect(q_model,e_model,e_back,setup)
    bot=Thread(target=script_run)
    bot.start()
    wodir()
    while True:
        bat=input("You:")
        if bat=="!exit":
            e_back.clear()
            q_model.put(bat)
            e_model.set()
            if e_back.wait():
                exit()
        else:
            bat="task:"+bat
            e_back.clear()
            q_model.put(bat)
            e_model.set()
            if e_back.wait():
                response=q_model.get()
                print(response)
                runret(response)

if model["type"]=="transformers":
    model,tokenizer=trans_load(model["path"])
    response, history = model.chat(tokenizer, setup, history=[])
    print(response)
    while True:
        wodir()
        task=input("You:")
        if task=="!exit":
            sys.exit()
        response, history = model.chat(tokenizer, task, history=history)