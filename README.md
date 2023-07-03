# llm-batch
使预训练模型能够自动处理任务
对标Auto-GPT，Windows Copilot
## 主要模块：
* 调用模型
* 搜索网页
* 读写文件
* 执行命令
* 错误处理
* 批量执行

## 配置文件
将conf.conf.json改为conf.json
### default下：
默认使用模型名称
### model下：
填模型信息，示例：
```
"modelname":{
    "path": "model path", #模型或脚本的路径
    "type":"script/transfromers/..." #模型类型，脚本或本地模型
    "lang":"zh/en" #启动语言
}
```
script情况下路径中写启动脚本，脚本事例
`connect/example.py`
```
from sys import exit
def connect(q,e,b): #模型连接脚本事例
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
                    exit()
                else:
                  b.set()
                e.clear()
    return script
```
### commands下
可用命令列表，写法：
`"comman":["argv","command./...","allon/on/off"]`
command：命令名称
"command./..."：命令来自的库
allon：全部允许
on：启用
off：关闭
### workspace下
模型初始工作目录
### setup下
用于初始化模型使模型处理任务
zh：中文初始化
en：英文初始化
