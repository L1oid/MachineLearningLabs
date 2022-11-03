import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('iris')  # загрузка датасета iris
sb.distplot(df['petal_length'])  # отрисовка по столбцу petal_length
plt.show()  # вывод

df = sb.load_dataset('iris')
sb.distplot(df['petal_length'], hist_kws={"alpha": 1})
plt.show()
