import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
from sklearn.metrics import confusion_matrix

# plot clusters and display mean values of centroids
# cluster_data has 3 centroids with 5 features each
# data has 4 features, it does not have the passport index
def plot_clusters(model, cluster_data, data):
    data = pd.DataFrame(data, columns=[
        'edu',
        'lit',
        'iq',
        'gdp'
    ])

    pca = PCA(n_components=2)

    reduced_data = pca.fit_transform(data)

    reduced_df = pd.DataFrame(reduced_data, index=data.index, columns=['PC1', 'PC2'])
    reduced_df['cluster'] = model.labels_
    centers_reduced = pca.transform(model.cluster_centers_)
    centers_reduced_df = pd.DataFrame(centers_reduced, columns=['PC1', 'PC2'])

    fig, ax = plt.subplots(figsize=(10, 10))

    # label each centroid with mean feature values as legend
    legend_labels = []
    for i in range(len(centers_reduced_df)):
        label = (f"Cluster {i}\n"
                 f"edu: {cluster_data.loc[i, 'Education Index']:.2f}\n"
                 f"lit: {cluster_data.loc[i, 'LiteracyRateAllGenders']:.2f}\n"
                 f"iq: {cluster_data.loc[i, 'AverageIQ_ICI2017Score']:.2f}\n"
                 f"gdp: {cluster_data.loc[i, '2022']:.2f}\n"
                 f"visa-free countries: {cluster_data.loc[i, 'Number of Visa-Free Destinations']:.2f}")
        legend_labels.append(label)

    sns.scatterplot(data=reduced_df, x='PC1', y='PC2', hue='cluster', ax=ax)
    sns.scatterplot(data=centers_reduced_df, x='PC1', y='PC2', color='red', ax=ax)

    ax.legend(legend_labels, title='Cluster Information', fontsize=10, title_fontsize='13', loc='upper left')

    plt.show()

def plot_clusters_3d(model, cluster_data, data):
    data = pd.DataFrame(data, columns=[
        'edu',
        'lit',
        'iq',
        'gdp'
    ])

    pca = PCA(n_components=3)

    reduced_data = pca.fit_transform(data)

    reduced_df = pd.DataFrame(reduced_data, index=data.index, columns=['PC1', 'PC2', 'PC3'])
    reduced_df['cluster'] = model.labels_
    centers_reduced = pca.transform(model.cluster_centers_)
    centers_reduced_df = pd.DataFrame(centers_reduced, columns=['PC1', 'PC2', 'PC3'])

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # label each centroid with mean feature values as legend
    legend_labels = []
    for i in range(len(centers_reduced_df)):
        label = (f"Cluster {i}\n"
                 f"edu: {cluster_data.loc[i, 'Education Index']:.2f}\n"
                 f"lit: {cluster_data.loc[i, 'LiteracyRateAllGenders']:.2f}\n"
                 f"iq: {cluster_data.loc[i, 'AverageIQ_ICI2017Score']:.2f}\n"
                 f"gdp: {cluster_data.loc[i, '2022']:.2f}\n"
                 f"visa-free countries: {cluster_data.loc[i, 'Number of Visa-Free Destinations']:.2f}")
        legend_labels.append(label)

    ax.scatter(reduced_df['PC1'], reduced_df['PC2'], reduced_df['PC3'], c=reduced_df['cluster'], cmap='viridis')
    ax.scatter(centers_reduced_df['PC1'], centers_reduced_df['PC2'], centers_reduced_df['PC3'], c='red')

    ax.legend(legend_labels, title='Cluster Information', fontsize=10, title_fontsize='13', loc='upper left')

    plt.show()
#feature_search_lin.append((features_to_use, accuracy))
def plot_linear_regressions(feature_search_lin):
    # plot linear regression results
    # print(feature_search_lin)
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.set_title("Linear Regression Results")
    ax.set_xlabel("Number of Features")
    ax.set_ylabel("Scores")
    unique_feature_counts = set([len([x for x in i.values() if x is True]) for i, _ in feature_search_lin])
    dict = {}
    for total in feature_search_lin:
        i, accuracy = total[0],total[1]
        i = len([x for x in i.values() if x is True])
        if i not in dict:
            dict[i] = [accuracy]
        else:
            dict[i].append(accuracy)
    for key in dict:
        dict[key] = sum(dict[key])/len(dict[key])
    #bar plot
    ax.bar(dict.keys(), dict.values())

    #for total in feature_search_lin:
    #     i, accuracy = total[0], total[1]
    #     i = len([x for x in i.values() if x is True])
    #     ax.plot(i, accuracy, 'o')
    plt.show()

def plot_linear_2(feature_search_lin):
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.set_title("Linear Regression Results")
    ax.set_xlabel("Number of Features")
    ax.set_ylabel("Scores")
    unique_features = list(feature_search_lin[0][0].keys())
    print(unique_features)
    dict = {}
    for i in feature_search_lin:
        features_used = list([a for a, b in i[0].items() if b is True])
        for j in features_used:
            if j not in dict:
                dict[j] = [i[1]]
            else:
                dict[j].append(i[1])
    for key in dict:
        dict[key] = sum(dict[key]) / len(dict[key])
    # bar plot
    print(dict)
    ax.bar(dict.keys(), dict.values())
    
    plt.show()

def plot_decision_boundary(model, X, y):
    # plot decision boundary
    h = .02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', s=20)
    plt.show()
# classes 2 -> high_passport_index, 1 -> medium_passport_index, 0 -> low_passport_index
def plot_confusion_matrix(conf_matrix):
    # smaller 
    plt.figure(figsize=(10, 10))
    sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='g', xticklabels=['low_passport_index', 'medium_passport_index', 'high_passport_index'], yticklabels=['low_passport_index', 'medium_passport_index', 'high_passport_index'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()


