import numpy as np
import matplotlib.pyplot as plt
data = [70, 10, 10, 10]
with plt.xkcd():
    plt.pie(data, labels=('В комментариях', 'В Ираке', 'В Сирии', 'В Афганистане'))
    plt.title('Где ведутся самые ожесточенные бои')
plt.show()