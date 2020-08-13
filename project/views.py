from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from article.models import User, Article

# 메인
def main(request):
    return render(request, 'main.html')

# 회원가입
def signup(request):
    # 실제 데이터베이스에 데이터를 저장(회원가입)
    if request.method == 'POST':
        # 회원정보 저장
        name = request.POST.get('name')
        id = request.POST.get('id')
        pwd = request.POST.get('pwd')
        birth1 = request.POST.get('birth1')
        birth2 = request.POST.get('birth2')
        birth3 = request.POST.get('birth3')
        gender = request.POST.get('gender')
        zonecode = request.POST.get('zonecode')
        address = request.POST.get('address')
        address_etc = request.POST.get('address_etc')
        phone = request.POST.get('phone')
        phone1 = request.POST.get('phone1')
        phone2 = request.POST.get('phone2')
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        user = User(name = name, id = id, pwd = pwd,
                    birth = birth1 + '.' + birth2 + '.' + birth3,
                    gender = gender,
                    address = zonecode + '/' + address + address_etc,
                    phone = phone + phone1 + phone2,
                    email = email1 + '@' + email2)
        user.save()
        return HttpResponseRedirect('/signup_success/')
    
    # 회원가입을 위한 양식(HTML) 전송
    return render(request, 'signup.html')

def signup_success(request):
    return render(request, 'signup_success.html')

# 로그인
def signin(request):
    if request.method == 'POST':
        # 회원정보 조회
        id = request.POST.get('id')
        pwd = request.POST.get('pwd')
        try:
            # select * from user where id=? and pwd=?
            user = User.objects.get(id=id, pwd=pwd)
            request.session['id'] = id
            return render(request, 'signin_success.html')
        except:
            return render(request, 'signin_fail.html')
    return render(request, 'signin.html')

# 로그아웃
def signout(request):
    del request.session['id'] # 개별 삭제
    request.session.flush() # 전체 삭제

    return HttpResponseRedirect('/main/')

# 지도
def map(request): 
    return render(request, 'map.html')

# 아이디 중복검사
def check_id(request):
    user_id = request.GET.get('user_id')

    # DB 값 비교

    result = {'code':'아이디 중복 확인', 'msg':user_id + ' 사용 가능한 아이디입니다.'}

    return JsonResponse(result)
