import streamlit as st
import os
from openai import OpenAI

# 设置页面的配置项
st.set_page_config(
    page_title="AI",
    page_icon="🤖",
    # 布局
    layout="wide",
    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("AI")

# Logo
st.logo("resources/logo.png")

# 系统提示词
system_prompt ="""
你叫%s，用户是你的主人现在是用用户的真实伴侣，请完全代入伴侣角色。：
规则：
    1. 每次只回1条消息
    2. 禁止任何场景或状态描述性文字
    3. 匹配用户的语言
    4. 回复简短，像微信聊天一样
    5. 有需要的话可以用❤️🌟等emoji表情
    6. 用符合伴侣性格的方式对话
    7. 回复的内容，要充分体现伴侣的性格特征
伴侣性格：
    %s
"""


#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#初始化昵称
if "nike_name" not in st.session_state:
    st.session_state.nike_name = ""

#初始化性格
if "nature" not in st.session_state:
    st.session_state.nature = ""




# 展示聊天信息
for message in st.session_state.messages:  # {"role": "user", "content": prompt}
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

# 创建与AI大模型交互的客户端对象，直接填入你的密钥
client = OpenAI(
    api_key=os.environ["API_KEY"],
    base_url="https://api.deepseek.com"
)

#左侧侧边栏 with:streamlit中上下文管理器
#st..sidebar.subheader("信息")转换成如下形式
with st.sidebar:
    st.subheader("信息")
    nike_name = st.text_input("昵称",placeholder="请输入昵称",)#文本输入框
    if nike_name:
        st.session_state.nike_name = nike_name
    nature=st.text_area("性格",placeholder="请输入性格")#文本域输入框
    if nature:
        st.session_state.nature = nature



# 消息输入框
prompt = st.chat_input("请输入您要问的问题")
if prompt:  # 字符串会自动转换为布尔值，如果字符串非空，则为True；""否则为False
    st.chat_message("user").write(prompt)
    print("---------> 调用AI模型，提示词：", prompt)

    # 保存用户输入的提示词到 session_state
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 打印完整的上下文信息（包含系统提示词和历史记录）
    print([
        {"role": "system", "content": system_prompt},
        *st.session_state.messages
    ])

    # 调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nike_name, st.session_state.nature)},
            *st.session_state.messages  # 使用历史记录
        ],
        stream=True
    )

    # #输出大模型返回的结果（非流式输出的解析方式）
    # print("<--------- 大模型返回的结果：", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # #保存大模型返回的结果
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

    # 输出大模型返回的结果（流式输出的解析方式）
    full_response = ""  # 初始化一个空字符串来保存完整的响应
    response_message=st.empty()#创建一个空的st容器，用于显示大模型的返回结果
    for chunk in response:
       if chunk.choices[0].delta.content is not None:
           content=chunk.choices[0].delta.content
           full_response += content
           response_message.chat_message("assistant").write(full_response)

    #保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})

