import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.cluster import KMeans
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix

### Statistical Tests ###
# 1. Education levels and passport index are not independent using chi-squared test
# 2. High average literacy rate and low average literacy rate countries have
# different passport index using two-sample t-test
# 3. There is a significant difference in passport index between countries with
# high GDP per capita and low GDP per capita using two-sample t-test

# Note, 'high' or 'low' means above or below the average value

### Machine Learning ###
# 1. Passport index using logistic regression
# 2. Cluster countries using KMeans


class HypothesisTester:

    def __init__(self, data, passport_index_year=2022):
        # get data for the year of interest
        self.data = data[data["Year"] == passport_index_year]

    def test_hypothesis_1(self):
        # chi-squared test to assess the independence between education levels and passport index
        data = self.data[['Education Index', 'Number of Visa-Free Destinations']]
        data = data.dropna()
        contingency_table = pd.crosstab(data['Education Index'], data['Number of Visa-Free Destinations'])
        chi2, p_value, _, _ = chi2_contingency(contingency_table)

        return chi2, p_value

    def test_hypothesis_2(self):
        # two-sample t-test to compare passport index between high and low average literacy rate countries
        data = self.data[['LiteracyRateAllGenders', 'Number of Visa-Free Destinations']]
        data = data.dropna()
        mean_lit_rate = data['LiteracyRateAllGenders'].mean()
        high_literacy = data[data['LiteracyRateAllGenders'] > mean_lit_rate]['Number of Visa-Free Destinations']
        low_literacy = data[data['LiteracyRateAllGenders'] <= mean_lit_rate]['Number of Visa-Free Destinations']
        t_statistic, p_value = ttest_ind(high_literacy, low_literacy)

        return t_statistic, p_value

    def test_hypothesis_3(self):
        # two-sample t-test to compare passport index between high and low GDP per capita countries
        data = self.data[['2022', 'Number of Visa-Free Destinations']]
        data = data.dropna()
        mean_gdp = data['2022'].mean()
        high_gdp = data[data['2022'] > mean_gdp]['Number of Visa-Free Destinations']
        low_gdp = data[data['2022'] <= mean_gdp]['Number of Visa-Free Destinations']
        t_statistic, p_value = ttest_ind(high_gdp, low_gdp)

        return t_statistic, p_value

    def parse_features(self, **kwargs):
        years_to_use = kwargs.get('years_to_use', ['2022', '2021', '2020', '2019'])
        # parse features for machine learning
        features = [
            # education
            'Education Index',
            # literacy
            'LiteracyRateAllGenders',
            # iq
            'AverageIQ_ICI2017Score',
            # gdp
            *years_to_use,
            # imports and exports
            'Exports',
            'Imports'
        ]

        use_edu = kwargs.get('use_edu', True)
        use_lit = kwargs.get('use_lit', True)
        use_iq = kwargs.get('use_iq', True)
        use_gdp = kwargs.get('use_gdp', True)
        use_impexp = kwargs.get('use_impexp', True)

        if not use_edu:
            features.remove('Education Index')
        if not use_lit:
            features.remove('LiteracyRateAllGenders')
        if not use_iq:
            features.remove('AverageIQ_ICI2017Score')
        if not use_gdp:
            for year in years_to_use:
                features.remove(year)
        if not use_impexp:
            features.remove('Exports')
            features.remove('Imports')

        return features

    def predict_0(self, **kwargs):
        # predict passport index using logistic regression
        features = self.parse_features(**kwargs)
        data = self.data[features + ['Number of Visa-Free Destinations']]
        data = data.dropna()

        X = data[features]
        y = data['Number of Visa-Free Destinations']

        # divide y into 4 classes for classification, rather than almost 200 classes
        n_classes = kwargs.get('n_classes', 4)
        y = pd.qcut(y, n_classes, labels=False)

        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        model = LogisticRegression()

        n_splits = kwargs.get('n_splits', 5)
        kf = KFold(n_splits=n_splits, shuffle=True)
        scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')
        val_accuracy = scores.mean()

        model.fit(X, y)

        return model, val_accuracy

    def predict_1(self, **kwargs):
        # predict passport index using linear regression
        features = self.parse_features(**kwargs)
        data = self.data[features + ['Number of Visa-Free Destinations']]
        data = data.dropna()

        X = data[features]
        y = data['Number of Visa-Free Destinations']

        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        model = LinearRegression()

        n_splits = kwargs.get('n_splits', 5)
        kf = KFold(n_splits=n_splits, shuffle=True)
        # using default scorer
        scores = cross_val_score(model, X, y, cv=kf, scoring=None)
        val_accuracy = scores.mean()

        return model, val_accuracy

    def predict_2(self, **kwargs):
        # cluster countries using KMeans
        features = self.parse_features(**kwargs)
        data = self.data[features + ['Number of Visa-Free Destinations']]
        data = data.dropna()

        X = data[features]

        scaler = MinMaxScaler()
        X = scaler.fit_transform(X)

        n_clusters = kwargs.get('n_clusters', 3)

        model = KMeans(n_clusters=n_clusters)

        model.fit(X)

        # get average data for each cluster, including the number of visa-free destinations
        cluster_data = data.copy()
        cluster_data['Cluster'] = model.predict(X)
        cluster_data = cluster_data.groupby('Cluster').mean()

        return model, cluster_data, X
    
    def predict_3(self, **kwargs):
        features = self.parse_features(**kwargs)
        data = self.data[features + ['Number of Visa-Free Destinations']]
        data = data.dropna()

        X = data[features]
        y = data['Number of Visa-Free Destinations']

        # divide y into 4 classes for classification, rather than almost 200 classes
        n_classes = kwargs.get('n_classes', 3)
        y = pd.qcut(y, n_classes, labels=False)

        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        model = LogisticRegression()

        n_splits = kwargs.get('n_splits', 5)
        kf = KFold(n_splits=n_splits, shuffle=True)
        scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')
        val_accuracy = scores.mean()

        model.fit(X, y)
        y_preds = cross_val_predict(model, X, y, cv=kf)


        conf_matrix = confusion_matrix(y, y_preds)
        #plot conf_matrix
        return y_preds, y, conf_matrix



