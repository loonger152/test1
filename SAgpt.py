import numpy as np

def ackley(x):
    """Ackley 函数"""
    a = 20
    b = 0.2
    c = 2 * np.pi
    sum1 = np.sum(x**2)
    sum2 = np.sum(np.cos(c * x))
    n = len(x)
    return -a * np.exp(-b * np.sqrt(sum1 / n)) - np.exp(sum2 / n) + a + np.exp(1)

def sa(objective_function, initial_solution, temperature, cooling_rate, iterations):
    """模拟退火算法"""
    current_solution = initial_solution
    current_energy = objective_function(current_solution)

    for iteration in range(iterations):
        # 生成新解
        new_solution = current_solution + np.random.normal(0, 0.1, len(initial_solution))
        new_energy = objective_function(new_solution)

        # 接受新解的条件
        if new_energy < current_energy or np.random.rand() < np.exp((current_energy - new_energy) / temperature):
            current_solution = new_solution
            current_energy = new_energy

        # 降温
        temperature *= cooling_rate

    return current_solution, current_energy

# 设置初始参数
dimension = 20
initial_solution = np.random.rand(dimension)
initial_temperature = 1.0
cooling_rate = 0.99
iterations = 1000

# 调用模拟退火算法
result_solution, result_energy = sa(ackley, initial_solution, initial_temperature, cooling_rate, iterations)

print("最优解:", result_solution)
print("最优值:", result_energy)
