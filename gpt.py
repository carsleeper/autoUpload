from openai import OpenAI
import os
def writingArticles( word :str ) -> str:
    key = os.getenv("openaiApiKey")
    client = OpenAI(api_key= key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={ "type" : "text"},
        messages=[
            {"role":"system","content":"You are a writer who writes blog. please answer in html"},
            {"role":"user","content":f"최근 화제가 되고있는 {word}에 대해 블로그에  tistory html 작성 모드로 자동업로드 하려고 하는데, 이에 맞게 글을 써줘."},
            # {"role":"user","content":f"중간중간에 실제로 있는 사진도 넣어줘."},
            {"role":"user","content":"글을 최소 5개의 주제로 , 주제별로 최대한 길게 써줘."},
            {"role":"user","content":"진짜 사람이 쓴 것 처럼 써줘."},
            {"role":"user","content":"부가설명 없이 html소스코드만 줘."},
            {"role":"user","content":"제목을 최대한 길고 기발하게 써줘."}
        ]
    )
    result =  response.choices[0].message.content
    return result[7:-3]

print('a')