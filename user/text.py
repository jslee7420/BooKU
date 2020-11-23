def signup_message(domain, uidb64, token):
    return f"아래 링크를 클릭하면 회원가입 인증이 완료됩니다. \n\n 회원가입 링크 : http://{domain}/user/activate/{uidb64}/{token}\n\n 감사합니다"


def change_pwd_message(domain, uidb64, token):
    return f"아래 링크를 클릭해서 비밀번호를 변경해주세요! \n\n 비밀번호 변경 링크 : http://{domain}/user/change_pwd/{uidb64}/{token}\n\n 감사합니다"