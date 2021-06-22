
import seaborn as sns
import matplotlib.pyplot as plt

class Grapher:
    """
    Holds display settings and renders charts.
    """

    def __init__(self, df):
        self.dataframe = df

    def scatter(self, x_axis, y_axis):
        sns.scatterplot(data=self.dataframe, x=x_axis, y=y_axis)
        plt.savefig(f'viz/static/viz/test.png') # save as file > index.html
