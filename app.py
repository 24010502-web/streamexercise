st.title("나의 첫 번째 Streamlit 앱! 👋")

    # 간단한 텍스트를 표시합니다.
    st.write("Streamlit은 정말 쉽고 빠르네요!")

    # 버튼을 추가하고 클릭 이벤트를 처리합니다.
    if st.button("인사하기"):
        st.success("안녕하세요! 반갑습니다.")

# 파이썬 파일을 직접 실행했을 때 main 함수를 호출합니다.
if __name__ == "__main__":
    main()
  
