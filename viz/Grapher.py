from os import nice
import seaborn as sns
import matplotlib.pyplot as plt
from .data import test_chart_path, nice_dict

class Grapher:
    """
    Holds display settings and renders charts.
    """

    def __init__(self, df):
        self.dataframe = df

    def scatter(self, x_axis, y_axis):
        sns.scatterplot(data=self.dataframe, x=x_axis, y=y_axis)
        plt.xlabel(nice_dict[x_axis])
        plt.ylabel(nice_dict[y_axis])
        plt.savefig(test_chart_path)
        plt.clf()
