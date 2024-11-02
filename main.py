import torch
from multiprocessing import Pool, cpu_count, Process


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, (int(n ** 0.5) + 1)):
        if n % i == 0:
            return False
    print(f'{n} is prime')


def gpu_task():
    a = torch.randn(1000, 1000, device='cuda')
    b = torch.randn(1000, 1000, device='cuda')

    while True:
        torch.matmul(a, b)


def infinite_number_generator():
    # Start at high number to avoid reduce downtime
    n = 1e14
    while True:
        yield n
        n += 1


if __name__ == '__main__':
    # Start GPU task
    gpu_process = Process(target=gpu_task)
    gpu_process.start()

    # Create a pool of max amount of processes
    with Pool(cpu_count()) as pool:
        for _ in pool.imap_unordered(is_prime, infinite_number_generator()):
            pass
