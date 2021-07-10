import seaborn as sns
import matplotlib.pyplot as plt
from .data import nice_dict
from .utils import new_chart_filepath

class Grapher:
    """
    Holds display settings and renders charts.
    """

    def __init__(self, df):
        self.dataframe = df
        self.chart_filepath = ''

    def render_input(self, chart_type, x_axis, y_axis):
        if chart_type == 'scatter':
            return self.scatter(x_axis, y_axis)
        elif chart_type == 'dist':
            return self.dist(x_axis)

    def scatter(self, x_axis, y_axis):
        sns.scatterplot(data=self.dataframe, x=x_axis, y=y_axis)
        plt.xlabel(nice_dict[x_axis])
        plt.ylabel(nice_dict[y_axis])
        self.chart_filepath = new_chart_filepath()
        plt.savefig(self.chart_filepath)
        plt.clf()

    def dist(self, x_axis):
        sns.displot(self.dataframe, x=x_axis)
        plt.xlabel(nice_dict[x_axis])
        self.chart_filepath = new_chart_filepath()
        plt.savefig(self.chart_filepath)
        plt.clf()