from locust import HttpLocust,TaskSet,task
'''
# 定义用户行为
class UserBehavior(TaskSet):

	@task
	def baidu_page(self):
		self.client.get("/")
		
class WebsiteUser(HttpLocust):
	task_set=UserBehavior
	min_wait=3000
	max_wait=6000
'''
'''
# Web性能测试
class UserBehavior(TaskSet):

    def on_start(self):
        """
        on_start is called when a Locust start before any task is scheduled
        """
        self.login()

    def login(self):
        self.client.post("/login_action", {"username":"admin", "password":"admin123456"})

    @task(2)
    def event_manage(self):
        self.client.get("/event_manage/")

    @task(2)
    def guest_manage(self):
        self.client.get("/guest_manage/")

    @task(1)
    def search_manage(self):
        self.client.get("/search_phone/", params={"phone":"13800112451"})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
'''
!/usr/bin/python
# -*- coding:utf-8 -*-

from locust import HttpLocust, TaskSet, task
from random import randint

# Web接口测试
class UserBehavior(TaskSet):

    @task()
    def user_sign(self):
        number = randint(1, 3001)
        phone = 13800110000 + number
        str_phone = str(phone)
        self.client.post("/api/user_sign/", data={"eid":"1", "phone":str_phone})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0