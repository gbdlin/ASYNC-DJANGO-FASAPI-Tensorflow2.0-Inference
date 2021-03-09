from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(0.2, 1)

    @task
    def on_start(self):
        self.client.post(
            "/api/predict",
            files={
                "files": ("cat.jpg", open("SampleImages/cat.jpg", "rb"), "image/jpeg")
            },
        )
