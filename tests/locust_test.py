from locust import HttpUser, task, between
from locust.user import wait_time


class PerfTest(HttpUser):
    wait_time = between(1, 5)

    @task
    def registerPerf(self):
        self.client.get(url="/")
        self.client.post(url="/showSummary", data={'email':'john@simplylift.co'})
        self.client.get(url="/book/Spring%20Festival/Simply%20Lift")       
        self.client.post(url="/purchasePlaces", data={'club':"Simply Lift", 'competition':"Fall Classic", 'places':5})
        self.client.get(url="/logout")
        self.client.get(url="/tab")
