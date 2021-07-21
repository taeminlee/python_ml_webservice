import streamlit as st

st.write("""
# DEMO
- streamlit 😀
""")

model = lambda x: x[::-1]  # 모델 초기화

query = st.text_input('질의문. 한 문장으로 입력해주세요.', value='예제 입력 문장 입니다.')

if st.button("Run"):
    result = model(query)
    st.write(result)