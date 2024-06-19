import streamlit as st
import matplotlib.pyplot as plt
import query
from PIL import Image

news = query.get_news()
css = """
<style>
.image-container {
  display: flex;
  justify-content: center;
}
</style>
"""
def Mark():

    st.title('Chào mừng bạn đến :red[BLOOD TEST 🩸]')
    with st.expander("CÁC BỆNH CHÚNG TÔI CÓ THỂ DỰ ĐOÁN"):
        marks1, marks2 = st.columns(2, gap='large')
        with marks1:
            st.info(':red[Phát hiện thiếu máu]', icon="🩸")
            st.image('Image/thieumau.jpg', width=300)
        with marks2:
            st.info(':red[Đánh giá nguy cơ COVID-19]', icon="🦠")
            st.image('Image/covid.jpg', width=300)
    st.info(":green[Đối tượng sử dụng :]"
               " Trang web này hướng đến những người muốn theo dõi sức khỏe của bản thân, đặc biệt là những người có nguy cơ mắc thiếu máu hoặc COVID-19.\n")
    st.info(":green[Lợi ích:]"
               " Giúp phát hiện sớm các bệnh lý nguy hiểm."
               " Theo dõi sức khỏe một cách hiệu quả."
               " Tiết kiệm thời gian và chi phí.")

    st.info("👉 Hãy truy cập trang web của chúng tôi để phân tích bảng xét nghiệm máu toàn phần và bảo vệ sức khỏe của bạn!")

    # Chia thành hai cột

    left_column, spacer, right_column = st.columns([2, 1, 2])
    # Cột bên trái
    with right_column:
        st.subheader('📊 :red[BIỂU ĐỒ]')

        def plot_anemia():
            count_1, count_0 = query.count_diseased_anemia()

            if count_1 is not None and count_0 is not None:
                labels = ['Người bị bệnh', 'Không bị bệnh']
                counts = [count_1, count_0]

                # Vẽ biểu đồ cột
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.bar(labels, counts, color=['blue', 'green'])
                ax.set_xlabel('Bệnh nhân')
                ax.set_ylabel('Số lượng')
                st.info('Biểu đồ số lượng người đã dự đoán của bệnh :red[Thiếu máu] 🩸')

                # Hiển thị biểu đồ trong streamlit
                st.pyplot(fig)
            else:
                st.write("Không thể lấy được dữ liệu từ database.")

        def plot_covid19():
            count_1, count_0 = query.count_diseased_covid()

            if count_1 is not None and count_0 is not None:
                labels = ['Người bị bệnh', 'Không bị bệnh']
                counts = [count_1, count_0]

                # Vẽ biểu đồ cột
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.bar(labels, counts, color=['red', 'green'])
                ax.set_xlabel('Bệnh nhân')
                ax.set_ylabel('Số lượng')
                st.info('Biểu đồ số lượng người đã dự đoán của bệnh :green[Covid 19] 🧪')

                # Hiển thị biểu đồ trong streamlit
                st.pyplot(fig)
            else:
                st.write("Không thể lấy được dữ liệu từ database.")

        plot_anemia()
        plot_covid19()
    # Cột bên trái
    with left_column:
        st.subheader('📰 :red[TIN TỨC]')
        for item in news:
            link_test = item['link']
            title_test = item['title']
            image_path = item['image_url']
            content = item['content']
            st.markdown(f"[**{title_test}**]({link_test})", unsafe_allow_html=False)
            if image_path:
                img_path = "Image/" + image_path
                image = Image.open(img_path)
                st.image(image, caption=content, use_column_width=True)

            else:
                st.write(content)





