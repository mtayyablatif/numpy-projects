import numpy as np

rolls = np.random.choice([1, 2, 3, 4, 5, 6], size=10000)

for n in [10, 100, 1000, 10000]:
    subset = rolls[:n]
    prob_of_six = np.mean(subset == 6)
    print(f"Trials={n}, P(rolling 6)={prob_of_six:.4f}")
