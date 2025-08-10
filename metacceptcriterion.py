from math import exp 
import matplotlib.pyplot as plt
iterations = 100
initial_temp = 10
iters = list(range(iterations))
temperature = [initial_temp / (i+1)for i in iters]
deltas = [0.01, 0.1,1.0]
for d in deltas:
    acceptance_probs = [exp(-d / t) for t in temperature]
    plt.plot(iters, acceptance_probs, label=f"ΔE={d:.2f}")
plt.title("Metropolis Acceptance Probability")
plt.xlabel("Iteration")
plt.ylabel("P(accept worse move)")
plt.legend()
plt.grid(True)
plt.show()