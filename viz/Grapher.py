import seaborn as sns
import matplotlib.pyplot as plt
import os
import random
from .data import nice_dict, image_directory

class Grapher:
    def __init__(self, df):
        self.dataframe = df
        sns.set(rc={
            'axes.facecolor':'#282828', 
            'figure.facecolor':'#282828', 
            'axes.labelcolor': 'white',
            'xtick.color':'white',
            'ytick.color':'white',
            })

    def set_chart_type(self, chart_type, x_axis, y_axis):
        """Call the appropriate method for desired chart type."""
        if chart_type == 'scatter':
            return self.scatter(x_axis, y_axis)
        elif chart_type == 'cat':
            return self.cat(x_axis, y_axis)
        elif chart_type == 'dist':
            return self.dist(x_axis)

    def render_chart(self):
        """Save chart to /viz/static/viz"""
        plt.tight_layout()
        self.chart_filepath = self.new_chart_filepath()
        plt.savefig(self.chart_filepath)
        plt.clf()

    def scatter(self, x_axis, y_axis):
        sns.scatterplot(data=self.dataframe, x=x_axis, y=y_axis)
        plt.xlabel(nice_dict[x_axis])
        plt.ylabel(nice_dict[y_axis])
        self.render_chart()

    def cat(self, x_axis, y_axis):
        sns.catplot(data=self.dataframe, x=x_axis, y=y_axis)
        plt.xlabel(nice_dict[x_axis])
        plt.xticks(rotation=45)
        plt.ylabel(nice_dict[y_axis])
        self.render_chart()

    def dist(self, x_axis):
        sns.displot(self.dataframe, x=x_axis)
        plt.xlabel(nice_dict[x_axis])
        self.render_chart()

    def new_chart_filepath(self):
        """Generate a random key name to save chart."""
        img_dir = os.listdir(image_directory)
        keys = [int(file.split('.')[0]) for file in img_dir] # get the key without file extension
        filename = random.randint(1000000,9999999)

        while filename in keys:
            filename = random.randint(1000000,9999999)
            
        return image_directory + str(filename) + '.jpg'