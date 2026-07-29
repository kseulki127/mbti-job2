import streamlit as st

st.set_page_config(page_title="직업별 필요 역량", page_icon="🛠️")

user_mbti = st.session_state.get("user_mbti", "ISTJ")

st.title("🛠️ 추천 직업별 필요 역량 & 과목")
st.write(f"**{user_mbti}** 유형을 위한 추천 직업에서 필요한 핵심 역량입니다.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔑 주요 핵심 역량")
    st.write("- 문제 해결 능력 및 논리적 사고")
    st.write("- 원활한 의사소통 및 공감 능력")
    st.write("- 전문 도구 및 기술 활용 능력")

with col2:
    st.subheader("📚 추천 고교 선택 과목")
    st.write("- 확률과 통계 / 미적분")
    st.write("- 사회·문화 / 심리학")
    st.write("- 정보 (코딩 및 컴퓨터)")