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
填模型信息，事例：
```
"modelname":{
    "path": "path/to/model",
    "type":"api/transfromers/..."
}
```
api情况下路径中写启动脚本，脚本事例
`connect/example.py`
```
def connect(q,e,b):
    def script():
        print("Start Running")
        while True:
            if e.wait():
                task=q.get()
                if task[:5]=="task:":
                    response="model return"
                    q.put(response)
                    b.set()
                else:
                  b.set()
                e.clear()
    return script
```
