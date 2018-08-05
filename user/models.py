from django.db import models


# 创建用户模型
class UserModel(models.Model):

    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=64, unique=True)
    # False 代表女
    sex = models.BooleanField(default=False)
    icon = models.ImageField(upload_to='icons', null=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'dayfresh_users'


class UserTicketModel(models.Model):

    # 关联用户表
    user = models.ForeignKey(UserModel)
    # ticket设置
    ticket = models.CharField(max_length=256)
    # 过期时间
    out_time = models.DateTimeField()

    class Meta:
        db_table = 'dayfresh_users_ticket'

