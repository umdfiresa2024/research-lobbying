# Q1: How can we best predict each firm’s lobbying spending on the Waxman-Markey bill? Q2: How do certain characteristics of a company predict how much money they’ll spend on lobbying for the Waxman-Markey bill?

## Introduction

	Lobbying is an important feature of representation in the US government as it can help those without voices be reached. Lobbying is also a tool of large businesses who want to support or oppose bills and legislation that improve or harm their profit margins. These companies may employ lobbyists to work on their behalf, or they can hire a lobbying firm to act on their behalf and make their case to legislators for why a bill should be supported or opposed. 
	Lobbying has multiple rules and policies in place to insure that misconduct is not jeopardizing this feature of government representation. Organizations must register if they employ a lobbyist, and lobbyists must register when they meet certain requirements. The Lobbying Disclosure Act of 1995 mandated that lobbying is publicly registered, and much of this data is available on OpenSecrets.org. Despite these policies, many Americans believe that lobbying is a feature of government corruption that sways laws and politicians into the pockets of wealthy business owners. The importance of our research and project is to verify these concerns and allow for a more transparent review of the lobbying sector.
	The relevant bill our study focuses on is the Waxman-Markey Bill. The goal of the bill was to establish limits on emissions for several greenhouse gasses. On June 26th, 2009, the bill narrowly passed the House, but, due to a special election in 2010 as well as other factors, the Senate majority leader never brought it to the Senate for a vote and it was ultimately never implemented. Since then, multiple other bills related to limiting greenhouse gas emissions have reached the house floor, such as the Energy Innovation and Carbon Dividend Act, which charges companies for their carbon pollution. Corporations that lose value from these implementations would be incentivized to lobby against these bills, as doing so would ultimately be less expensive than losing revenue. 
	“Shadow lobbying” is lobbying done by people who are not registered as lobbyists. This creates huge problems for tracking the money in politics. Slobozhan et al. (2022) investigated the prominence of shadow lobbying. The paper collected a list of all bills after and including the year 2000 and subtracted all bills that were registered to have been lobbied for or against on OpenSecrets. The researchers then analyzed the remaining bills to examine the probability that they were lobbied but not reported, or if they were simply not lobbied. The paper states that it infers that a significant amount of bills had lobbying activity that was not reported properly. We strive to build further on this research. One problem is that, while a bill might have technically reported lobbying, the actual amount spent may be underreported. This problem was not investigated in the prior study because they only looked at bills without any reported lobbying. Our research will create a model that develops a theoretical amount spent on lobbying for a climate bill similar to Waxman-Markey, then will compare to the actual amount, allowing us to assess the likelihood that a bill’s lobbying was underreported. 
	We will create a model that will predict lobbying expenditure  for a company–theoretically, how much money a company will spend on lobbying for the Waxman-Markey Bill. Greenhouse gas emissions , sector, and stock value will be the inputs that will be used to generate the output value. The model will be trained with data from the Waxman-Markey bill, then applied to similar bills that aimed to reduce GHG emissions. Another hope is that this model can help prevent underreporting of lobbying, as, if there is a severe disparity between the predicted number and reported amount of money spent on policies related to climate change, the bill and its related parties can be investigated further for potential lobbying misconduct.

 ## Literature Review

	Our predictive modeling was inherited from research done that similarly predicted the lobbying behavior of corporations (Meng & Rode, 2019). Previous research used regression modeling systems to predict company values, serving to uncover relationships between lobbying expenditures and whether or not a bill has been passed (Meng & Rode, 2019). Additionally, Brulle (2016) used sectoral analysis to predict lobbying expenditures, resulting in findings which indicate that fossil fuel industries lobby the most, especially in comparison to renewable energy companies and environmental advocacy organizations. This, alongside previous research from Meng & Rode (2019), establishes correlations to fossil fuel lobbying expenditures and the failure of policy. 
	It’s worth noting that climate lobbying only accounts for 2.9% of lobbying in the United States (Brulle 2016). Despite this, billions of dollars are spent annually in lobbying efforts to deter policy implementation. In addition, some of these lobbying efforts routinely go unaccounted for as a result of shadow lobbying, as the Lobbying Disclosure Act is only required to account for bills lobbied by registered lobbyists. Similarly to prior analysis of the Waxman-Markey bill, regression modeling can be used to predict whether or not a bill has been secretly lobbied (Slobozhan et al., 2020)	
	These parallels help set the foundations for what we wish to build off as it comes to expanding our research. For example, our research still relies on sectoral analysis as a determiner of similarly researched explanatory variables (e.g. revenue share). In this case, our desired expansion involves providing additional data on companies whose carbon emissions greatly differ from the companies included in prior datasets. For example, our dataset includes firms that did not lobby against the Waxman-Markey bill. This allows us to more accurately predict lobbying expenditure correlations by including more zeroes, reducing inflation in our initial dataset. This accuracy will come at the forefront in our goal of not only predicting the implementation of the Waxman-Markey bill, but predicting implementations of similar environmental policy bills, such as the priorly mentioned Energy Innovation Act, as a model in analyzing social costs. Our desired accuracy also allows our research to extend beyond typical social cost nomenclature and to an approach that analyzes both private costs and benefits. We want to explore whether or not the fate of environmental policy not only poses consequences to society, but consequences to lobbying firms, corporations, and Congress. Ultimately, our research will build upon prior analysis of climate lobbying’s social costs into an exploration of the benefits firms receive from lobbying and extend that to societal determinants and implications.

Step 1. Install necessary packages.

``` r
install.packages("tidyverse")
```

    Installing package into '/cloud/lib/x86_64-pc-linux-gnu-library/4.4'
    (as 'lib' is unspecified)

``` r
install.packages("kableExtra")
```

    Installing package into '/cloud/lib/x86_64-pc-linux-gnu-library/4.4'
    (as 'lib' is unspecified)

Step 2. Declare that you will use these packages in this session.

``` r
library("tidyverse")
```

    ── Attaching core tidyverse packages ──────────────────────── tidyverse 2.0.0 ──
    ✔ dplyr     1.1.4     ✔ readr     2.1.5
    ✔ forcats   1.0.0     ✔ stringr   1.5.1
    ✔ ggplot2   3.5.1     ✔ tibble    3.2.1
    ✔ lubridate 1.9.3     ✔ tidyr     1.3.1
    ✔ purrr     1.0.2     
    ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ✖ dplyr::filter() masks stats::filter()
    ✖ dplyr::lag()    masks stats::lag()
    ℹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors

``` r
library("kableExtra")
```


    Attaching package: 'kableExtra'

    The following object is masked from 'package:dplyr':

        group_rows

Step 3. Upload the dataframe that you have created in Spring 2024 into
the repository.

Step 4. Open the dataframe into the RStudio Environment.

``` r
df<-read.csv("main_data.csv")
```

Step 5. Use the **head** and **kable** function showcase the first 10
rows of the dataframe to the reader.

``` r
kable(head(df))
```

| firm_name | permno | naics2 | naics3 | naics4 | dValue_CAPM | dValue_10CI | dValue_15CI | lobby | outlier | US_revenue_share | carbon_intensity |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ADVANCED MICRO DEVICES | 61241 | 33 | 334 | 3344 | 16011982 | 14782741 | -240055 | 1200000 | 0 | 0.1226636 | 0.080 |
| AES | 76712 | 55 | 551 | 5511 | -691024872 | -691657852 | -720684334 | 11250 | 0 | 0.1584387 | NA |
| AGL RESOURCES | 15553 | 55 | 551 | 5511 | 50785837 | 51740420 | 48795742 | 240000 | 0 | 1.0000000 | NA |
| AIR PROD & CHEM | 28222 | 32 | 325 | 3251 | 252146065 | 251323110 | 218761140 | 2415000 | 0 | 0.4565935 | 0.619 |
| AIRGAS | 70308 | 42 | 424 | 4246 | 29140084 | 28049241 | 21514282 | 310000 | 0 | 0.9801500 | NA |
| ALASKA AIRGROUP | 28804 | 48 | 481 | 4811 | 55431639 | 55404061 | 54121225 | 140000 | 0 | NA | 1.217 |

## Question 1: What is the frequency of this data frame?

Answer: N/A

## Question 2: What is the cross-sectional (geographical) unit of this data frame?

Answer: Company

Step 6. Use the **names** function to display all the variables (column)
in the dataframe.

``` r
names(df)
```

     [1] "firm_name"        "permno"           "naics2"           "naics3"          
     [5] "naics4"           "dValue_CAPM"      "dValue_10CI"      "dValue_15CI"     
     [9] "lobby"            "outlier"          "US_revenue_share" "carbon_intensity"

## Question 3: Which column represents the explanatory variable of interest?

Answer: US_revenue_share, carbon_intensity, naics2, naics3, naics4

## Question 4: Which column represents the outcome variable of interest?

Answer: lobby

Step 7: Fit a regression model $y=\beta_0 + \beta_1 x + \epsilon$ where
$y$ is the outcome variable and $x$ is the treatment variable. Use the
**summary** function to display the results.

``` r
model1<-lm(lobby ~ US_revenue_share + carbon_intensity + as.factor(naics2), data=df)

summary(model1)
```


    Call:
    lm(formula = lobby ~ US_revenue_share + carbon_intensity + as.factor(naics2), 
        data = df)

    Residuals:
          Min        1Q    Median        3Q       Max 
    -12280344  -2927236  -1356113    300077  49757799 

    Coefficients:
                        Estimate Std. Error t value Pr(>|t|)  
    (Intercept)          2067136    5268064   0.392   0.6953  
    US_revenue_share       31880    2294269   0.014   0.9889  
    carbon_intensity     2197722    3229118   0.681   0.4971  
    as.factor(naics2)21 -2032348    5679135  -0.358   0.7209  
    as.factor(naics2)22  1100020    5026069   0.219   0.8270  
    as.factor(naics2)23 -1973106    8519770  -0.232   0.8172  
    as.factor(naics2)31 -1326162    5278811  -0.251   0.8020  
    as.factor(naics2)32   753528    5514997   0.137   0.8915  
    as.factor(naics2)33  1591667    5072894   0.314   0.7541  
    as.factor(naics2)48 -2571088    6366048  -0.404   0.6869  
    as.factor(naics2)49 18796968    7736303   2.430   0.0162 *
    as.factor(naics2)51  -697273    6041517  -0.115   0.9083  
    as.factor(naics2)52  2772986    6326487   0.438   0.6618  
    as.factor(naics2)54  -316342    8613610  -0.037   0.9708  
    as.factor(naics2)56 -1278969    6928590  -0.185   0.8538  
    as.factor(naics2)72 -2191567    6950082  -0.315   0.7529  
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 6908000 on 156 degrees of freedom
      (51 observations deleted due to missingness)
    Multiple R-squared:  0.1253,    Adjusted R-squared:  0.0412 
    F-statistic:  1.49 on 15 and 156 DF,  p-value: 0.1149

## Linear Regression Equation

$$
lobby_i = \beta_0 + \beta_1 \times RevShare_i + \beta_2 \times CarbonIntensity_i + \sigma_{naic} + \epsilon_i
$$

where $i$ represents each company

## Question 6: What fixed effects can be included in the regression? What does each fixed effects control for? Please include a new equation that incorporates the fixed effects.

## Question 7: Run a new regression with the fixed effects. Does the RMSE improve?

## References

Bogardus, K., & Reilly , A. (2016, June 27). 7 years later, failed Waxman-Markey bill still makes waves. E&E News by POLITICO. http://www.eenews.net/articles/7-years-later-failed-waxman-markey-bill-still-makes-waves/

Brock, C. Partisan polarization and corporate lobbying: information, demand, and conflict. Int Groups Adv 10, 95–113 (2021). https://doi.org/10.1057/s41309-021-00112-5

Brulle, R.J. The climate lobby: a sectoral analysis of lobbying spending on climate change in the USA, 2000 to 2016. Climatic Change 149, 289–303 (2018). https://doi.org/10.1007/s10584-018-2241-z

Butler, D. M., & Miller, D. R. (2022). Does Lobbying Affect Bill Advancement? Evidence from Three State Legislatures. Political Research Quarterly, 75(3), 547-561. https://doi.org/10.1177/10659129211012481

Chen, J. (2024, August 28). Lobby: What it is, how it works, examples. Investopedia. https://www.investopedia.com/terms/l/lobby.asp 

Hill, M.D., Kelly, G.W., Lockhart, G.B. and Van Ness, R.A. (2013), Determinants and Effects of Corporate Lobbying. Financial Management, 42: 931-957. https://doi.org/10.1111/fima.12032

Meng, Kyle C.; Rode, Ashwin (2019). Data from: The social cost of lobbying over climate policy [Dataset]. Dryad. https://doi.org/10.5061/dryad.gg4pk7d

Segal, T. (2022, July 20). Bribery vs. lobbying: What’s the difference? Investopedia. https://www.investopedia.com/financial-edge/0912/the-differences-between-bribery-and-lobbying.aspx#:~:text=Bribery%20is%20considered%20an%20effort,illegal%2C%20while%20lobbying%20is%20not 

Slobozhan, I., Ormosi, P., Sharma, R. (2020). Which Bills Are Lobbied? Predicting and Interpreting Lobbying Activity in the US. In: Song, M., Song, IY., Kotsis, G., Tjoa, A.M., Khalil, I. (eds) Big Data Analytics and Knowledge Discovery. DaWaK 2020. Lecture Notes in Computer Science(), vol 12393. Springer, Cham. https://doi.org/10.1007/978-3-030-59065-9_23

Slobozhan, I., Ormosi, P., & Sharma, R. (2022). Detecting shadow lobbying. Social Network Analysis and Mining, 12(1), 48.


