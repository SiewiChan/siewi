from django.db import models

# 分类表
class Category(models.Model):
    choices = (
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('os','操作系统'),
        ('python','Python'),
        ('java','Java'),
        ('js','Javascript'),
        ('c','C'),
        ('cplus','C++'),
    )

    category = models.CharField('分类名',max_length=20,choices=choices)

    def __str__(self):
        return self.category.title()

    class Meta:
        verbose_name = verbose_name_plural = '分类表'

# 课程表
class Tutorials(models.Model):
    title = models.CharField('课程名称',max_length=20)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,verbose_name='分类名')
    image = models.ImageField('缩略图',upload_to='')
    description = models.CharField('描述',max_length=150,default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '课程表'

# 文章详细表
class Articles(models.Model):
    title = models.CharField('文章标题',max_length=20)
    category = models.ForeignKey(Tutorials, on_delete=models.DO_NOTHING)
    article = models.TextField(default='Please Input information')
    author = models.CharField(max_length=50,default='陈煜')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural ='文章表'