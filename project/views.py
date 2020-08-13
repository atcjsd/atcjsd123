from django.http import HttpResponse
from django.shortcuts import render
from articlewrite.models import articlebuy, articlefree, articlesale

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