from locust import between, task
from locust.contrib.fasthttp import FastHttpUser

class NginxTaskSet(FastHttpUser):

    wait_time = between(1, 5)

    @task
    def load_contents(self):
        self.client.get("http://nginx")