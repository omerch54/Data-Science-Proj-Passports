-How many data points are there in total? How many are there in each group you care about?

In our csv tables, we have roughly 200 rows of data in our (5) csv files as we are working with countries. We care about 
countries and their respective passports strengths, education level, and economic status, and we have curated data almost 
all countries.

-Do you think this is enough data to perform your analysis later on?

Yes, we believe that this is enough data to perform our analysis later on. We have a good amount of data to work with 
given our context and the type of analysis we are looking to perform.

-What are the identifying attributes?

The identifying attributes are the country names. We have a column for country names, and we will use this to identify
the countries in our data.

-Where is the data from?

The data are from the following sources:
https://en.wikipedia.org/wiki/Henley_Passport_Index -> passport index
https://www.datapandas.org/ranking/education-rankings-by-country#full-data -> education rankings
https://en.wikipedia.org/wiki/List_of_countries_by_exports -> exports
https://en.wikipedia.org/wiki/List_of_countries_by_imports -> imports
https://worldpopulationreview.com/country-rankings/average-iq-by-country -> average IQ
https://worldpopulationreview.com/country-rankings/literacy-rate-by-country -> literacy rate
https://data.worldbank.org/indicator/NY.GDP.PCAP.CD -> GDP per capita

-How did you collect your data?

We scraped the data from the top 4 sources in the list above, and we downloaded data from the bottom 3. Now, we can
just load the data from the csv files we have created.

-Is the source reputable?

Yes, the sources are reputable. We are using reputable sources such as Wikipedia and the World Bank.

-How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?

We generated the sample by scraping the data from the sources listed above. The sample is relatively small, but it is
representative of the countries we are interested in. We cannot really have a sampling bias as we are working with countries,
and not a specific group of people. Our maximum sample size is ~200, but there are much possible information we could
have collected for each country. We have chosen to focus on the education level and economic status, which are the
ones we are researching to see if they have any correlation with the passport strength.

-How clean is the data? Does this data contain what you need in order to complete the project you proposed to do?

The data is relatively clean, but there are some missing values. We have the data we need to complete the project we
proposed to do.

-How did you check for the cleanliness of your data? What was your threshold reference?

We checked for the cleanliness of our data by looking at the data in the csv files. We checked for missing values,
issues loading the data, and the data types. We did not have a threshold reference, as there is a lot of 
variability in the data we are working with - different countries have different levels of education, economic status,
etc. that can differ greatly.

-Did you implement any mechanism to clean your data? If so, what did you do?

As the data we found are from curated sources, we did not have to clean the data, but there are some missing values
and some issues with the data types. We are planning to clean the data when we are ready to perform the analysis and 
know what we need to do with the data.

-Are there missing values? Do these occur in fields that are important for your project's goals?

Yes, there are missing values, but most are not important as they are not data collected on the years we are interested
in. There also is some missing data on recent years, and it might affect our analysis for some countries to some extent,
but we believe it won't be a major issue. We can still get significant results from the number of countries we have 
full data for.

-Are there duplicates? Do these occur in fields that are important for your project's goals?

No.

-How is the data distributed? Is it uniform or skewed? Are there outliers? What are the min/max values?

The data is distributed in a way that is not uniform, and there are outliers. The data is skewed, and there are
outliers. The min/max values are different for each country, and we have a wide range of values for each attribute.
Working with countries, we have a lot of variability in the data we are working with, but we are hoping to find some
correlation between the passport strength and the education level and economic status of the countries.

-Are there any data type issues? Where are these coming from? How will you fix them?

Yes, there are some data type issues. We did not clean the data while scraping it, and some datasets we downloaded
do not have the perfect format. For example, in one csv we downloaded, the year is a float, and we will have to convert
it to an integer. We will fix them by casting the data to the correct data type.

-Do you need to throw any data away? What data? Why? Any reason this might affect the analyses you are able to run or the conclusions you are able to draw?

We do not need to throw any data away.

-Summarize any challenges or observations you have made since collecting your data. Then, discuss your next steps and how your data collection has impacted the type of analysis you will perform. (approximately 3-5 sentences)

We have observed that the data we have collected is not perfect, and there are some missing values and data type issues.
That being said, we believe that we have enough data to perform the analysis we are interested in. Some challenges we
have faced are:
* A website we were scraping did not have a common coding structure, and we had to adjust our code
to account for this. For tables, it was not using table tags etc.
* A website we were scraping had a dynamic table, and we had to use Selenium to scrape the data.
We don't think these challenges will affect our analysis as we were able to collect the data we needed. Our next steps
are to clean the data and perform the analysis. We will look for correlation between the passport strength and the
education level and economic status of the countries as initially planned.