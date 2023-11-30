import requests
import time 
import os

class LoadGenerator:

    def __init__(self,target,frequency):
        self.target = target
        self.frequency = frequency
        self.total_request = 0
        self.total_request_failure = 0
        self.total_response_time = 0
        self.count = 0

    def generator_load(self):
        for _ in range(20):
            self.count += 1
            start_time = time.time()
            print(start_time)
            try:
                response = requests.get(self.target,timeout=10)
                response.raise_for_status()
                print(response)
                self.total_response_time += time.time() - start_time
            except requests.exceptions.RequestException:
                self.total_request_failure += 1
            finally:
                self.total_request += 1
                time.sleep(1 / self.frequency)

    def print_results(self):
        avg_response_time = self.total_response_time / self.total_request if self.total_request else 0
        print(f"Average Response time: {avg_response_time:.2f} seconds")
        print(f"Total Failure: {self.total_request_failure}")
        return {"total_request": self.total_request_failure,"avg_response": avg_response_time,"Number_Of_Requests": self.count}

if __name__ == "__main__":
    target = os.getenv("TARGET", "http://localhost:5000/primecheck")
    frequency = float(os.getenv("FREQUENCY",10))

    load_generator = LoadGenerator(
        target,frequency
    )
    load_generator.generator_load()
    load_generator.print_results()

        