For at least 8 of the attributes of your records, you should provide the following information:
Type of data that will be used for the representation.
Default value
Range of value.
Simplified analysis of the distribution of values
Are these values unique?
Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how?
Is this a required value?
Do you plan to use this attribute/feature in the analysis? If so, how?
Does this feature include potentially sensitive information? If so, how do you suggest handling such issues?

**Country**
Type: String
Default value: None
Range of value: 195 countries
Simplified analysis of the distribution of values: The countries are distributed across the world, 
with some countries having more data than others.
Unique: Yes
Duplicate detection: Yes, by checking if the country is already in the dataset with the same columns.
Required: Yes
Use in analysis: Yes, to compare the passport strength with the education level and economic status of the countries.
Sensitive information: No

**Year of Data Collection**
Type: Integer
Default value: None
Range of value: 2019-2024
Simplified analysis of the distribution of values: The data is distributed across the years, 
for a given feature, years have the same distribution. But different features have different distributions of years.
Unique: No
Duplicate detection: No
Required: Yes
Use in analysis: Yes, this shows trends over time.
Sensitive information: No

**Passport Rank**
Type: Integer
Default value: None
Range of value: 1-111
Simplified analysis of the distribution of values: The passport rank is distributed across the countries,
with some countries having a higher rank than others. Each rank has one to a few countries.
Unique: No
Duplicate detection: No
Required: Yes
Use in analysis: Yes, to see what passport strength is correlated with.
Sensitive information: No

**Number of Visa Free Countries**
Type: Integer
Default value: None
Range of value: 28-194
Simplified analysis of the distribution of values: There are one to a few countries for each number of visa-free countries.
Unique: No
Duplicate detection: No
Required: Yes
Use in analysis: Yes, to see what passport strength is correlated with.
Sensitive information: No

**Education Index**
Type: Float
Default value: None
Range of value: 0.159 - 0.938
Simplified analysis of the distribution of values: Roughly normally distributed, with a few outliers.
Unique: No
Duplicate detection: No
Required: Yes
Use in analysis: Yes, to see if the education level of a country is correlated with the passport strength.
Sensitive information: No

**Exports**
Type: Float
Default value: None
Range of value: 3 - 3,715,827 (in millions of USD)
Simplified analysis of the distribution of values: Normally distributed, with a few outliers.
Unique: No
Duplicate detection: No
Required: Yes
Use in analysis: Yes, to see if international trade is correlated with the passport strength.
Sensitive information: No

**Imports**
Type: Float
Default value: None
Range of value: 3.770 - 3,375,948 (in millions of USD)
Simplified analysis of the distribution of values: Normally distributed, with a few outliers.
Unique: No
Duplicate detection: No
Required: Yes
Use in analysis: Yes, to see if international trade is correlated with the passport strength.
Sensitive information: No

**GDP per Capita**
Type: Float
Default value: None
Range of value: 259.0 - 240,862.2 (in USD)
Simplified analysis of the distribution of values: Normally distributed, with a few outliers.
Unique: No
Duplicate detection: No
Required: Yes
Use in analysis: Yes, to see if the economic status of a country is correlated with the passport strength.
Sensitive information: No

**Average IQ**
Type: Float
Default value: None
Range of value: 47.72 - 106.48	
Simplified analysis of the distribution of values: Normally distributed, with a few outliers.
Unique: No
Duplicate detection: No
Required: Yes
Use in analysis: Yes, to see if the average IQ of a country is correlated with the passport strength, as 
it can be considered a measure of the education level of a country.
Sensitive information: Yes, this feature could be considered sensitive, but it is publicly available information. We
will not use this feature to identify individuals, but to see if it is correlated with the passport strength and 
possibly combine it with the education index.
