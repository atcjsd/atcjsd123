from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from articlewrite.models import articlebuy, articlefree, articlesale, articlenotic
from django.http import HttpResponseRedirect
<<<<<<< HEAD
from article.models import User, Article
=======
import os
>>>>>>> 37674a29ca811dfc17c0da151fe1811d7e720269

# 메인
def main(request):
    return render(request, 'main.html')

<<<<<<< HEAD
# 회원가입
=======
def sell(request):
    return render(request, 'main.html')

def community(request):
    return render(request, 'community.html')


########################################################3
#def list(request):
#    # select * from article order by id desc
#    article_list = Article.objects.order_by('-id')
#    context = {
#        'article_list' : article_list
#    }
#    return render(request, 'list.html', context)

def list_buy(request):
    # select * from article order by id desc
    article_list = articlebuy.objects.order_by('-id')
    context = {
        'articlewrite_list' : article_list
    }
    return render(request, 'list_buy.html', context)

def list_sale(request):
    # select * from article order by id desc
    article_list = articlesale.objects.order_by('-id')
    context = {
        'articlewrite_list' : article_list
    }
    return render(request, 'list_sale.html', context)

def list_free(request):
    # select * from article order by id desc
    article_list = articlefree.objects.order_by('-id')
    context = {
        'articlewrite_list' : article_list
    }
    return render(request, 'list_free.html', context)

def list_notic(request):
    # select * from article order by id desc
    article_list = articlenotic.objects.order_by('-id')
    context = {
        'articlewrite_list' : article_list
    }
    return render(request, 'list_notic.html', context)



#########################################################33
def write_buy(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES['image']

        try: # 디렉토리 생성
            os.mkdir('upload1')
        except FileExistsError:
            pass
        image_name = image.name
        with open('media/image/' + image_name, 'wb') as file:
            for chunk in image.chunks():
                file.write(chunk)

        # try:
            #email = request.session['email']
            # select * from user where email = ?

            #user = User.objects.get(email=email)
            # insert into article (title, content, user_id) values (?, ?, ?)
        articlewrite = articlebuy(title=title, content=content, image=image)
        #user=user
        articlewrite.save()
        
        return render(request, 'write_success.html')
        # except:
        #     return render(request, 'write_fail.html')

    return render(request, 'write_buy.html')

def write_free(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # try:
            #email = request.session['email']
            # select * from user where email = ?

            #user = User.objects.get(email=email)
            # insert into article (title, content, user_id) values (?, ?, ?)
        articlewrite = articlefree(title=title, content=content)#user=user
        articlewrite.save()
        
        return render(request, 'write_success.html')
        # except:
        #     return render(request, 'write_fail.html')

    return render(request, 'write_free.html')

def write_sale(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # try:
            #email = request.session['email']
            # select * from user where email = ?

            #user = User.objects.get(email=email)
            # insert into article (title, content, user_id) values (?, ?, ?)
        articlewrite = articlesale(title=title, content=content)#user=user
        articlewrite.save()
        
        return render(request, 'write_success.html')
        # except:
        #     return render(request, 'write_fail.html')

    return render(request, 'write_sale.html')

def write_notic(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # try:
            #email = request.session['email']
            # select * from user where email = ?

            #user = User.objects.get(email=email)
            # insert into article (title, content, user_id) values (?, ?, ?)
        articlewrite = articlenotic(title=title, content=content)#user=user
        articlewrite.save()
        
        return render(request, 'write_success.html')
        # except:
        #     return render(request, 'write_fail.html')

    return render(request, 'write_notic.html')

########################################################3

def detail_buy(request, id):
    # select * from article where id = ?
    articlewrite = articlebuy.objects.get(id=id)
    context = {
        'article' : articlewrite
    }
    return render(request, 'detail_buy.html', context)

def detail_free(request, id):
    # select * from article where id = ?
    articlewrite = articlefree.objects.get(id=id)
    context = {
        'article' : articlewrite
    }
    return render(request, 'detail_free.html', context)

def detail_sale(request, id):
    # select * from article where id = ?
    articlewrite = articlesale.objects.get(id=id)
    context = {
        'article' : articlewrite
    }
    return render(request, 'detail_sale.html', context)

def detail_notic(request, id):
    # select * from article where id = ?
    articlewrite = articlenotic.objects.get(id=id)
    context = {
        'article' : articlewrite
    }
    return render(request, 'detail_notic.html', context)

#################################################################
def update_buy(request, id):
    # select * from article where id = ?
    articlewrite = articlebuy.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            # update article set title = ?, content = ? where id = ?
            articlewrite.title = title
            articlewrite.content = content
            articlewrite.save()
            return render(request, 'update_success.html')
        except:
            return render(request, 'update_fail.html')
    context = {
        'article' : articlewrite
    }
    return render(request, 'update_buy.html', context)

def update_free(request, id):
    # select * from article where id = ?
    articlewrite = articlefree.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            # update article set title = ?, content = ? where id = ?
            articlewrite.title = title
            articlewrite.content = content
            articlewrite.save()
            return render(request, 'update_success.html')
        except:
            return render(request, 'update_fail.html')
    context = {
        'article' : articlewrite
    }
    return render(request, 'update_free.html', context)

def update_sale(request, id):
    # select * from article where id = ?
    articlewrite = articlesale.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            # update article set title = ?, content = ? where id = ?
            articlewrite.title = title
            articlewrite.content = content
            articlewrite.save()
            return render(request, 'update_success.html')
        except:
            return render(request, 'update_fail.html')
    context = {
        'article' : articlewrite
    }
    return render(request, 'update_sale.html', context)

def update_notic(request, id):
    # select * from article where id = ?
    articlewrite = articlenotic.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            # update article set title = ?, content = ? where id = ?
            articlewrite.title = title
            articlewrite.content = content
            articlewrite.save()
            return render(request, 'update_success.html')
        except:
            return render(request, 'update_fail.html')
    context = {
        'article' : articlewrite
    }
    return render(request, 'update_notic.html', context)

###########################################################################

def delete_buy(request, id):
    try:
        # select * from article where id = ?
        articlewrite = articlebuy.objects.get(id=id)
        articlewrite.delete()
        return render(request, 'delete_success.html')
    except:
        return render(request, 'delete_fail.html')

def delete_free(request, id):
    try:
        # select * from article where id = ?
        articlewrite = articlefree.objects.get(id=id)
        articlewrite.delete()
        return render(request, 'delete_success.html')
    except:
        return render(request, 'delete_fail.html')

def delete_sale(request, id):
    try:
        # select * from article where id = ?
        articlewrite = articlesale.objects.get(id=id)
        articlewrite.delete()
        return render(request, 'delete_success.html')
    except:
        return render(request, 'delete_fail.html')

def delete_notic(request, id):
    try:
        # select * from article where id = ?
        articlewrite = articlenotic.objects.get(id=id)
        articlewrite.delete()
        return render(request, 'delete_success.html')
    except:
        return render(request, 'delete_fail.html')


######################################################################
#####################################################################

>>>>>>> 37674a29ca811dfc17c0da151fe1811d7e720269
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




################################################