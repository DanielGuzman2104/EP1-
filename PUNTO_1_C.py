import numpy as np
import matplotlib.pyplot as plt


R0 = 100  
alpha = 0.00385  # Coeficiente

T = np.arange(-200, 200, 1)
R = R0 * (1 + alpha * T)


#////////////////////PLOTEO///////////////// 

plt.legend()
plt.show()
plt.figure(figsize=(10, 5))
plt.plot(T, R, label="PT100", color="RED", linewidth= 3)
plt.title("PT100")
plt.xlabel("T (°C)")
plt.ylabel("R(Ohmios)")
plt.grid(True)
