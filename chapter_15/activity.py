import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')  
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
mental_health_scores = [5, 4, 3, 2, 1, 1, 1]


fig, ax = plt.subplots(figsize=(12, 6))


ax.plot(days, mental_health_scores, 'o-', color='red', linewidth=2.5, label='Mental Health Declining')

ax.set(ylim=(0, 6), yticks=np.arange(0, 7, 1))

ax.set_title('Mental Health Trends Over the Week', fontsize=20, color='darkblue', weight='bold')
ax.set_xlabel('Days of the Week', fontsize=16, weight='bold')
ax.set_ylabel('Mental Health Score', fontsize=16, weight='bold')


ax.grid(True, linestyle='--', alpha=0.6)


ax.legend(loc='upper right', fontsize=12)


plt.show()