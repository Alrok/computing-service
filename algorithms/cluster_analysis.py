import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import time
import datetime

from models.db.user import UserModel


class ClusterAnalysis:
    def __init__(self):
        pass

    dataFrame = None
    X = None

    def get_cluster_user_ids(self, user_id):
        self.init_data_frame()
        self.normalize_data()

        n_clusters = 3
        km = KMeans(n_clusters=n_clusters)

        # fit & predict clusters
        clusters = km.fit_predict(self.X)
        self.dataFrame['cluster'] = clusters

        d = self.dataFrame.to_dict('index')

        result = list()
        for index in d:
            if d[index]['cluster'] == d[user_id]['cluster']:
                result.append(index)

        return result

    def normalize_data(self):
        scaler = StandardScaler()
        self.X = scaler.fit_transform(self.dataFrame)

    def init_data_frame(self):
        data_set = dict()
        users = UserModel.query.all()

        for user in users:
            data_set[user.id] = [user.gender, time.mktime(
                datetime.datetime.strptime(user.dateOfBirth, "%d/%m/%Y").timetuple())]

        self.dataFrame = pd.DataFrame.from_dict(data_set, orient='index', columns=['gender', 'dateOfBirth'])

        us = list()
        for u in users:
            us.append(u.json())
        return us
