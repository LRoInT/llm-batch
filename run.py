import sys
import json
import commands
from threading import Thread
conf=json.load(open("conf.json","r"))
conf=json.dumps(conf)
versions="""
LLM BATCH V0.0.1
"""
###############
print(versions)
###############
try:
    if sys.argv[1]=="--help"or sys.argv[1]=="-h":
        print("""
        -h --help 显示帮助
        -r --run 快速执行
        -u --use [-local/api]使用指定模型
        """)
except:
    pass
