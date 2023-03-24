from locust import between, task
from locust.contrib.fasthttp import FastHttpUser

class NginxTaskSet(FastHttpUser):

    wait_time = between(1, 5) # each user wait between 1 and 5 seconds between evey task execution

    @task
    def load_contents(self):
        self.client.get("http://nginx")