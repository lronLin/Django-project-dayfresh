
import random
from datetime import datetime


def get_ticket():
    ticket = ''
    s = 'abcdefghijkrmnopqrstuvwxyz1234567890'
    for i in range(28):
        r_num = random.choice(s)
        ticket += r_num
    return ticket


# 获取订单数量
def get_order_num():
    num = ''
    s = '1234567890abcdefghijklmnopqefdf'
    for j in range(8):
        num += random.choice(s)
    order_time = datetime.now().strftime('%Y%m%d%H%M%S')
    return order_time + num