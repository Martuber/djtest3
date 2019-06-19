from django.db import models

# Create your models here.


class BookInfoManager(models.Manager):
    """建立图书类的管理器"""
    def get_queryset(self):
        """修改查询集"""
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

    # 通过管理器来创建图书类
    def create(self, title, price, author=None):
        b = BookInfo()
        b.title = title
        b.author = author
        b.price = price
        return b


class HeroInfoManager(models.Manager):
    """图书类管理器"""
    def get_queryset(self):
        return super(HeroInfoManager, self).get_queryset().filter(isDelete=False)

    def create(self, name, age, bookname):
        """通过管理器类来创建对象"""
        h = HeroInfo()
        h.hero_name = name
        h.hero_age = age
        h.hero_book = bookname


class BookInfo(models.Model):
    """建立图书信息"""
    title = models.CharField(max_length=10)
    author = models.CharField(max_length=10)
    price = models.IntegerField()
    publish_date = models.DateTimeField(null=True)
    reading_volume = models.IntegerField(null=True)
    publisher = models.CharField(max_length=10,null=True)
    comments = models.CharField(max_length=1000, null=True)
    isDelete = models.BooleanField(default=False)

    # 建立一个管理器属性
    manager = BookInfoManager()
    original_manager = models.Manager()


    class Meta:
        db_table = "BookInfo"

    def __str__(self):
        return "{} {} {}".format(self.id, self.title, self.isDelete)

    def isdeleted(self):
        if self.isDelete:
            return "是"
        else:
            return "否"
    isdeleted.short_description = "是否删除"


class HeroInfo(models.Model):
    """建立图书中的英雄人物信息"""
    hero_name = models.CharField(max_length=10)
    hero_age = models.IntegerField()
    hero_book = models.ForeignKey(BookInfo)
    hero_comments = models.CharField(max_length=1000, null=True)
    hero_like = models.CharField(max_length=200, null=True)
    isDelete = models.BooleanField(default=False)

    # 建立管理器对象
    original_manager = models.Manager()
    manager = HeroInfoManager()

    class Meta:
        """定义关于模型的信息"""
        db_table = "HeroInfo"

    def __str__(self):
        return "{} {} {}".format(self.id, self.hero_name, self.hero_age)

    def isdeleted(self):
        if self.isDelete:
            return "是"
        else:
            return "否"
    isdeleted.short_description = "是否删除"

