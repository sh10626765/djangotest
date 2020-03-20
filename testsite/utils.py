import pandas
import numpy

from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest


def get_list_max(_list):
    return numpy.max(_list)


def get_list_pct(_list, _percentage):
    return numpy.percentile(a=_list, q=_percentage)


def get_list_avg(_list):
    return numpy.mean(_list)


def get_list_min(_list):
    return numpy.min(_list)


def get_list_var(_list):
    return numpy.var(_list)


def get_list_std(_list):
    return numpy.std(_list)


class ExcelFileProcess(object):

    def __init__(self, file_name):
        """
        use file name and needed columns to initial an instance to process with excel files
        :param file_name:
        :param use_columns:
        """
        self.file_name = file_name
        self.dataframe = pandas.read_excel(file_name)

    def get_column_names(self):
        return [column_name for column_name in self.dataframe]

    def get_data(self):
        """
        get data from excel by rows
        :return: a list containing each row in dict (column names are keys)
        """
        materials = []

        for row in self.dataframe.iterrows():
            material = {}

            for column_name in self.get_column_names():
                material[column_name.replace('.', '').replace('$', '')] = row[1][column_name]

            materials.append(material)

        return materials

    def has_blank_cell(self):
        """
        dataframe.isnull() returns a tuple like ([ROW_INDEX], [COLUMN_INDEX]) of blank cells
        :return: True if blank cells in excel file, otherwise False
        """
        if 0 == numpy.where(self.dataframe.isnull())[0].size:
            return False

        return True

    def blank_cells(self):
        """
        dataframe.isnull() returns a tuple like ([ROW_INDEX], [COLUMN_INDEX]) of blank cells
        :return: a list containing locations of blank cells.
                For example: if the returned list is [(0, 9), (4, 4), (13, 8), (17, 13)]
                that means row[0],column[9] in the dataframe is blank
        """
        blank_matrix = numpy.where(self.dataframe.isnull())
        return list(zip(blank_matrix[0], blank_matrix[1]))

    def get_column_average(self):
        """
        get every column's average value of the dataframe
        :return: a dict (keys are column names)
        """
        return self.dataframe.mean().to_dict()

    def get_column_max(self):
        """
        get every column's max value of the dataframe
        :return: a dict (keys are column names)
        """
        return self.dataframe.max().to_dict()

    def get_column_quantile(self, percentage):
        """
        get every column's quantile value of the dataframe
        :param percentage:
        :return:
        """
        return self.dataframe.quantile(q=percentage,numeric_only=True).to_dict()

    def get_column_median(self):
        """
        get every column's median value of the dataframe
        :return: a dict (keys are column names)
        """
        return self.dataframe.median().to_dict()

    def get_column_min(self):
        """
        get every column's min value of the dataframe
        :return: a dict (keys are column names)
        """
        return self.dataframe.min().to_dict()

    def get_column_var(self):
        """
        :return:
        """
        return self.dataframe.var().to_dict()

    def get_column_std(self):
        """
        :return:
        """
        return self.dataframe.std().to_dict()

    def get_column_mad(self):
        """
        :return:
        """
        return self.dataframe.mad().to_dict()

    def get_column_skew(self):
        """
        :return:
        """
        return self.dataframe.skew().to_dict()

    def get_column_kurt(self):
        """
        :return:
        """
        return self.dataframe.kurt().to_dict()

    def get_outlier_index_boxplot(self, column_index):
        """
        this func will find the abnormal values over a column through the given column name of a self.dataframe
        :return: the abnormal values' indexes in the column
        """
        value_series = self.dataframe.iloc[:, column_index]
        value_q1 = value_series.quantile(q=0.25)
        value_q3 = value_series.quantile(q=0.75)
        value_iqr = value_q3 - value_q1
        value_upper = value_q3 + value_iqr * 1.5
        value_lower = value_q1 - value_iqr * 1.5

        res = []
        for idx, val in value_series.items():
            if val > value_upper or val < value_lower:
                res.append(idx)

        return res

    def get_outlier_index_LOF(self):
        clf = LocalOutlierFactor(n_neighbors=self.dataframe.shape[0] // 2, contamination=0.1)
        # data = self.dataframe.values
        labels = clf.fit_predict(self.dataframe.iloc[:, 4:])
        # scores = clf.negative_outlier_factor_
        res = []
        for i in range(len(labels)):
            if -1 == labels[i]:
                res.append(i)
        return res

    def get_outlier_index_IF(self):
        clf = IsolationForest(n_estimators=self.dataframe.shape[0] * 2, contamination=0.1)
        labels = clf.fit_predict(self.dataframe.iloc[:, 4:])
        res = []
        for i in range(len(labels)):
            if -1 == labels[i]:
                res.append(i)
        return res