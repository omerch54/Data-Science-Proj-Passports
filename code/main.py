import os
import numpy as np

from sklearn.metrics import silhouette_score
from scraper import PassportIndexScraper, EducationRankingsScraper, ExportsScraper, ImportsScraper, \
    AverageIQScraper, LiteracyRateScraper, GDPPerCapitaScraper, \
    PASSPORT_INDEX_URL, EDUCATION_RANKINGS_URL, EXPORTS_URL, IMPORTS_URL
from preprocessor import Preprocessor
from models import HypothesisTester
from visualization import plot_clusters, plot_clusters_3d, plot_linear_regressions, plot_linear_2, plot_decision_boundary, plot_confusion_matrix


if __name__ == '__main__':
    output_dir = "./code/data_deliverable/data"
    web_scrapers = [
        ExportsScraper(EXPORTS_URL, f"{output_dir}/exports.csv"),
        ImportsScraper(IMPORTS_URL, f"{output_dir}/imports.csv"),
        PassportIndexScraper(PASSPORT_INDEX_URL, f"{output_dir}/passport_index.csv"),
        EducationRankingsScraper(EDUCATION_RANKINGS_URL, f"{output_dir}/education_rankings.csv"),
        AverageIQScraper(f"{output_dir}/countries_average_iq.csv"),
        LiteracyRateScraper(f"{output_dir}/countries_literacy_rate.csv"),
        GDPPerCapitaScraper(f"{output_dir}/countries_gdp.csv")
    ]
    for scraper in web_scrapers:
        try:
            if os.path.exists(scraper.save_path):
                scraper.load()
            else:
                scraper.scrape()
                scraper.save()
        except Exception as e:
            print(f"Error scraping {scraper.url} or using {scraper.save_path}: {e}")

    data = [(sc.data, sc.save_path.split("/")[-1]) for sc in web_scrapers]
    preprocessed_output_dir = "./code/data_deliverable/preprocessed_data"
    preprocessor = Preprocessor(data=data, data_dir=output_dir)
    preprocessed_data = preprocessor.preprocess(drop_years=np.arange(1950, 2010))
    preprocessor.save_preprocessed_data(save_dir=preprocessed_output_dir)

    joined_data = preprocessor.join_by_country()

    hypothesis_tester = HypothesisTester(joined_data)

    # 1. Test hypothesis 1
    ttest, pvalue = hypothesis_tester.test_hypothesis_1()
    print(f"Chi-squared test statistic: {ttest}, p-value: {pvalue}")

    # 2. Test hypothesis 2
    ttest, pvalue = hypothesis_tester.test_hypothesis_2()
    print(f"Two-sample t-test statistic: {ttest}, p-value: {pvalue}")

    # 3. Test hypothesis 3
    ttest, pvalue = hypothesis_tester.test_hypothesis_3()
    print(f"Two-sample t-test statistic: {ttest}, p-value: {pvalue}")

    # search for best features with all combinations of features
    feature_search_log = []
    feature_search_lin = []
    for n_classes in [2, 3, 4, 5]:
        for use_edu in [True, False]:
            for use_lit in [True, False]:
                for use_iq in [True, False]:
                    for use_gdp in [True, False]:
                        for use_impexp in [True, False]:
                            if not (use_edu or use_lit or use_iq or use_gdp or use_impexp):
                                continue
                            features_to_use = {
                                'use_edu': use_edu,
                                'use_lit': use_lit,
                                'use_iq': use_iq,
                                'use_gdp': use_gdp,
                                'use_impexp': use_impexp,
                                # 'n_clusters': 3,
                                'n_splits': 5,
                                'n_classes': n_classes,
                            }
                            _, accuracy = hypothesis_tester.predict_0(**features_to_use)
                            feature_search_log.append((features_to_use, accuracy))

                            _, accuracy = hypothesis_tester.predict_1(**features_to_use)
                            feature_search_lin.append((features_to_use, accuracy))
    feature_search_lin_1 = feature_search_lin.copy()
    feature_search_log.sort(key=lambda x: x[1], reverse=True)
    feature_search_lin.sort(key=lambda x: x[1], reverse=True)

    features_to_use = {
        'use_edu': True,
        'use_lit': True,
        'use_iq': True,
        'use_gdp': True,
        'use_impexp': False,
        'n_clusters': 3,
        'years_to_use': ['2022']
    }

    model, cluster_data, X = hypothesis_tester.predict_2(**features_to_use)

    plot_clusters(model, cluster_data, X)

    cluster_data.to_csv("./code/analysis_deliverable/results/cluster_data.csv", index=False)
    slh_score = silhouette_score(X, model.labels_)
    print(f"Silhouette score: {slh_score}")
    plot_clusters_3d(model, cluster_data, X)
    plot_linear_regressions(feature_search_lin_1)
    plot_linear_2(feature_search_lin_1)

    features_to_use = {
        'use_edu': True,
        'use_lit': True,
        'use_iq': False,
        'use_gdp': True,
        'use_impexp': False,
        'n_clusters': 3,
        'years_to_use': ['2022']
    }

    y_pred, y_ground, conf_matrix = hypothesis_tester.predict_3(**features_to_use)
    plot_confusion_matrix(conf_matrix)






