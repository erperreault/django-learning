
import seaborn as sns
import matplotlib.pyplot as plt
from .data import test_chart_path

class Grapher:
    """
    Holds display settings and renders charts.
    """

    def __init__(self, df):
        self.dataframe = df

    def scatter(self, x_axis, y_axis):
        print(self.dataframe)
        sns.scatterplot(data=self.dataframe, x=x_axis, y=y_axis)
        plt.savefig(test_chart_path)
        plt.clf()
