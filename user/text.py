def signup_message(domain, uidb64, token):
    return f"BooKU는 대학생이라면 누구나 쉽게 전공책을 거래할 수 있는 플랫폼입니다.\n\n우리학교, 우리과 사람들과 전공책을 거래하고 소통하길 희망하시면 하단의 인증하기 링크를 클릭하고 회원가입 인증을 완료해주세요 \n\n 회원가입 링크: http://{domain}/user/activate/{uidb64}/{token}\n\n 감사합니다"
