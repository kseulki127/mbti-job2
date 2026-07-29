import streamlit as st

st.set_page_config(page_title="상담사 추천 이유", page_icon="💬")

user_mbti = st.session_state.get("user_mbti", "ISTJ")

st.title("💬 상담사의 맞춤 추천 이유")
st.write(f"왜 **{user_mbti}** 성향에게 이 직업들이 잘 맞을까요?")

st.success(f"""
🤝 **상담사 코칭 한마디:**

{user_mbti} 유형은 본인의 타고난 강점과 환경이 조화를 이룰 때 가장 멋진 역량을 발휘합니다!
자신의 장점을 살릴 수 있는 직업을 고르고, 자신감을 가지고 차근차근 준비해 보세요.
""")