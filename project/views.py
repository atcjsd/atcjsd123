from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

def main(request):
    return render(request, 'main.html')

def signup(request):
    # 실제 데이터베이스에 데이터를 저장(회원가입)
    if request.method == 'POST':
        # 회원정보 저장
        email = request.POST.get('email')
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        user = User(email=email, name=name, pwd=pwd)
        user.save()
        return HttpResponseRedirect('/index/')

    # 회원가입을 위한 양식(HTML) 전송

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        # 회원정보 조회
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        try:
            # select * from user where email=? and pwd=?
            user = User.objects.get(email=email, pwd=pwd)
            request.session['email'] = email
            return render(request, 'signin_success.html')
        except:
            return render(request, 'signin_fail.html')
    return render(request, 'signin.html')

def signout(request):
    del request.session['email'] # 개별 삭제
    request.session.flush() # 전체 삭제

    return HttpResponseRedirect('/index/')

def map(request): # 지도
    return render(request, 'map.html')
