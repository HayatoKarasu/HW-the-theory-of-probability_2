from matplotlib import pyplot as plt

plt.text(0.01, 0.9, "У нас 3 коробки:", fontsize=15)
plt.text(0.01, 0.8, "В первой: 3 красных и 1 зеленый шар", fontsize=15)
plt.text(0.01, 0.7, "Во второй: 2 красных и 3 зеленых", fontsize=15)
plt.text(0.01, 0.6, "В третьей: 3 красных шара", fontsize=15)
plt.text(0.01, 0.5, "Закрытыми глазами взяли один шар", fontsize=15)
plt.text(0.01, 0.4, "и он оказался красным.", fontsize=15)
plt.text(0.01, 0.3, "Расчитать вероятность для 1, 2, 3 коробки.", fontsize=15)
plt.text(0.01, 0.2, "Используем формулы:", fontsize=15)
form = r"$C_n^k = \frac{n!}{k!(n-k)!} ; P(A_i)=\frac{n_i}{N} ; P(B) = \sum_{i=1}^3 P(B|A_i)P(A_i)$"
plt.text(0.01, 0.1, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

form = r"$P(B|A_i) = p_i; P(A_i|B) = \frac{P(B|A_i)P(A_i)}{P(B)}$"
plt.text(0.01, 0.9, form, fontsize=15)
plt.text(0.01, 0.8, "Решение:", fontsize=15)
plt.text(0.01, 0.7, "Для начала узнаем вероятность попадания", fontsize=15)
plt.text(0.01, 0.6, "красного шара для каждой коробки:", fontsize=15)
form = r"$p_1 = \frac{C_3^1}{C_4^1} = \frac{3}{4}; p_2 = \frac{C_2^1}{C_5^1} = \frac{2}{5}; p_3 = \frac{C_3^1}{C_3^1} = 1$"
plt.text(0.01, 0.5, form, fontsize=15)
plt.text(0.01, 0.4, "Дальше вероятность для каждой коробки:", fontsize=15)
form = r"$P(A_1) = \frac{4}{12} = \frac{1}{3}; P(A_2) = \frac{5}{12}; P(A_3) = \frac{3}{12} = \frac{1}{4}$"
plt.text(0.01, 0.3, form, fontsize=15)
plt.text(0.01, 0.2, "Следом общую вероятность события:", fontsize=15)
form = r"$P(B) = \frac{3}{4} * \frac{1}{3} + \frac{2}{5} * \frac{5}{12} + \frac{1}{1} * \frac{1}{4} = \frac{1}{4} + \frac{1}{6} + \frac{1}{4} = \frac{2}{3}$"
plt.text(0.01, 0.1, form, fontsize=15)


fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, "Ну а теперь, имея все вероятности получим", fontsize=15)
plt.text(0.01, 0.8, "вероятность выпадения красного шара для", fontsize=15)
plt.text(0.01, 0.7, "каждой коробки:", fontsize=15)
form = r"$P(A_1|B) = \frac{1}{4} / \frac{2}{3} = \frac{3}{8} = (0,375*100) = $"
plt.text(0.01, 0.6, form, fontsize=15)
plt.text(0.01, 0.5, " = 37,5%", fontsize=15)
form = r"$P(A_2|B) = \frac{1}{6} / \frac{2}{3} = \frac{1}{4} = (0,25*100) = $"
plt.text(0.01, 0.4, form, fontsize=15)
plt.text(0.01, 0.3, " = 25%", fontsize=15)
form = r"$P(A_1|B) = \frac{1}{4} / \frac{2}{3} = \frac{3}{8} = (0,375*100) = $"
plt.text(0.01, 0.2, form, fontsize=15)
plt.text(0.01, 0.1, " = 37,5%", fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, "Очень интересный ответ!", fontsize=15)
plt.text(0.01, 0.8, "Получается что у нас для 1 и 3 коробки", fontsize=15)
plt.text(0.01, 0.7, "одинаковая вероятность, как для монеты", fontsize=15)
plt.text(0.01, 0.6, "50 на 50.", fontsize=15)
plt.text(0.01, 0.5, "А еще интересный момент, при расчете", fontsize=15)
plt.text(0.01, 0.4, "для первой коробки было замечено, что ", fontsize=15)
plt.text(0.01, 0.3, "вероятность выпадения 1 зеленого шара", fontsize=15)
plt.text(0.01, 0.2, "настолько мала, что она просто ", fontsize=15)
plt.text(0.01, 0.1, "растворилась в расчетах.", fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()