import streamlit as st

st.set_page_config(page_title="직업별 MBTI 비율", page_icon="📊")

# 메인에서 선택한 MBTI 불러오기 (기본값 ISTJ)
user_mbti = st.session_state.get("user_mbti", "ISTJ")

st.title("📊 추천 직업군과 실제 MBTI 비율")
st.write(f"현재 선택된 MBTI (**{user_mbti}**)에게 추천하는 직업군과 실제 종사자 비율입니다.")

# 간단한 데이터 예시 (직업별 비율)
RATIO_DATA = {
    "ISTJ": {"데이터 분석가": {"ISTJ": 28, "INTJ": 22, "ESTJ": 18, "기타": 32}, "회계사": {"ISTJ": 35, "ESTJ": 25, "ISFJ": 12, "기타": 28}},
    "ENFP": {"마케팅 기획자": {"ENFP": 35, "ENTP": 25, "INFP": 15, "기타": 25}, "방송 PD": {"ENFP": 32, "ENTP": 22, "기타": 46}},
}

# 데이터가 없는 경우 기본값 제공
data = RATIO_DATA.get(user_mbti, {"추천 직업 A": {user_mbti: 30, "기타": 70}, "추천 직업 B": {user_mbti: 25, "기타": 75}})

for job, ratios in data.items():
    st.markdown(f"### 📌 {job}")
    for mbti, pct in ratios.items():
        st.text(f"{mbti}: {pct}%")
        st.progress(pct)
    st.write("")