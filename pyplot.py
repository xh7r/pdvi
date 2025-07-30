import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


class Pyplot:
    """
    Realizing the visualization of various graphs by pyplot
    @Author: Jaylen
    @Date: 2025.06.29
    """

    def __init__(self, data_path=''):
        self.__data_path = data_path
        self.__data = self.__read_data()

        plt.figure(figsize=(10, 6), dpi=120)
        plt.grid(axis='y', linestyle='--', alpha=0.4)

    def __read_data(self):
        """
        read data file according to suffix xlsx or csv
        """

        # Check file exist
        if not os.path.exists(self.__data_path):
            raise FileNotFoundError(f"cant find: {self.__data_path}")

        # get file extension
        ext = os.path.splitext(self.__data_path)[1].lower()

        if ext == '.xlsx':
            return pd.read_excel(self.__data_path)
        elif ext == '.csv':
            return pd.read_csv(self.__data_path)
        else:
            raise ValueError(f"We just support the extension of xlsx and csv.")

    def get_data(self):
        """
        Get the private attribute self.__data
        :return: self.__data
        """
        return self.__data

    def bar(self, title='title', x_label='x', y_label='y', fontsize=20):
        """
        Drawing bar graph: Two columns of data
        :param x_field:
        :param y_field:
        :param title:
        :param x_label:
        :param y_label:
        :param fontsize:
        :return: No return
        """
        x = self.__data['x']
        y = self.__data['y']

        bars = plt.bar(x, y, color=plt.cm.PuBu(np.linspace(0.4, 0.8, len(x))), edgecolor='black')

        plt.title(title, fontsize=fontsize, fontweight='bold')
        plt.xlabel(x_label, fontsize=fontsize)
        plt.ylabel(y_label, fontsize=fontsize)

        for bar in bars:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), int(bar.get_height()), ha='center',
                     va='bottom',
                     fontsize=fontsize - 5)
        plt.tight_layout()
        plt.show()

    def line(self):
        pass

    def heatmap(self):
        pass

    def scatter(self):
        pass

    def pie(self):
        pass

    def box(self):
        pass

    def histogram(self):
        pass

    def buble(self):
        pass

    def stacked_bar(self):
        pass

    def violin(self):
        pass

    def facet_hist(self):
        pass

    def kde(self):
        pass
