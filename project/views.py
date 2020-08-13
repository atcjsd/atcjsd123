from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

def main(request):
    return render(request, 'main.html')

def signup(request):
    # 실제 데이터베이스에 데이터를 저장(회원가입)
    if request.method == 'POST':
        # 회원정보 저장
        name = request.POST.get('name')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        user = User(email=email, name=name, pwd=pwd)
        user.save()
        return HttpResponseRedirect(request, 'signup_success.html')

    # 회원가입을 위한 양식(HTML) 전송

    return render(request, 'signup.html')

# 로그인
def signin(request):
    if request.method == 'POST':
        # 회원정보 조회
        id = request.POST.get('id')
        pwd = request.POST.get('pwd')
        try:
            # select * from user where email=? and pwd=?
            user = User.objects.get(id=id, pwd=pwd)
            request.session['id'] = id
            return render(request, 'signin_success.html')
        except:
            return render(request, 'signin_fail.html')
    return render(request, 'signin.html')

# 로그아웃
def signout(request):
    del request.session['email'] # 개별 삭제
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
