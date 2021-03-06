# An Analysis on the Relationships between Behavioral/Physiological Factors and Diabetes

I have an interest in sports, nutrition, and how to maintain certain habits in order to increase athletic performance and overall bodily health. I also have family members who suffer from diabetes and want to be able to better inform them about how to manage their blood sugar and lifestyle choices. In this analysis, I dive into a few factors that I believe would have an impact on diabetes prevalence in the United States. My goal is to stimulate further curiosity and investigation into the factors that have the most impact on diabetes.

# Data Sources

I gathered 2 sources of data from the Center for Disease Control & Prevention (CDC):
* Nutrition, Pysical Activity, and Obesity in US States - 2011-2018
* 500 Cities Data - 2017

# Background Information

* In 2018, 34.2 million Americans, or 10.5% of the population, had diabetes
* The estimated total economic cost of diagnosed diabetes in 2012 is $245 billion, a 41% increase from our previous estimate of $174 billion (in 2007 dollars)
* Exercise helped to lower insulin resistance in previously sedentary older adults with abdominal obesity at risk for diabetes (Resistance training and aerobic) - Harvard Study
* Cross sectional, prospective and retrospective studies have found significant association between physical inactivity and Type 2 Diabetes

# Exploratory Data Analysis

In order to make sense of the data from the CDC, I performed some exploratory data analysis. First, from the Nutrition, Physical Activity, and Obesity dataset, I wanted to see the distribution of the actual data collected. I wanted to draw some parallels to the idea of normal distributions and how most of the random variables in nature are randomly distributed. As can be seen below, the distribution for the Inactivity data resembles a normal distribution. 

![Inactive Data Distr](/img/InactiveDataDistr.png)

I wanted to further analyze the dataset, so I chose a few factors to look at: Inactivity, Obesity, Lack of Fruit Consumpiton, and Lack of Vegetable Consumption. The following picture shows the distribution of data for the above mentioned factors of interest. 


![Total Data Distr](/img/TotalDataDistr.png)

Next, I was interested in viewing the percent obesity in certain US states. I chose the states with the highest population size because I thought they may have relatively higher diabetes prevalence than states with a smaller population. I also included New Jersey because I wanted to have a comparison with my home state.   

![Percent Obese USA](/img/PercentObeseUSA.png)

As seen from the graph, Texas has the highest percent of their population suffering from obesity. The state with the lowest percent of their population suffering from obesity seems to be California. This means that population size may not be indicative of obesity prevalence. 

![Percent Inactive USA](/img/PercentInactiveUSA.png)

In many studies, inactivity has been shown to be a contributing factor to illness. This may have to do with the numerous biochemical molecules, that are released during exercise but are absent during inactivity, which play a vital role in regulating weight, stress, metabolism, and other physiological factors. 

![Percent FrtVeg USA](/img/PercentFrtVegUSA.png)

Nutrition is another widely studied but not well understood lifestyle factor. It is a very complex area of study, which must take into account not only absolute quantities but relative as well. If one consumes sugar but also has a relatively high amount of fat and some protein, the sugar is not processed by the body in the same way as if one would only be consuming sugar. There are many synergistic effects that must be taken into account when analyzing food intake. Water is also very important in maintaining and ensuring efficient digestion, temperature regulation, and many more vital bodily functions.
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
I was interested in seeing the relationship among: Inactivity, Obesity, Fruit Consumption, and Vegetable Consumption. For this I constructed a correlation matrix visualized as a heatmap. The graph shows the strength of relationships, based on hue, for each of the factors of interest. This correlation matrix was constructed from the Nutrition, Physical Activity, and Obesity dataset provided by the CDC.

![Corr Hlth Var 01](/img/CorrHealthVar01.png)

&nbsp;
&nbsp;

In the heatmap shown below, the data was taken from the 500 Cities Dataset. This dataset included a few more measures that I found interesting to look at with regards to diabetes. The measures I focused on were: Inactivity, Lack of Sleep, Binge Drinking, Smoking, Diabetes, and Obesity.

![Corr Hlth Var 02](/img/CorrHlthVar02.png)

&nbsp;
&nbsp;
 
It is important to note that there was a NEGATIVE correlation between binge drinking prevalence and diabetes prevalence. There have been studies showing that while moderate alcohol use can increase blood sugar, heavy alcohol use results in a significant drop in blood sugar and can be lethal. For this reason, many doctors advise their diabetic patients to monitor their alcohol intake more closely. Further investigation should be done that takes into consideration other reasons for this negative correlation. 

![Drinking Diabetes Joint](/img/DrinkingDiabetesJoint.png)

&nbsp;
&nbsp;

When viewed next to each other, these graphs can give us an idea of overall relatedness between the lifestyle factors and diabetes prevalence. Using this information, models can be constructed that could then be used to predict diabetes prevalence given a set of lifestyle factors. This could be used by governments and public officials to determine what kind of funding to allocate for nutrition and health services, as well as how to best fund programs that could curtail the economic effects of diabetes on our healthcare system. 

![Total Correlation 01](/img/TotalCorrelation01.png)

&nbsp;
&nbsp;

Data analysis can be a very powerful tool that gives us insights to questions that are otherwise very difficult to analyze. The advancement of computers, the internet, and other technologies have provided us with the ability to visualize and study complex relationships among factors of interest. These tools and abilities can guide us in asking the proper questions and coming to the best possible conclusions in order to provide predictive power to those who implement these techniques in real world applications.

# Conlusion

* More studies should be conducted to analyze the impact of lifestyle on type 2 Diabetes: Exercise, Sleep, Nutrition, Stress Levels, Drug Use
* Exercise can lower insulin resistance and should be incorporated into a holistic treatment for people suffering from diabetes
* Although the relationship between nutrition and diabetes is complex, the most harmful products to consume are carbonated beverages
* Other factors like lack of sleep seem to have a high correlation with diabetes incidence - why?

# Next Steps
* Gather more accurate information about lifestyle choices

* Gather information about economic burden due to diabetes

* Figure out what kind of effect exercise and better nutrition would have on diabetes related healthcare costs

* Adjust the analysis to include the population size

