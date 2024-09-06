import json
import os
import random

def dump_jsonl(jsons, file_path):
    with open(file_path, 'w') as f:
        for js in jsons:
            json.dump(js, f, ensure_ascii=False)
            f.write('\n')

os.system('unzip gcjpy.zip -d gcjpy')

dataset = []
for i, author in enumerate(os.listdir("./gcjpy")):
    for file in os.listdir("./gcjpy/" + author):
        file_path = os.path.join("./gcjpy/" + author, file)
        code = open(file_path, "r").read()
        js = {'author': author, 'label': i, 'code': code}
        dataset.append(js)

split = [0.9, 0.05, 0.05]
random.shuffle(dataset)
train_size = int(len(dataset) * split[0])
eval_size = int(len(dataset) * split[1])

train_dataset = dataset[:train_size]
eval_dataset = dataset[train_size: train_size + eval_size]
test_dataset = dataset[train_size + eval_size:]

dump_jsonl(train_dataset, "./train.jsonl")
dump_jsonl(eval_dataset, "./valid.jsonl")
dump_jsonl(test_dataset, "./test.jsonl")

