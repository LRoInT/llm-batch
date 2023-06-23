#本地模型启动库
from transformers import AutoModel,AutoTokenizer
def trans_call(load):
    tokenizer = AutoTokenizer.from_pretrained(load,remote_trust=True)
    model=AutoModel.from_pretrained(load,remote_trust=True)
    return model,tokenizer