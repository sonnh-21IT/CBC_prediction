import streamlit as st
import pickle
import pandas as pd
def app():

    st.title('Hệ thống tư vấn :green[THUỐC 💊]')
    st.markdown("""---""")

    col1,col2,col3= st.columns(3)

    with col1:
        st.success(":green[Lợi ích:] 👌" 
                " \nGiảm thiểu sai sót trong sử dụng thuốc."
                " \nNâng cao hiệu quả điều trị."
                " \nHỗ trợ trong việc tự quản lý sức khỏe.")
    with col2:
        st.warning(":red[Lưu ý:] ⛔"
                   " \nHệ thống chỉ gợi ý thuốc."
                   " \nLiều lượng và cách dùng không đúng hoặc sai ."
                   " \nCần phải xác minh với bác sĩ trước khi uống.")

    with col3:
        st.info('Thông tin: 🔎 '
                "Việc tư vấn thuốc cung cấp tên và thông tin của thuốc để hỗ trợ mọi người trong việc "
                "quản lý và sử dụng thuốc một cách an toàn và hiệu quả")

    # image = Image.open("Image/medicine-image.jpg")
    # st.image(image, caption='Recommended Medicines')

    medicines_dict = pickle.load(open('recommend/medicine_dict.pkl', 'rb'))
    medicines = pd.DataFrame(medicines_dict)

    # To load similarity-vector-data from pickle in the form of dictionary
    similarity = pickle.load(open('recommend/similarity.pkl', 'rb'))

    def recommend(medicine):
        medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
        distances = similarity[medicine_index]
        medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]

        recommended_medicines = []
        for i in medicines_list:
            recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
        return recommended_medicines

    st.markdown("""---""")
    st.title('Chọn thuốc tại đây 👇')

    selected_medicine_name = st.selectbox(
        'Chọn tên thuốc thay thế của bạn sẽ được đề xuất',
        medicines['Drug_Name'].values)
    st.markdown("""---""")

    if st.button('Tìm thuốc'):
        recommendations = recommend(selected_medicine_name)

        if recommendations:
            st.subheader("Thuốc được khuyên dùng")

            recommendations_df = pd.DataFrame({
                'Tên/ Loại thuốc đề xuất': recommendations,
             })
            st.dataframe(recommendations_df)

            j=0
            for i in recommendations:
                st.write(
                   " Thuốc :green["+ i +"] Nhấn vào đây để tìm thuốc 👉 " + "\n https://pharmeasy.in/search/all?name="+i  )  # Recommnded-drug purchase link from pharmeasy
                j=j+1


        else:
            st.write("Không tìm thấy đề xuất nào. Vui lòng kiểm tra tên thuốc và thử lại.")



