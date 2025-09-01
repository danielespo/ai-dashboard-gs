from prometheus_client import start_http_server, Gauge, Counter
import random
import time

# Create metrics
inference_latency = Gauge('inference_latency_microseconds', 'AI model inference latency in microseconds')
trading_signals = Counter('trading_signals_total', 'Total trading signals processed')
model_accuracy = Gauge('model_accuracy_percent', 'Current model accuracy percentage')

def generate_fake_metrics():
    while True:
        inference_latency.set(random.uniform(100, 2000))  # 100-2000 microseconds
        trading_signals.inc(random.randint(1, 10))
        model_accuracy.set(random.uniform(85, 99))
        time.sleep(5)

if __name__ == '__main__':
    start_http_server(8000)
    generate_fake_metrics()
