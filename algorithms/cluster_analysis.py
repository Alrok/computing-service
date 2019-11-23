import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, normalize
from sklearn.cluster import KMeans
import time
import datetime
from math import sqrt

from models.db.user import UserModel


class ClusterAnalysis:
    def __init__(self):
        pass

    dataFrame = None
    X = None

    def get_cluster_user_ids(self, user_id):
        self.init_data_frame()
        self.normalize_data()

        pca = PCA(n_components=2)
        X_principal = pca.fit_transform(self.X)
        X_principal = pd.DataFrame(X_principal)
        X_principal.columns = ['a', 'b']

        wcss = self.calculate_wcss(X_principal)
        n = self.optimal_number_of_clusters(wcss)
        kmeans = KMeans(n_clusters=n, init='k-means++', max_iter=300, n_init=10, random_state=0)
        clusters = kmeans.fit_predict(X_principal)

        self.dataFrame['cluster'] = clusters

        d = self.dataFrame.to_dict('index')

        result = list()
        for index in d:
            if d[index]['cluster'] == d[user_id]['cluster']:
                result.append(index)

        return result

    def normalize_data(self):
        scaler = MinMaxScaler()
        self.X = scaler.fit_transform(self.dataFrame)
        self.X = normalize(self.X)

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

    def optimal_number_of_clusters(self, wcss):
        x1, y1 = 2, wcss[0]
        x2, y2 = 10, wcss[len(wcss) - 1]

        distances = []
        for i in range(len(wcss)):
            x0 = i + 2
            y0 = wcss[i]
            numerator = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
            denominator = sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
            distances.append(numerator / denominator)

        return distances.index(max(distances)) + 2

    def calculate_wcss(self, data):
        wcss = []
        for n in range(2, 21):
            kmeans = KMeans(n_clusters=n, init='k-means++', max_iter=300, n_init=10, random_state=0)
            kmeans.fit(X=data)
            wcss.append(kmeans.inertia_)

        return wcss
