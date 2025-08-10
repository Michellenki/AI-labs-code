import matplotlib.pyplot as plt

# 1. Total number of iterations and initial temperature
iterations = 100
initial_temp = 10

# 2. Compute temperature schedule (exponential decay)
iters = list(range(iterations))
temperatures = [initial_temp * 0.95 ** i for i in iters]  # 0.95 is the cooling factor

# 3. Plot
plt.plot(iters, temperatures, color='orange')
plt.title("Temperature Decay over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()