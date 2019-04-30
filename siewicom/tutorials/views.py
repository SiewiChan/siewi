from django.shortcuts import render,get_object_or_404
from django.views import View

from .models import Category,Tutorials,Articles


class IndexView(View):

    def get(self,request):
        # 获取所有的分类
        categories = Category.objects.all()
        # 对分类进行遍历
        for category in categories:
            # 从教程表中查找分类下的所有教程
            tutorials = Tutorials.objects.filter(category=category)
            # 利用python给分类动态添加属性
            category.tutorials = tutorials
        context = {
            'categories':categories,
        }
        return render(request,'client/index.html',context)


class ArticleView(View):

    def get(self,request,category,tutorial_pk=1):
        
        # 在文章详情表中通过教程名(tutorial_title）获取所有的文章
        articles = Articles.objects.filter(category = tutorial_pk)
        current_article = articles.first()
        curerent_pk = current_article.pk
        article_list = articles.filter(category__gte=curerent_pk)

        context = {
            'articles':articles, 
            'current':current_article,
            'article_list':article_list,
        }
        return render(request,'client/article.html',context)