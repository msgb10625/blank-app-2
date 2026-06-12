import streamlit as st

# 1. 메뉴 및 가격 데이터 설정
menu = ["아이스아메리카노", "카페라떼", "초코라떼"]
price = [3000, 3500, 4000]

# 앱 타이틀
st.title("☕ 미니 카페 키오스크")
st.subheader("원하시는 메뉴를 선택해주세요.")

# 2. 화면에 메뉴판 출력 (반복문 활용)
st.write("---")
st.markdown("### 📋 메 뉴 판")
for i in range(3):
    st.write(f"**{i+1}. {menu[i]}** — {price[i]:,}원")
st.write("---")

# 3. Streamlit 라디오 버튼으로 메뉴 입력 받기
# 화면에는 '메뉴명 (가격원)'으로 보여주고, 선택된 인덱스를 가져옵니다.
options = [f"{menu[i]} ({price[i]:,}원)" for i in range(3)]
choice = st.radio("메뉴 선택", options)

# 4. 주문하기 버튼 클릭 시 결과 출력
if st.button("주문하기"):
    # 사용자가 선택한 문구에서 메뉴 이름만 추출하기 위해 index 활용
    selected_index = options.index(choice)
    selected_menu = menu[selected_index]
    
    # 성공 메시지 출력
    st.success(f"✅ {selected_menu} 주문이 완료되었습니다!")