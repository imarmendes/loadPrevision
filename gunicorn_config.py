import multiprocessing

bind = '0.0.0.0:8000'  # Endereço e porta onde o Gunicorn irá ouvir

workers = multiprocessing.cpu_count() * 2 + 1  # Número de processos de trabalho
worker_class = 'sync'  # Tipo de worker
timeout = 30  # Tempo limite de resposta em segundos
