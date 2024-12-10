# Lobbying Markdown


## Title

Q1: How can we best predict each firm’s lobbying spending on the
Waxman-Markey bill?

Q2: How do certain characteristics of a company predict how much money
they’ll spend on lobbying for the Waxman-Markey bill?

## Introduction

Lobbying is one of the most important facets of the political process. In particular, it has a significant impact on the legislative process. Essentially, lobbying is the act of communicating directly with a politician in the hopes of influencing future policy (Chen, 2024). While lobbying is protected under our constitutional rights, many critics notice that it has historically been used as a tool by large businesses to pass or halt legislation that impacts their profit margins (Wallach, 2015). These companies may hire lobbyists to advocate to lawmakers their support for or opposition against a bill. Climate lobbying only accounts for 2.9% of lobbying in the United States (Brulle 2016). Despite this, billions of dollars are spent annually in lobbying efforts to deter policy implementation. In addition, some of these lobbying efforts routinely go unaccounted for as a result of shadow lobbying, as the Lobbying Disclosure Act is only required to account for bills lobbied by registered lobbyists. Our research aims to estimate corporate spending on lobbying and promote transparency within the lobbying sector.
Our research focuses on the Waxman-Markey Bill, a 2009 climate bill that sought to establish measures to control U.S. carbon emissions (Bogardus et al, 2016). The bill narrowly passed the House and was never brought to the Senate due to opposition control of the chamber. Since then, multiple other bills regarding greenhouse gas emissions have reached the house floor, such as the Energy Innovation and Carbon Dividend Act, which charge companies for their carbon pollution (H.R.5744 - 118th Congress (2023-2024): Energy Innovation and Carbon Dividend Act of 2023, 2023). Corporations that lose value from these implementations are more likely to lobby against these bills, since stopping the legislation can be more cost-effective than complying with the bill. 
Our goal was to create a model that estimates how much money a company may spend on lobbying for the Waxman-Markey Bill. We utilized R programming to aggregate company data and developed a linear model to estimate corporate spending on lobbying. The model considered a company’s gas emissions, sector, and stock value and output an estimate for the dollar amount spent on lobbying by the company. This model can be used in future applications of legislative analysis. In particular, this method can be used to predict the public reaction to certain legislation or estimate the effectiveness of mandatory reporting measures. For instance, the model’s estimate of a particular company’s lobbying spending may aid detection of underreporting lobbying by highlighting the gap between a company’s actual and estimated spending. Similarly, it can prevent shadow lobbying and lobbying done by individuals not registered as lobbyists (Slobozhan et al, 2022).


## Literature Review

The concept for our data model was based on prior research predicting corporate lobbying (Meng & Rode, 2019). Research by Meng and Rode (2019) used regression modeling systems to predict whether or not a company would gain or lose value, serving as a step to uncover the relationships between a firm’s lobbying expense and the fate of climate policy. Their empirically driven analysis was clear: firms that were expected to lose value were more likely to spend money against the Waxman-Markey bill in comparison with firms that were expected to gain value. Additionally, research by Brulle (2016) used sectoral analysis to predict lobbying expenditures, resulting in findings that indicate that fossil fuel industries lobby the most, especially in comparison to renewable energy companies and environmental advocacy organizations. 
Such research allows us to give a general hypothesis that sector is a significant variable in predicting lobbying expenditures. For example, Brulle (2019) notes that the fossil fuel sector is the second highest industry in lobbying expenditures as policies like the Waxman-Markey Bill can significantly impact their operational practices. Any regulations set forth by policy can have significant effects on the market value of a company, leading them to spend money that can inhibit its success. Our hypothesis asserts these practices aren’t solely conducted by individual firms but are conducted on the premise of sector-wide fears. In Meng & Rode’s case these fears were driven by market value, but previous research, such as Slobozhan et al. (2020) which uses regression modeling as an analytical basis, allows us to further hypothesize that these fears are also driven by greenhouse gas emissions. Certain sectors emit more carbon than others, and firms wish to deter regulations that climate policy would invoke. Sectors that emit more carbon, such as the carbon industry, are more likely to have the necessary amount of money to spend on lobbying in comparison to environmentally advocacy or wildlife preservation organizations which may find climate policy’s successes more appealing to their outcomes. 
	Our research expanded on sectoral analysis as a determiner of similarly researched explanatory variables (e.g., revenue share).We utilized additional data on companies whose carbon emissions greatly differed from the companies included in prior datasets. For example, our dataset includes firms that did not lobby against the Waxman-Markey bill. This allows us to more accurately estimate lobbying expenditure correlations by reducing the inflation in our response variable that comes with only including data from companies that lobby. As mentioned in the introduction, our desired accuracy will come at the forefront in future goals of estimating lobbying expenditures of the Waxman-Markey bill and predicting implementations of similar environmental policy bills, such as the priorly mentioned Energy Innovation Act, to further analyze social costs. Eventually, we hope our research helps future explorations in whether or not the fate of environmental policy not only poses consequences to society but consequences to lobbying firms, corporations, and Congress. Ultimately, we hope our research, originally built from prior analysis of climate lobbying’s social costs, can more accurately predict lobbying expenditures. We hope our estimations can rationally define the successes and failures of climate policy.


## Data Description

Step 1. Install necessary packages.

``` r
#install.packages("tidyverse")
#install.packages("kableExtra")
```

Step 2. Declare that you will use these packages in this session.

``` r
library("tidyverse")
library("kableExtra")
```

Step 3. Upload the dataframe that you have created in Spring 2024 into
the repository.

Step 4. Open the dataframe into the RStudio Environment.

``` r
df<-read.csv("finaldatasets/4. merge with meng/merged_meng.csv")
```

Step 5. Use the **head** and **kable** function showcase the first 10
rows of the dataframe to the reader.

``` r
kable(head(df))
```

| Ticker | Company | Total.GHG | NAICS | US_revenue_share | carbon_intensity | lobby_amount |
|:---|:---|---:|---:|---:|---:|---:|
| AA | ALCOA INC | 9665558 | 331312 | 0.5101266 | 1.054 | 3240000 |
| ABT | ABBOTT LABORTORIES | 271109 | 325412 | NA | NA | 0 |
| ADM | ARCHER DANIELS MIDLAND CO. | 11145390 | 311222 | NA | NA | 0 |
| AEE | AMEREN | 58893386 | 221210 | 1.0000000 | 0.000 | 3090000 |
| AEP | AMERICAN ELECTRIC POWER | 112654855 | 221112 | NA | 0.000 | 14100663 |
| AES | AES CORPORATION | 19935187 | 551112 | 0.1584387 | NA | 11250 |

## Question 1: What is the frequency of this data frame?

Answer: 0, data tacken during the waxman markey bill period

## Question 2: What is the cross-sectional (geographical) unit of this data frame?

Answer: Company

Step 6. Use the **names** function to display all the variables (column)
in the dataframe.

``` r
names(df)
df <- df %>% 
  mutate(NAIC2 = substr(NAICS, 1, 2))
```

## Question 3: Which column represents the explanatory variable of interest?

Answer: Total.GHG and NAICS

## Question 4: Which column represents the outcome variable of interest?

Answer: lobby_amount

Step 7: Fit a regression model $y=\beta_0 + \beta_1 x + \epsilon$ where $y$ is the outcome variable and $x$ is the treatment variable. Use the summary function to display the results.


``` r
names(df)
table(df$NAIC2)
model1<-lm(lobby_amount ~ Total.GHG + as.factor(NAIC2), data=df)

summary(model1)

library(ggplot2)
ggplot(df, aes(x = log(Total.GHG), y = log(lobby_amount))) +
  geom_point()
```

## Question 5: What is the equation that describes the linear regression above? Please include an explanation of the variables and subscripts.

$$
lobby_i = \beta_0 + \beta_1 \times Total.GHG_i  +  \epsilon_i
$$

where $i$ represents each company

## Question 6: What fixed effects can be included in the regression? What does each fixed effects control for? Please include a new equation that incorporates the fixed effects.

We already included a fixed effect which was a dummie variable for NAICS336411 after finding it to be the only significant NAICS sector predictor.



## Conclusion and Future Work

At a significance level of 0.05, a company’s total greenhouse gas emissions is a significant predictor for the company’s lobbying spending. A company’s NAICS sector is not a significant predictor. 

Companies that produce more GHG emissions have a higher likelihood of lobbying against the Waxman-Markey bill. This is because it affects their profits by forcing them to significantly change their operational methods to be more environmentally friendly. Likewise, companies that have lower GHG emissions have more incentive to lobby for the bill because it increases costs for their competitors. 

This project can be improved by trying more robust models for the data  or by collecting more data since the current dataset is small and missing values for some explanatory variables.

These findings confirm previous research that GHG emissions is a significant predictor of lobbying spending but suggest that the relationship between GHG emissions and lobbying spending may not be as strong as past research implied, depending on the model used.



## References

Bogardus, K., & Reilly , A. (2016, June 27). 7 years later, failed
Waxman-Markey bill still makes waves. E&E News by POLITICO.
http://www.eenews.net/articles/7-years-later-failed-waxman-markey-bill-still-makes-waves/

Brock, C. Partisan polarization and corporate lobbying: information,
demand, and conflict. Int Groups Adv 10, 95–113 (2021).
https://doi.org/10.1057/s41309-021-00112-5

Brulle, R.J. The climate lobby: a sectoral analysis of lobbying spending
on climate change in the USA, 2000 to 2016. *Climatic Change* 149,
289–303 (2018). https://doi.org/10.1007/s10584-018-2241-z

Butler, D. M., & Miller, D. R. (2022). Does Lobbying Affect Bill
Advancement? Evidence from Three State Legislatures. Political Research
Quarterly, 75(3), 547-561. https://doi.org/10.1177/10659129211012481

Cabral, S., Krasner, D., & Doubledee, R. (2023, May 2). Calls for
transparency around corporate political spend are growing louder. Just
31% of America’s largest companies currently disclose. JUST Capital.
https://justcapital.com/news/31-percent-of-americas-largest-companies-disclose-lobbying-political-contributions/#:~:text=The%20state%20of%20political%20spend,the%20companies%20in%20our%20Rankings

Chen, J. (2024, August 28). Lobby: What it is, how it works, examples.
Investopedia. https://www.investopedia.com/terms/l/lobby.asp

Hill, M.D., Kelly, G.W., Lockhart, G.B. and Van Ness, R.A. (2013),
Determinants and Effects of Corporate Lobbying. *Financial Management*,
42: 931-957. https://doi.org/10.1111/fima.12032

Meng, Kyle C.; Rode, Ashwin (2019). Data from: The social cost of
lobbying over climate policy \[Dataset\]. Dryad.
https://doi.org/10.5061/dryad.gg4pk7d Polluters pay. people get a carbon
cashback. Energy Innovation and Carbon Dividend Act. (2023, September
28). https://energyinnovationact.org/

Segal, T. (2022, July 20). Bribery vs. lobbying: What’s the difference?
Investopedia.
https://www.investopedia.com/financial-edge/0912/the-differences-between-bribery-and-lobbying.aspx#:~:text=Bribery%20is%20considered%20an%20effort,illegal%2C%20while%20lobbying%20is%20not

Slobozhan, I., Ormosi, P., Sharma, R. (2020). Which Bills Are Lobbied?
Predicting and Interpreting Lobbying Activity in the US. In: Song, M.,
Song, IY., Kotsis, G., Tjoa, A.M., Khalil, I. (eds) Big Data Analytics
and Knowledge Discovery. DaWaK 2020. Lecture Notes in Computer
Science(), vol 12393. Springer, Cham.
https://doi.org/10.1007/978-3-030-59065-9_23

Slobozhan, I., Ormosi, P., & Sharma, R. (2022). Detecting shadow
lobbying. *Social Network Analysis and Mining*, 12(1), 48.

Weiser, D. (2024, September 20). Why lobbying is legal and important in
the U.S. Investopedia.
https://www.investopedia.com/articles/investing/043015/why-lobbying-legal-and-important-us.asp#:~:text=Lobbying%20is%20an%20integral%20part,participation%20in%20our%20democratic%20environment
