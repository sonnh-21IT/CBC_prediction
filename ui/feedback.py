import streamlit as st
import query
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

def app():

    if 'logged_in' in st.session_state:
        if st.session_state.logged_in['is_logged']:

            progress = ["Covid19", "Thiếu Máu","Đái Tháo Đường"]
            st.title(':red[Gửi phản hồi cho chúng tôi]  💖')
            user = {'name': st.session_state.logged_in['name'],'user_id':st.session_state.logged_in['user_id'], 'phone': st.session_state.logged_in['phone'],
                    'email': st.session_state.logged_in['email'],'total':st.session_state.logged_in['total']}
            with st.expander("Thông tin của bạn"):
                marks1, marks2, marks3 = st.columns(3, gap='large')
                with marks1:
                    st.info(user['name'], icon="👤")
                with marks2:
                    st.info(user['phone'], icon="📞")
                with marks3:
                    st.info(str(user['total'])+' lần test', icon="🧪")
            selected_progress = st.selectbox("Bệnh đã dự đoán:", progress)

            table_name = ''
            df = pd.DataFrame()
            if selected_progress == "Covid19":
                data_dict = query.get_data_by_user_id(user['user_id'],'covid_test_results')
                if data_dict is not None:
                    data_dict['created_at'] = data_dict['created_at'].strftime('%Y-%m-%d %H:%M:%S')
                    df = pd.DataFrame(data_dict, index=[0])
                    df = df.drop('user_id', axis=1)
                table_name = 'covid_test_results'
            elif selected_progress == "Thiếu Máu":
                data_dict = query.get_data_by_user_id(user['user_id'],'anemia_test_results')
                if data_dict is not None:
                    data_dict['created_at'] = data_dict['created_at'].strftime('%Y-%m-%d %H:%M:%S')
                    df = pd.DataFrame(data_dict, index=[0])
                    df = df.drop('user_id', axis=1)
                table_name = 'anemia_test_results'
            elif selected_progress == "Đái Tháo Đường":
                data_dict = query.get_data_by_user_id(user['user_id'],'anemia_test_results')
                if data_dict is not None:
                    data_dict['created_at'] = data_dict['created_at'].strftime('%Y-%m-%d %H:%M:%S')
                    df = pd.DataFrame(data_dict, index=[0])
                    df = df.drop('user_id', axis=1)
                table_name = 'diabetes_test_results'
            feedback = st.text_area("Phản hồi:")
            
            # Tạo GridOptionsBuilder để cấu hình bảng
            gb = GridOptionsBuilder.from_dataframe(df)
            gb.configure_selection('multiple', use_checkbox=True)  # Cấu hình để chọn nhiều hàng với checkbox
            
            grid_options = gb.build()
            # Hiển thị bảng với AgGrid
            grid_response = AgGrid(
                df,
                gridOptions=grid_options,
                update_mode=GridUpdateMode.SELECTION_CHANGED,  # Cập nhật khi có thay đổi trong lựa chọn
                enable_enterprise_modules=True,
                theme='streamlit',  # Bạn có thể chọn các theme khác như 'light', 'dark', 'blue', 'fresh', 'material'
                height=200,
                width='100%',
            )

            satisfaction_level_options = ["Dự đoán chính xác", "Dự đoán không chính xác"]
            satisfaction_level = st.radio("Bạn thấy dự đoán của chúng tôi như thế nào?", options=satisfaction_level_options)
            if st.button("Gửi phản hồi"):
                selected_rows = grid_response['selected_rows']
                if selected_rows is None:
                    st.warning("Bạn chưa chọn mục dự đoán của chúng tôi!!")
                elif selected_rows is not None and not selected_rows.empty:
                    if satisfaction_level == "Dự đoán không chính xác":
                        diseased = 0
                        if selected_rows['diseased'][0] == 0:
                            diseased = 1
                        query.update_data_predict(user['user_id'],diseased,table_name)
                    query.insert_feedback(st.session_state.logged_in['user_id'],selected_progress, feedback, satisfaction_level)
                    st.markdown("""
                                <style>
                                .success-box {
                                    padding: 20px;
                                    border-radius: 10px;
                                    background-color: #f0f8ff;
                                    color: #006400;
                                    font-size: 18px;
                                    width: 400px;
                                    margin: 0 auto;
                                    text-align: center;
                                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                                }
                                .success-box h4 {
                                    margin-top: 0;
                                    font-size: 24px;
                                    color: #006400;
                                }
                                .success-box p {
                                    margin-bottom: 0;
                                }
                                </style>
                                <div class="success-box">
                                    <h4>🎉 Phản hồi đã được gửi!</h4>
                                    <p>Cảm ơn bạn đã sử dụng dịch vụ dự đoán của chúng tôi!</p>
                                </div>
                            """, unsafe_allow_html=True)
                    st.balloons()
        else:
            st.info("Hãy đăng nhập để phản hồi!!")
