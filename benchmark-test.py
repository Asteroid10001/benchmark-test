import os
import sys
import pandas as pd
from time import sleep

'''OPENAI_API_KEY=''
DASHSCOPE_API_KEY=''
DEEPSEEK_API_KEY=''
LLAMA_API_KEY= '''''

import openai

def call_with_message(message, model, prompt="You are a helpful assistant."):
    if "gpt" in model:
        #api_key = os.getenv("OPENAI_API_KEY")
        api_key =''
        base_url = "https://api.openai.com/v1"
    elif "qwen" in model:
        #api_key = os.getenv("DASHSCOPE_API_KEY")
        api_key =''
        base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    elif "deepseek" in model:
        #api_key = os.getenv("DEEPSEEK_API_KEY")
        api_key =''
        base_url = "https://api.deepseek.com"
        return None
    elif "llama" in model:
        #api_key = os.getenv("DASHSCOPE_API_KEY")
        api_key =''
        base_url = "https://api.llama-api.com"

    try:
        client = openai.OpenAI(
            api_key=api_key, 
            base_url=base_url,
        )
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {
                    "role": "user",
                    "content": message
                }
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"错误信息：{e}")


active_model = sys.argv[1]
print(f"test using model {active_model}")


excel_filename = "聚变大模型测试用例汇总.xlsx"
prompt_index = 1
message_index = 4

sheet_names = pd.ExcelFile(excel_filename).sheet_names
print(f"sheet names: {sheet_names}")
num_sheets = len(sheet_names)

df = pd.read_excel(excel_filename, sheet_name=list(range(num_sheets)))

with pd.ExcelWriter(f"{active_model}_{excel_filename}") as writer:
    for s in range(1, num_sheets):
        sheet = df[s]
        for i in sheet.index:
            prompt = sheet.iloc[i, prompt_index]
            if str(prompt)=="nan":
                prompt = "你是聚变物理和人工智能领域的专家。"
            message = sheet.iloc[i, message_index]
            print(f"prompt: {prompt}")
            print(f"message: {message}")
            try:
                response = call_with_message(message=message, model=active_model, prompt=prompt)
                print(f"response: {response}")
                sheet.loc[i, message_index+4] = response
            except Exception as e:
                print(f"错误信息：{e}")
                continue
            print('=============')
            sleep(1)
        sheet.to_excel(writer, sheet_name=sheet_names[s], index=True, header=True)


'''
python benchmark-test.py qwen-long
python benchmark-test.py qwen-audio-turbo
python benchmark-test.py qwen-vl-plus
python benchmark-test.py gpt-4o
python benchmark-test.py {你的model}
'''
