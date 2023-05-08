import matplotlib.pyplot as plt

inputs = [1, 2, 3, 4, 5]
squears= [1, 4, 9, 16, 25]

plt.style.use('_mpl-gallery')


def squeare_plot(ax):
    ax.plot(inputs,squears,linewidth=1, c='red')

    ax.set_xlabel('value', fontsize=14,loc='right')
    ax.set_ylabel('value\'s squeare', rotation='horizontal', loc='top', fontsize=14)
    ax.set_title('square', fontsize=20)
    ax.tick_params(axis='both', labelsize=12)
    ax.axis([1, 5, 0, 30])

fig, ax = plt.subplots(figsize=(10, 5),layout='constrained')
squeare_plot(ax)


plt.show()
