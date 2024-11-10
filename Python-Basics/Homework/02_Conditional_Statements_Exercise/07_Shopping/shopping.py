GPU_PRICE = 250
CPU_PERCENT = 0.35
RAM_PERCENT = 0.10

DISCOUNT = 0.15

budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

sum_gpu = GPU_PRICE * gpu_count
sum_cpu = (sum_gpu * CPU_PERCENT) * cpu_count
sum_ram = (sum_gpu * RAM_PERCENT) * ram_count

total_price =  sum_gpu + sum_cpu + sum_ram

if gpu_count > cpu_count:
    total_price -= total_price *  DISCOUNT

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(total_price - budget):.2f} leva more!")