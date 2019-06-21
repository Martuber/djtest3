from django.shortcuts import render
from .models import  *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

"""定义视图：
    视图就是一个函数
    必须要有一个HttpRequest实例 (即接受一个web请求）
    必须返回一个web响应(HttpResponse对象)
    """

def index(request):
    # 查询金庸作品书籍
    book_by_jy = BookInfo.original_manager.filter(author="金庸")

    # 查询所有倚天屠龙记中的英雄人物
    heroes_in_yitian = HeroInfo.manager.filter(hero_book__title="倚天屠龙记")

    # 查询英雄名为 “郭靖”的图书

    book_contain_xz = BookInfo.manager.filter(heroinfo__hero_name__contains="小朱")

    bookslist = {"books": book_by_jy, "heroes_in_yitian": heroes_in_yitian,
                 "book_contain_xz":book_contain_xz}
    return render(request, template_name="booktest/index.html", context=bookslist)

"""
讲解Requet对象
作用是接收包含请求报文的内容（参数），包含两种方案：
    - get(在url中分？后面的部分给出具体参数)
    - post

"""



def detail(request, p1):
    """定义一个视图， 接受来自url中的参数"""
    return HttpResponse(p1)

def show(*args):
    """定义一个视图， 接受位置参数和关键字参数"""
    return HttpResponse(" {}-{}-{}".format(args[1], args[2], args[3]))



def show_kwargs(request,P1, P2, P3):
    """定义一个视图， 接受位置参数和关键字参数"""
    return HttpResponse(" {}--{}--{}".format(P1, P2, P3))


"""展示链接的页面"""
def getTest1(request):

    return render(request, "booktest/getTest1.html")

# 接受一键一值的情况
# 是指：当原始url通过get方式请求，在？后面带有若干的关键字参数，当正则匹配之后，匹配到对应的视图函数，并由request接受
def getTest2(request):
    # 根据键接受值（此处一个键只有一个值 ）
    a1 = request.GET["a"]   # request.GET["a"] 等同于 request.GET.get("a")  该方法只能获取键值的最新一个值
    b1 = request.GET["b"]
    c1 = request.GET["c"]

    # 构造上下文
    contest = {"a": a1, "b": b1, "c": c1}

    # 向模板中传递上下文，并进行渲染
    return render(request, "booktest/getTest2.html", context=contest)

# 接受一键多值的情况
def getTest3(request):

    alist = request.GET.getlist("a")

    context = {"alist":alist}

    return render(request, "booktest/getTest3.html", context=context)

"""

POST方式 

定义两个视图：


"""

def postTest1(request):
    """填写表单信息"""

    return render(request, template_name="booktest/postTest1.html")


def postTest2(request):
    """接受表单信息"""

    uname = request.POST["uname"]   # 这个键对应前端表单的提交字段
    upwd = request.POST["upassword"]
    ugender = request.POST["ugender"]
    uhobby = request.POST.getlist("uhobby")

    # 构建上下文，向模板中传递数据
    context = {"uname":uname, "upwd":upwd, "ugender":ugender, "uhobby":uhobby}

    return render(request, template_name="booktest/postTest2.html", context=context)

"""
Response 对象

属性：
    - content: 表示要返回的内容，字符串类型
    - charset: 
方法：
    - init():
    - write():
    - flush():
    - set_cookie():
    

"""
# cookie 是一个字典对象
def cookieTest1(request):
    cookies = request.COOKIES
    response = HttpResponse()
    if cookies.__contains__("cookie_data"):
        response.write(cookies["cookie_data"])

    """设置一个cookie键值"""
    # response.set_cookie("cookie_data","abc")    #  会在浏览器上显示：Set-Cookie: cookie_data=abc;

    return response


"""重定向"""
def rederect(request):
    return HttpResponseRedirect("/booktest/target_page")


def target_page(request):
    return HttpResponse("这是重定向之后的地址")

"""session
作用：状态保持
"""