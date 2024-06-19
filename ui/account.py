import query
import streamlit as st
import bcrypt

def validate_inputs(input_list):
    invalid_inputs = []
    
    for key, value in input_list:
        if not value or not value.strip():  # Kiểm tra nếu không có dữ liệu hoặc chỉ chứa khoảng trắng
            invalid_inputs.append(key)
    
    return invalid_inputs

def info(user):
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
def app():
    st.title('Chào mừng bạn đến :red[BLOOD TEST] 🩸')
    if 'logged_in' in st.session_state:
        if st.session_state.logged_in['is_logged']:
            user = {'user_id':st.session_state.logged_in['user_id'],'name': st.session_state.logged_in['name'], 'phone': st.session_state.logged_in['phone'],
                    'email': st.session_state.logged_in['email'],'total': st.session_state.logged_in['total']}
            info(user)
        else:
            choice = st.selectbox('Login/Signup', ['Đăng nhập', 'Tạo tài khoản'])
            if choice == 'Đăng nhập':
                email = st.text_input('Địa chỉ Email', placeholder='Enter your username here ...')
                password = st.text_input('Mật khẩu', type='password', placeholder='Enter your password here ...')
                
                if st.button('Đăng nhập'):
                    input_list = [("Địa chỉ Email", email), ("Mật khẩu", password)]
                    invalid_inputs = validate_inputs(input_list)
                    if len(invalid_inputs)>0:
                        st.warning("Đầu vào không hợp lệ: "+ str(invalid_inputs))
                    else:
                        user = query.verify_credentials(email,password)
                        if user:
                            # Lưu thông tin người dùng vào session state
                            st.session_state.logged_in = {'is_logged': True,'user_id':user['id'], 'name':user['name'],'phone':user['phone'],'email':user['email'],'total':query.total_test_count(user['id'])}
                            info(st.session_state.logged_in)
                        else:
                            st.markdown("""
                                <style>
                                .error-box {
                                    padding: 10px;
                                    border: 2px solid red;
                                    border-radius: 5px;
                                    background-color: #f8d7da;
                                    color: red;
                                    font-size: 16px;
                                }
                                </style>
                                <div class="error-box">
                                    <h4>⚠️ Lỗi đăng nhập</h4>
                                    <p>Có vấn đề với tài khoản hoặc mật khẩu của bạn ! </p>
                                </div>
                            """, unsafe_allow_html=True)

            else:
                # need phone
                name = st.text_input('Tên người dùng')
                email = st.text_input('Địa chỉ Email')
                phone = st.text_input('Số điện thoại')
                password = st.text_input('Mật khẩu', type='password')

                if st.button('Tạo tài khoản'):
                    input_list = [("Tên người dùng", name),("Địa chỉ Email", email), ("Số điện thoại", phone), ("Mật khẩu", password)]
                    invalid_inputs = validate_inputs(input_list)
                    if len(invalid_inputs)>0:
                        st.warning("Đầu vào không hợp lệ: "+ str(invalid_inputs))
                    else:
                        user = query.signup(name, email, phone, bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))
                        st.session_state.logged_in = {'is_logged': True,'user_id':user['id'], 'name': user['name'], 'phone': user['phone'],
                                                        'email': user['email'],'total':query.total_test_count(user['id'])}
                        info(st.session_state.logged_in)
                        st.markdown("""
                                <style>
                                .success-box {
                                    padding: 10px;
                                    border: 2px solid green;
                                    border-radius: 5px;
                                    background-color: #dff0d8;
                                    color: green;
                                    font-size: 16px;
                                }
                                </style>
                                <div class="success-box">
                                    <h4>🎉 Success!</h4>
                                    <p>Tài khoản của bạn đã được tạo thành công. Bây giờ bạn có thể đăng nhập bằng tài khoản mới của mình.</p>
                                </div>
                            """, unsafe_allow_html=True)
