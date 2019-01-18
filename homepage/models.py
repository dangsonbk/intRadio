from django.db import models

# Create your models here.

class Category(models.Model):
    slug = models.CharField(max_length=50,verbose_name="Slug")
    name = models.CharField(max_length=50,verbose_name="Tên category")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Letter(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null=True)
    l_from = models.CharField(max_length=100,verbose_name="Tên người gửi")
    l_to = models.CharField(max_length=100,verbose_name="Tên người nhận")

    l_from_img = models.URLField(verbose_name="Ảnh người gửi")
    l_to_img = models.URLField(max_length=250,verbose_name="Ảnh người nhận")

    l_title = models.CharField(max_length=300,verbose_name="Title")
    l_content = models.TextField(max_length=2000,verbose_name="Nội dung",blank=True,null=True)
    l_audio = models.URLField(max_length=250,verbose_name="Đường dẫn bài radio")

    l_onair_date = models.DateField(verbose_name="Ngày lên sóng")

    def __str__(self):
        return self.l_title
