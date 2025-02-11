For the Hypothesis Testing Component:

**Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s)
did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model?
Did you have to clean or restructure your data? What is your interpretation of the results? Do you accept or deny the
hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you
got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the
results?**


**FIRST HYPOTHESIS TEST**
For the first hypothesis test, we used a chi squared test, because we were interested in seeing if there is a 
relationship between education levels and passport index. A chi squared test made sense here because a chi-squared
independence test is used to test the statistical relationship between two categorical variables. For the data, we got 
the relevant columns of the data. In this context, relevant means that we picked the columns named “Education Index” 
and “number of visa-free destinations”. Later, we dropped the rows that had a null entry in those columns. The 𝑝-value 
for the above test is more than 0.05 (0.8878055302539459), so we fail to reject the null hypothesis and can't accept the 
alternate hypothesis which is: there is no significant association between education levels and the number of visa-free 
destinations. This is the approach we used for all the tests and the models, so we would not need to drop rows when we 
actually don't use a certain column. We select the columns we are interested in, and then drop rows when we find empty 
values only in those columns. For example, if we are not using the 'GDP' column, an empty value in that column would not 
result in the loss of a row.


**SECOND HYPOTHESIS TEST**


We used a two sample t test for this hypothesis test, because we wanted to compare passport index between high and low 
average literacy rate countries. We use a two sample t test when we want to compare a variable between two groups. 
In Hypothesis Test 2, since the p-value is much smaller than 0.05 (3.4945857262692777e-14), we reject the null 
hypothesis. This suggests that there is a significant difference in the number of visa-free destinations between 
countries with high and low literacy rates. For the data, we selected the "LiteracyRateAllGenders" and "Number of 
Visa-Free Destinations" columns, and again, we dropped empty rows. Then, we calculated the mean literacy rate from the 
data, and created two samples with passport strength when literacy rates are high/low. We identified countries with 
literacy rates less than the mean with low literacy rates, and ones with literacy rates higher than the mean high.


**THIRD HYPOTHESIS TEST**


We used a two sample t test for this hypothesis test, because we wanted to compare passport index between high and low 
GDP per capita countries. We use a two sample t test when we want to compare a variable between two groups. In 
Hypothesis Test 3, the p-value is much smaller than 0.05 (4.413583676028024e-23), leading to the rejection of the null 
hypothesis. This indicates that there is a significant difference in the number of visa-free destinations between 
countries with high and low GDP per capita, which is important for our analysis. This is also what we had thought. 
Countries with higher GDP have “a higher hand” in foreign relations, allowing their citizens to visit other countries. 
For the data, we selected "2022" (indicator of GDP per capita in the year 2022) and "Number of Visa-Free Destinations" 
columns. Then, similar to what we did for the second hypothesis, we calculated the mean GDP, and classified GDP values 
as high or low based on whether they are higher or lower than the mean. We formed two sample sets with passport 
strengths from high and low GDP countries, and performed the hypothesis test.


**Did you find the results corresponded with your initial belief in the data? If yes/no, why do you think this was the
case? Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have
been used? Was the data adequate for your analysis? If not, what aspects of the data were problematic and how could you
have remedied that?**


**FIRST HYPOTHESIS TEST**
For the first hypothesis test, the results didn’t correspond with our initial belief of the data, because we had thought 
that there would definitely be a relationship between education levels and passport index. The reason why the results 
show us this might be because there are a lot of omitted variables in the data collection process for the education 
levels. The way education is determined for a country might not be the same for another country, etc. We believe that 
the tools we chose for the analysis were appropriate. A chi squared test made sense here because a chi-squared 
independence test is used to test the statistical relationship between two categorical variables. The data had some 
null entries, so we had to drop some of the rows. Also, we assumed that because in some rows the years weren’t matching, 
the data education levels didn’t change that much across the years. We could have remedied that by grouping across 
years, but we would have had much less data points. 


**SECOND HYPOTHESIS TEST**
For the second hypothesis test, the results did correspond with our initial belief of the data, because we thought that 
there is a significant difference in the number of visa-free destinations between countries with high and low literacy 
rates. The reason why this tool was appropriate is because we want to compare a variable between two groups. The data 
had some null entries, so we had to drop some of the rows. Also, we assumed that because in some rows the years weren’t 
matching, the data literacy rates didn’t change that much across the years. We could have remedied that by grouping 
across years, but we would have had much less data points. 


**THIRD HYPOTHESIS TEST**


For the second hypothesis test, the results did correspond with our initial belief of the data, because we thought that 
there is a significant difference in the number of visa-free destinations between countries with high and low GDP per 
capita. The reason why this tool was appropriate is because we want to compare a variable between two groups. The data 
had some null entries, so we had to drop some of the rows. Also, we assumed that because in some rows the years weren’t 
matching, the data GDP per capita didn’t change that much across the years. This would mean that we assume both GDP and 
population don’t change that much over years, which might be tricky. We could have remedied that by grouping across 
years, but we would have had much less data points. 


For the Machine Learning Component:


**Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s)
did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model?
Did you have to clean or restructure your data? What is your interpretation of the results? Do you accept or deny the
hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you
got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the
results?**

**Did you find the results corresponded with your initial belief in the data? If yes/no, why do you think this was the
case? Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have
been used? Was the data adequate for your analysis? If not, what aspects of the data were problematic and how could you
have remedied that?**


**FIRST ML MODEL(S)**

For our first ML models, we used Logistic Regression and Linear Regression models. We tried combinations of different 
features (literacy rate, GDP per capita, etc.) to predict passport strength. We used logistic and linear regression 
because our data is labeled and we have continuous features. (we do not have boolean features)and our output is also 
labeled. For the logistic regression, we separated the passport index data to 3, 4, and also 5 classes. The 3 classes 
were separated according to countries that were “developed”, “mildly developed”, and “not developed”.  The 4 classes we 
tried were the quarters (%25, %50, %75, %100). We also tried 5 classes. The accuracy when we had 5 classes was %56. We 
also tried with 2 classes, and we got the best results when we had 2 classes(accuracy = 0.915); however, we concluded 
that dividing into just 2 classes was biased, so we didn’t use this in the end. Going back to the logistic regression 
when we had 3 classes, the best features to use when we had 3 classes were education index and GDP per capita. The 
accuracy when we used these features were 0.747. When we had 4 classes, the best features to use were education index, 
average iq, GDP per capita. This gave us an accuracy of 0.643. 


For the linear regression model, the best features to use were education rate and GDP per capita. This gave us an 
accuracy of 0.698. We think that the accuracy is better when we have less classes as a result of the decision boundaries 
being less complex (allowing outliers). As explained above in the document, after selecting the relevant rows, we 
dropped the rows with empty values. 

Overall, we are happy with the results even in the face of data scarcity. Again, even if we are happy, having more data 
could definitely help in this situation. Since we are working with countries, we are limited in the sense that there 
are only around ~200, we could have had more data in the sense that we could have added more features/omitted variables 
that we think affect the passport index. 

We found out that the results kind of corresponded with our initial belief that there is some type of 
correlation/relationship between the selected features and passport index. Also, the fact that GDP per capita repeats 
as a great feature to use even if class number or regression type changes, shows us that GDP per capita and passport 
index are related in some type of way. Given this, it is not baffling to see that countries like Luxembourg and 
Singapore, who have the highest GDP per capita are also a couple of the strongest passports in the world. 


**SECOND ML MODEL**

As our second ML model, we chose to use the KMeans algorithm. Since we don't have much data and our labels are discrete 
yet cover a wide range of values, we decided to use an unsupervised learning method. As opposed to many failing 
supervised learning methods that resulted in low accuracy (like the dummy classifier and decision tree), the KMeans 
provided us with interpretable clusters. Our hypothesis was that the GDP, literacy rate, average IQ, and education level 
features of a country were all positively correlated with that country's passport strength. Through KMeans, we were able 
to group countries based on these features, and inspect the mean values of cluster centroids. We saw that clusters that 
had high mean values for these features also had high mean passport strengths, with the same holding true for lower 
values/lower mean passport strengths. This validated our hypothesis.

As explained above in the document, after selecting the relevant rows, we dropped the rows with empty values. 

Since this KMeans is an unsupervised model, evaluating was more difficult. We were not trying to cluster different 
classes and evaluate how close each point in a cluster is to the centroid in the traditional sense. We extracted the 
cluster information and evaluated the correlation of mean values in the cluster, after saving it as a csv. This was 
meaningful in our case as we wanted to see if different countries' features and passport indices could show some form of 
pattern, exploring the idea we introduced when doing logistic regression. For instance, if we assume the three clusters 
denote a country's development level, we can see how that affects passport strength. However, evaluating the quality of 
clustering with a silhouette score metric, we see that the clusters are not that well formed. The correlation is there, 
but we see that it is more 'continuous' than grouped. Thus, even though the model was useful in providing us with 
insights, it turned out to be a suboptimal model for this dataset.

The results we found are as expected, since historically, we would expect this kind of trend. Our biases and knowledge 
towards the world would lead us to believe that countries that are more privileged, have better economic standards, and 
better education systems/opportunities to be "respected" more by other ones. Countries with better infrastructure and 
more opportunities are seen as credible, and their people are trusted more. We are assuming that this is because of 
stigmas/biases created towards poorer countries, and the exclusion of them. However, we saw that data on imports and 
exports actually skewed the results. Though we initially assumed they would also be a part of the equation in 
determining passport strength, this discrepancy might be due to considerations of the people from countries, their 
living standards, and how they would act as tourists, rather than the country's trade relations.

Overall, we are happy and confident with our results. Nonetheless, we would like to add that our data could have been 
more robust. Since we are working with countries, we are limited in the sense that there are only around ~200, but we 
could have found more features, features with matching years, and possibly more years of passport information to 
augment and aggregate the data. We also had missing values for some countries in some columns. We could not use data on 
every single country (we still used most). 

