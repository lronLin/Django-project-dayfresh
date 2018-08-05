import re
from datetime import datetime

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse

from user.models import UserTicketModel


class UserMiddle(MiddlewareMixin):

    # 请求拦截
    def process_request(self, request):

        # 过滤
        paths = ['/user/login/', '/user/register/', '/']
        # if request.path in paths:
        #     return None
        # 与上面方法返回的值是一样的
        for path in paths:
            # match - 正则匹配
            if re.match(path, request.path):
                return None

        # 验证用户的登录状态 - 获取ticket
        ticket = request.COOKIES.get('ticket')
        # 如果没有ticket，则直接跳转到登录
        if not ticket:
            return HttpResponseRedirect(reverse('user:login'))
        # 通过ticket获取user
        user = UserTicketModel.objects.filter(ticket=ticket).first()
        if not user:
            return HttpResponseRedirect(reverse('user:login'))
        # 判断过期时间
        if user.out_time.replace(tzinfo=None) < datetime.now():
            user.delete()
            return HttpResponseRedirect(reverse('user:login'))
        # 没有过期, 中间件赋值
        request.user = user.user

