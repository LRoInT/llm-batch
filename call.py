#本地模型启动库
from transformers import AutoModel,AutoTokenizer
def trans_load(load):
    #启动本地transformers模型
    model = AutoModel.from_pretrained(load)
    tokenizer = AutoTokenizer.from_pretrained(load)
    return model,tokenizer
