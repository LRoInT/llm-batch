import os
import subprocess
def runcmd(cmd):
    os.system(cmd)
    """
    result = subprocess.run(cmd.split(" "), capture_output=True, text=True) # 运行命令，并将输出解码为文本
    print(result.stdout) # 打印标准输出，是一个字符串
    print(result.stderr) # 打印标准错误，是一个字符串
    """


