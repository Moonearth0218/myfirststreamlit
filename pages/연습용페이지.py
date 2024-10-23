# import streamlit as st

# #st.set_page_config(page_title = "연수용페이지", page_icon="✨")

# # 페이지 제목
# st.title("형성평가를 봅시다")

# option = st.radio("선생님의 전공은 무엇일까요?", ["물리", "화학", "생명과학", "지구과학"])
# option = st.multiselect("지구과학 중 가장 좋아하는 부분은 무엇인가요?", ["지질", "대기", "해양", "우주"])

# option = st.radio("연수 장소는 어디일까요?", ["강남역", "선릉역", "역삼역", "서초역"])
# if option == '강남역' : 
# 	st. success("정답입니다!")
# 	st.balloons()
	
# elif option == "교대역":
# 	st.write("엇... 비슷한데.. 더 가까운 역이 있어요.")
# elif option == "교대역":
# 	st.write("다시 생각해보세요")
# else:
# 	st.error("다시 풀어보세요 ㅠㅠ")

# # 세 개의 열을 생성
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.header("첫 번째 열")
#     st.write("여기는 첫 번째 열입니다.")

# with col2:
#     st.header("두 번째 열")
#     st.image("https://via.placeholder.com/150", caption="이미지 예시")

# with col3:
#     st.header("세 번째 열")
#     st.button("버튼 예시")

#made by GPT
import streamlit as st

# 페이지 제목과 아이콘 설정
st.set_page_config(page_title="훈련을 위한 페이지", page_icon="✨")

# 페이지 제목 표시
st.title("형성 평가를 살펴봅시다")

# Step 1: 전공 선택
major = st.radio("제 전공은 무엇일까요?", ["물리학", "화학", "생명과학", "지구과학"])

# Step 2: 사용자가 "지구과학"을 선택한 경우 좋아하는 부분 질문
if major == "지구과학":
    favorite_part = st.multiselect(
        "지구과학에서 좋아하는 부분은 무엇입니까?", 
        ["지질학", "대기", "해양", "우주"]
    )

# Step 3: 훈련 장소 선택
location = st.radio(
    "훈련은 어디에서 진행됩니까?", 
    ["강남역", "선릉역", "역삼역", "서초역"]
)

# Step 4: 선택한 장소에 따라 정답 여부 확인
if location == '강남역':
    st.success("정답입니다!")
    #st.balloons()  # 정답일 때 풍선 효과
elif location == '선릉역':
    st.write("음... 비슷하지만 더 가까운 역이 있어요.")
elif location == '역삼역':
    st.write("다시 생각해 보세요.")
else:
    st.error("다시 시도해 보세요 ㅠㅠ")

# Step 5: 세 개의 열을 만들어 콘텐츠 표시
col1, col2, col3 = st.columns(3)

# 첫 번째 열 콘텐츠
with col1:
    st.header("첫 번째 열")
    st.write("이것은 첫 번째 열입니다.")

# 두 번째 열 콘텐츠 (예시 이미지 포함)
with col2:
    st.header("두 번째 열")
    st.image("https://via.placeholder.com/150", caption="이미지 예시")

# 세 번째 열 콘텐츠 (버튼 예시 포함)
with col3:
    st.header("세 번째 열")
    if st.button("버튼 예시"):
        st.write("버튼이 클릭되었습니다!")
