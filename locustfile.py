from locust import HttpUser, task, between, LoadTestShape

class MyUser(HttpUser):
    wait_time=between(1,2)

    @task
    def submit_form(self):
        # Enviar el formulario con los campos de nombre, correo electrónico, número de teléfono y mensaje
        response=self.client.post("http://wordpress1:80", {
            "name-1": "Miguel Paredes",
            "email-1": "miguel.paredes@example.com",
            "phone-1": "0987654321",
            "textarea-1": "Hola, este es un mensaje de prueba"
        })

class StresstestShape(LoadTestShape):
    stages = [
        {"duration": 15, "users": 10, "spawn_rate": 1},
        # {"duration": 30, "users": 15, "spawn_rate": 1},
        # {"duration": 45, "users": 20, "spawn_rate": 1},
        # {"duration": 60, "users": 25, "spawn_rate": 1}
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None