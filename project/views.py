from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from articlewrite.models import articlebuy, articlefree, articlesale, articlenotic
from django.http import HttpResponseRedirect

def main(request):
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

        # try:
            #email = request.session['email']
            # select * from user where email = ?

            #user = User.objects.get(email=email)
            # insert into article (title, content, user_id) values (?, ?, ?)
        articlewrite = articlebuy(title=title, content=content)#user=user
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




################################################