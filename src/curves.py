from matplotlib import pyplot as plt


def dark_style():
    # style
    plt.style.use("seaborn-dark")
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#151515'  # bluish dark grey
    for param in ['text.color', 'xtick.color', 'grid.color', 'ytick.color', 'axes.labelcolor']:
        plt.rcParams[param] = 'white'  # very light grey

    plt.grid(color='#2A3459')  # bluish dark grey, but slightly lighter than background

    # ==========================


def neon_curve(x, y, y2, y3):
    n_lines = 5
    diff_linewidth = 0.5
    alpha_value = 0.03

    for n in range(1, n_lines + 1):
        plt.plot(x, y,
                 linewidth=2 + (diff_linewidth * n),
                 alpha=alpha_value,
                 color='#08F7FE')

        plt.plot(x, y2,
                 linewidth=2 + (diff_linewidth * n),
                 alpha=alpha_value,
                 color='#00D8FF')

        plt.plot(x, y3,
                 linewidth=2 + (diff_linewidth * n),
                 alpha=alpha_value,
                 color='#23FF00')


class Curve:

    def __init__(self, title, xlabel, ylabel, labels):
        self.title = title
        self.labels = labels
        self.xlabel = xlabel
        self.ylabel = ylabel
        dark_style()

    def plot_data(self, x, y, y2, y3, isError):
        plt.plot(x, y, label=self.labels[0], color='#FF31DD')
        plt.plot(x, y2, label=self.labels[1], color='#00D8FF')
        plt.plot(x, y3, label=self.labels[2], color='#23FF00')

        plt.legend(facecolor="black", frameon=True)

        plt.title(self.title, fontsize=15, style="italic")
        plt.xlabel(self.xlabel, loc='right', fontsize=10)
        plt.ylabel(self.ylabel, loc='top', fontsize=10)
        neon_curve(x, y, y2, y3)

        plt.grid(which='both', b=True, color="0.5")

        plt.grid(which='minor', b=True, color="0.2", alpha=0.5)

        plt.show()
