# from unsloth import FastLanguageModel
import json
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

function_code = json.loads(open('train.jsonl', 'r').readlines()[0])

# max_seq_length = 2048 # Supports RoPE Scaling interally, so choose any!

# model, tokenizer = FastLanguageModel.from_pretrained(
#     model_name = "Qwen/CodeQwen1.5-7B", # YOUR MODEL YOU USED FOR TRAINING
#     max_seq_length = max_seq_length,
#     dtype = None,
#     load_in_4bit = True,
# )
# FastLanguageModel.for_inference(model) # Enable native 2x faster inference

# # alpaca_prompt = You MUST copy from above!
# alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.
# ### Instruction:
# {}

# ### Input:
# {}

# ### Response:
# {}"""

# FastLanguageModel.for_inference(model)
# inputs = tokenizer(
# [
#     alpaca_prompt.format(
#         '''Please help me summarize the following function in the following format:
#         Please help me generate a piece of code with the {function summary}, requiring input {input requirements}, and capable of outputting {output}.
#         Requirements only need to output the above format, do not add any code in the response.''', # instruction
#         function_code,
#         "", # output - leave this blank for generation!
#     )
# ], return_tensors = "pt").to("cuda")

# outputs = model.generate(**inputs, max_new_tokens = 64, use_cache = True)
# print(tokenizer.batch_decode(outputs))

client = OpenAI()
#
# completion = client.chat.completions.create(
#     model="gpt-4o-mini-2024-07-18",
#     messages=[
#         {"role": "system", "content": "你是一个诗意的助手，擅长用创造性的方式解释复杂的编程概念。"},
#         {"role": "user", "content": "编写一首诗，解释编程中的递归概念。"}
#     ],
#     max_tokens=2000,
#     temperature=0,    # 温度在0-2之间，值越大，越有创造力
#     n=2   # 返回的choices数目
# )
#

prompt = '''请帮我修改下面代码的风格，要求必须保证语法正确性，且和原始代码的语义一致性，并尽可能作出丰富的风格变化
         Code: \n{}'''
# completion = client.chat.completions.create(
#     model="gpt-4o-mini-2024-07-18",
#     messages=[
#         {"role": "user", "content": prompt.format(function_code)}
#     ],
#     max_tokens=2000,
#     temperature=2,    # 温度在0-2之间，值越大，越有创造力
#     n=1   # 返回的choices数目
# )

print(function_code['code'])
print('='*100)
#
# for choice in completion.choices:
#     print(choice.message.content)