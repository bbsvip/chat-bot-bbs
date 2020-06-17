# -*- coding: utf-8 -*-
from fbchat import log, Client
from fbchat.models import *
import getpass
import sys
sys.dont_write_bytecode=True
import importlib
importlib.reload(sys)
import os
os.environ['PYDEVD_USE_FRAME_EVAL'] = 'NO'
os.environ['PYTHONIOENCODING'] = 'UTF-8'

class AutoBot(Client):
    def onMessage(self, mid=None, author_id=None, message=None,message_object=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg={}):
        log.info('Đã nhận được tin nhắn từ {} với nội dung là: {}'.format(author_id, message))
        log.info('Thực hiện gửi message đến {}'.format(author_id))
        if self.uid != author_id:
            self.send(Message(text='Cừu đang bận chơi đồ....\n À nhầm chơi game :)\n Gấp thì gọi!'), thread_id=thread_id, thread_type=thread_type)

client = AutoBot('mr.bbs.noname', '@@@0331999Bbsvip')
client.listen()
