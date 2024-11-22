# Lobbying Markdown

## Title

Q1: How can we best predict each firm’s lobbying spending on the
Waxman-Markey bill?

Q2: How do certain characteristics of a company predict how much money
they’ll spend on lobbying for the Waxman-Markey bill?

## Introduction

Lobbying is an important feature of representation in the US government
as it can help those without voices be reached. In the corporate world,
lobbying can also be used by businesses to support or oppose bills and
legislation that improve or harm their profit margins. These companies
may employ lobbyists to work on their behalf, or they can hire a
lobbying firm to act on their behalf and make their case to legislators
for why a bill should be supported or opposed. Because of the influence
lobbying can hold over politics, the process has multiple rules and
policies in place to insure that misconduct is not jeopardizing this
feature of government representation. Organizations must register if
they employ a lobbyist, and lobbyists must register when they meet
certain requirements. The Lobbying Disclosure Act of 1995 mandated that
lobbying is publicly registered, and much of this data is available on
OpenSecrets.org. Despite these policies, many Americans believe that
lobbying is a feature of government corruption that sways laws and
politicians into the pockets of wealthy business owners. The importance
of our research and project is to verify these concerns and allow for a
more transparent review of the lobbying sector. The relevant bill our
study focuses on is the Waxman-Markey Bill. The goal of the bill was to
establish limits on emissions for several greenhouse gasses. On June
26th, 2009, the bill narrowly passed the House, but, due to a special
election in 2010 as well as other factors, the Senate majority leader
never brought it to the Senate for a vote and it was ultimately never
implemented. Since then, multiple other bills related to limiting
greenhouse gas emissions have reached the house floor, such as the
Energy Innovation and Carbon Dividend Act, which suggests charging
companies for their carbon pollution. If implementing these measures
would cost a company money and/or potential revenue, it is logical to
assume, then, that these corporations could be incentivized to lobby
against these bills, as doing so would ultimately be less expensive than
implementing the bill and losing revenue. As it turns out, lobbying is
not immune to corruption. “Shadow lobbying” is lobbying done by people
who are not registered as lobbyists. People can seek to influence
politicians’ stances on issues without being technically “lobbyists.”
This creates huge problems for tracking the money in politics. Slobozhan
et al. (2022) investigated the prominence of shadow lobbying. The paper
collected a list of all bills after and including the year 2000 and
subtracted all bills that were registered to have been lobbied for or
against on OpenSecrets. The researchers then analyzed the remaining
bills to examine the probability that they were lobbied but not
reported, or if they were simply not lobbied. The paper states that it
infers that a significant amount of bills had lobbying activity that was
not reported properly. We strive to build further on this research. One
problem is that, while a bill might have technically reported lobbying,
the actual amount spent may be underreported. This problem was not
investigated in the prior study because they only looked at bills
without any reported lobbying. Our research will create a model that
develops a theoretical amount spent on lobbying for a climate bill
similar to Waxman-Markey, then will compare to the actual amount,
allowing us to assess the likelihood that a bill’s lobbying was
underreported. We will create a model that will predict lobbying
expenditure for a company–theoretically, how much money a company will
spend on lobbying for the Waxman-Markey Bill. Greenhouse gas emissions ,
sector, and stock value will be the inputs that will be used to generate
the output value. The model will be trained with data from the
Waxman-Markey bill, then applied to similar bills that aimed to reduce
GHG emissions. Another hope is that this model can help prevent
underreporting of lobbying, as, if there is a severe disparity between
the predicted number and reported amount of money spent on policies
related to climate change, the bill and its related parties can be
investigated further for potential lobbying misconduct.

## Literature Review

Our predictive modeling was inherited from research done that similarly
predicted the lobbying behavior of corporations (Meng & Rode, 2019).
Previous research used regression modeling systems to predict company
values, serving to uncover relationships between lobbying expenditures
and whether or not a bill has been passed (Meng & Rode, 2019).
Additionally, Brulle (2016) used sectoral analysis to predict lobbying
expenditures, resulting in findings which indicate that fossil fuel
industries lobby the most, especially in comparison to renewable energy
companies and environmental advocacy organizations. This, alongside
previous research from Meng & Rode (2019), establishes correlations to
fossil fuel lobbying expenditures and the failure of policy. It’s worth
noting that climate lobbying only accounts for 2.9% of lobbying in the
United States (Brulle 2016). Despite this, billions of dollars are spent
annually in lobbying efforts to deter policy implementation. In
addition, some of these lobbying efforts routinely go unaccounted for as
a result of shadow lobbying, as the Lobbying Disclosure Act is only
required to account for bills lobbied by registered lobbyists. Similarly
to prior analysis of the Waxman-Markey bill, regression modeling can be
used to predict whether or not a bill has been secretly lobbied
(Slobozhan et al., 2020) These parallels help set the foundations for
what we wish to build off as it comes to expanding our research. For
example, our research still relies on sectoral analysis as a determiner
of similarly researched explanatory variables (e.g. revenue share). In
this case, our desired expansion involves providing additional data on
companies whose carbon emissions greatly differ from the companies
included in prior datasets. For example, our dataset includes firms that
did not lobby against the Waxman-Markey bill. This allows us to more
accurately predict lobbying expenditure correlations by including more
zeroes, reducing inflation in our initial dataset. This accuracy will
come at the forefront in our goal of not only predicting the
implementation of the Waxman-Markey bill, but predicting implementations
of similar environmental policy bills, such as the priorly mentioned
Energy Innovation Act, as a model in analyzing social costs. Our desired
accuracy also allows our research to extend beyond typical social cost
nomenclature and to an approach that analyzes both private costs and
benefits. We want to explore whether or not the fate of environmental
policy not only poses consequences to society, but consequences to
lobbying firms, corporations, and Congress. Ultimately, our research
will build upon prior analysis of climate lobbying’s social costs into
an exploration of the benefits firms receive from lobbying and extend
that to societal determinants and implications.

## Data Description

Step 1. Install necessary packages.

``` r
#install.packages("tidyverse")
#install.packages("kableExtra")
```

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
df<-read.csv("finaldatasets/4. merge with meng/merged_meng.csv")
```

Step 5. Use the **head** and **kable** function showcase the first 10
rows of the dataframe to the reader.

``` r
kable(head(df))
```

| Ticker | Company                    | Total.GHG |  NAICS | US_revenue_share | carbon_intensity | lobby_amount |
|:-------|:---------------------------|----------:|-------:|-----------------:|-----------------:|-------------:|
| AA     | ALCOA INC                  |   9665558 | 331312 |        0.5101266 |            1.054 |      3240000 |
| ABT    | ABBOTT LABORTORIES         |    271109 | 325412 |               NA |               NA |            0 |
| ADM    | ARCHER DANIELS MIDLAND CO. |  11145390 | 311222 |               NA |               NA |            0 |
| AEE    | AMEREN                     |  58893386 | 221210 |        1.0000000 |            0.000 |      3090000 |
| AEP    | AMERICAN ELECTRIC POWER    | 112654854 | 221112 |               NA |            0.000 |     14100663 |
| AES    | AES CORPORATION            |  19935187 | 551112 |        0.1584387 |               NA |        11250 |

## Question 1: What is the frequency of this data frame?

Answer: 0, data tacken during the waxman markey bill period

## Question 2: What is the cross-sectional (geographical) unit of this data frame?

Answer: Company

Step 6. Use the **names** function to display all the variables (column)
in the dataframe.

``` r
names(df)
```

    [1] "Ticker"           "Company"          "Total.GHG"        "NAICS"           
    [5] "US_revenue_share" "carbon_intensity" "lobby_amount"    

## Question 3: Which column represents the explanatory variable of interest?

Answer: Total.GHG and NAICS

## Question 4: Which column represents the outcome variable of interest?

Answer: lobby_amount

Step 7: Fit a regression model $y=\beta_0 + \beta_1 x + \epsilon$ where
$y$ is the outcome variable and $x$ is the treatment variable. Use the
**summary** function to display the results.

``` r
table(df$NAICS)
```


    113310 211111 211112 212210 212221 212312 213112 221111 221112 221113 221119 
         1     17      3      2      3      1      2      9      2      1     16 
    221121 221122 221210 311222 311230 311421 311422 311611 311615 311942 312111 
         7      1     12      2      2      2      1      4      1      1      1 
    312140 312221 312229 314110 322110 322121 322122 322130 322211 322291 324110 
         1      1      1      1      1      5      1      1      1      1     11 
    325110 325120 325181 325182 325188 325193 325199 325211 325311 325312 325320 
         1      4      1      1      1      1      1      4      3      1      1 
    325412 325414 325510 325611 325612 325998 326192 326211 327213 327310 327320 
         9      1      1      2      1      2      1      2      1      1      1 
    327420 331111 331112 331221 331311 331312 331524 332311 332312 332313 332911 
         1      3      1      5      1      1      1      1      1      1      1 
    332991 333111 333120 333132 333611 333618 333923 333993 334111 334119 334220 
         1      1      1      2      1      1      1      1      1      1      2 
    334412 334413 335224 335921 336111 336211 336330 336399 336411 336412 336413 
         1      4      1      2      1      1      1      1      1      2      1 
    336414 336415 337214 337910 339112 339113 423930 424510 448120 453998 481111 
         1      1      1      1      2      1      1      1      1      1      1 
    482111 483111 483113 486110 486210 486990 488119 488330 525920 525990 531190 
         1      1      1      1     10      1      1      1      1      5      1 
    541711 551112 562212 562219 562920 611310 713110 713990 721120 
         1      1      1      2      1      1      1      1      1 

``` r
model1<-lm(lobby_amount ~ Total.GHG + as.factor(NAICS), data=df)

summary(model1)
```


    Call:
    lm(formula = lobby_amount ~ Total.GHG + as.factor(NAICS), data = df)

    Residuals:
         Min       1Q   Median       3Q      Max 
    -9238278  -287599        0     1367 44033144 

    Coefficients:
                             Estimate Std. Error t value Pr(>|t|)    
    (Intercept)             3.709e+06  5.031e+06   0.737 0.462333    
    Total.GHG               3.732e-02  2.773e-02   1.346 0.180711    
    as.factor(NAICS)211111 -2.920e+06  5.177e+06  -0.564 0.573757    
    as.factor(NAICS)211112 -5.112e+05  5.810e+06  -0.088 0.930022    
    as.factor(NAICS)212210 -3.745e+06  6.162e+06  -0.608 0.544407    
    as.factor(NAICS)212221 -3.506e+06  5.810e+06  -0.603 0.547277    
    as.factor(NAICS)212312 -3.539e+06  7.115e+06  -0.497 0.619790    
    as.factor(NAICS)213112 -3.425e+06  6.162e+06  -0.556 0.579329    
    as.factor(NAICS)221111  1.847e+06  5.335e+06   0.346 0.729671    
    as.factor(NAICS)221112  2.670e+05  6.566e+06   0.041 0.967624    
    as.factor(NAICS)221113  1.929e+06  7.117e+06   0.271 0.786738    
    as.factor(NAICS)221119 -3.295e+06  5.227e+06  -0.630 0.529598    
    as.factor(NAICS)221121 -3.674e+06  5.392e+06  -0.681 0.496851    
    as.factor(NAICS)221122 -3.709e+06  7.115e+06  -0.521 0.603037    
    as.factor(NAICS)221210 -3.142e+06  5.240e+06  -0.600 0.549884    
    as.factor(NAICS)311222 -3.202e+06  6.164e+06  -0.519 0.604303    
    as.factor(NAICS)311230 -3.713e+06  6.162e+06  -0.602 0.547905    
    as.factor(NAICS)311421 -3.712e+06  6.162e+06  -0.602 0.548020    
    as.factor(NAICS)311422 -3.609e+06  7.115e+06  -0.507 0.612871    
    as.factor(NAICS)311611 -3.482e+06  5.625e+06  -0.619 0.537052    
    as.factor(NAICS)311615 -2.477e+06  7.115e+06  -0.348 0.728304    
    as.factor(NAICS)311942 -3.711e+06  7.115e+06  -0.522 0.602870    
    as.factor(NAICS)312111  2.754e+06  7.115e+06   0.387 0.699400    
    as.factor(NAICS)312140 -3.712e+06  7.115e+06  -0.522 0.602799    
    as.factor(NAICS)312221 -3.751e+06  7.115e+06  -0.527 0.598935    
    as.factor(NAICS)312229 -1.046e+06  7.115e+06  -0.147 0.883353    
    as.factor(NAICS)314110 -3.716e+06  7.115e+06  -0.522 0.602422    
    as.factor(NAICS)322110 -3.725e+06  7.115e+06  -0.524 0.601489    
    as.factor(NAICS)322121 -3.778e+06  5.512e+06  -0.685 0.494293    
    as.factor(NAICS)322122 -3.718e+06  7.115e+06  -0.523 0.602207    
    as.factor(NAICS)322130 -3.740e+06  7.115e+06  -0.526 0.600078    
    as.factor(NAICS)322211 -3.743e+06  7.115e+06  -0.526 0.599759    
    as.factor(NAICS)322291 -3.378e+06  7.115e+06  -0.475 0.635783    
    as.factor(NAICS)324110  5.848e+05  5.273e+06   0.111 0.911861    
    as.factor(NAICS)325110 -3.715e+06  7.115e+06  -0.522 0.602457    
    as.factor(NAICS)325120 -3.838e+06  5.626e+06  -0.682 0.496327    
    as.factor(NAICS)325181 -3.710e+06  7.115e+06  -0.521 0.602961    
    as.factor(NAICS)325182 -3.770e+06  7.115e+06  -0.530 0.597146    
    as.factor(NAICS)325188 -3.712e+06  7.115e+06  -0.522 0.602764    
    as.factor(NAICS)325193 -3.771e+06  7.115e+06  -0.530 0.597074    
    as.factor(NAICS)325199 -3.740e+06  7.115e+06  -0.526 0.600034    
    as.factor(NAICS)325211 -3.929e+06  5.631e+06  -0.698 0.486518    
    as.factor(NAICS)325311 -3.871e+06  5.811e+06  -0.666 0.506455    
    as.factor(NAICS)325312 -3.770e+06  7.115e+06  -0.530 0.597131    
    as.factor(NAICS)325320 -3.727e+06  7.115e+06  -0.524 0.601285    
    as.factor(NAICS)325412 -3.716e+06  5.304e+06  -0.701 0.484814    
    as.factor(NAICS)325414 -3.711e+06  7.115e+06  -0.521 0.602929    
    as.factor(NAICS)325510 -2.596e+06  7.122e+06  -0.364 0.716094    
    as.factor(NAICS)325611 -6.490e+05  6.162e+06  -0.105 0.916279    
    as.factor(NAICS)325612 -3.861e+06  7.116e+06  -0.543 0.588325    
    as.factor(NAICS)325998 -3.715e+06  6.162e+06  -0.603 0.547624    
    as.factor(NAICS)326192 -3.717e+06  7.115e+06  -0.522 0.602257    
    as.factor(NAICS)326211 -3.725e+06  6.162e+06  -0.604 0.546623    
    as.factor(NAICS)327213 -3.753e+06  7.115e+06  -0.527 0.598790    
    as.factor(NAICS)327310 -3.770e+06  7.115e+06  -0.530 0.597141    
    as.factor(NAICS)327320 -4.146e+06  7.122e+06  -0.582 0.561516    
    as.factor(NAICS)327420 -3.742e+06  7.115e+06  -0.526 0.599895    
    as.factor(NAICS)331111 -3.812e+06  5.810e+06  -0.656 0.512963    
    as.factor(NAICS)331112 -3.711e+06  7.115e+06  -0.522 0.602856    
    as.factor(NAICS)331221 -3.907e+06  5.529e+06  -0.707 0.481041    
    as.factor(NAICS)331311 -3.720e+06  7.115e+06  -0.523 0.601954    
    as.factor(NAICS)331312 -8.299e+05  7.120e+06  -0.117 0.907391    
    as.factor(NAICS)331524 -3.729e+06  7.115e+06  -0.524 0.601164    
    as.factor(NAICS)332311 -3.710e+06  7.115e+06  -0.521 0.602954    
    as.factor(NAICS)332312 -3.711e+06  7.115e+06  -0.521 0.602916    
    as.factor(NAICS)332313 -3.709e+06  7.115e+06  -0.521 0.603045    
    as.factor(NAICS)332911 -3.715e+06  7.115e+06  -0.522 0.602515    
    as.factor(NAICS)332991 -3.013e+06  7.115e+06  -0.424 0.672623    
    as.factor(NAICS)333111 -2.114e+06  7.115e+06  -0.297 0.766842    
    as.factor(NAICS)333120 -3.754e+06  7.115e+06  -0.528 0.598682    
    as.factor(NAICS)333132 -2.858e+06  6.162e+06  -0.464 0.643627    
    as.factor(NAICS)333611 -3.837e+06  7.116e+06  -0.539 0.590673    
    as.factor(NAICS)333618 -3.710e+06  7.115e+06  -0.521 0.602957    
    as.factor(NAICS)333923 -1.843e+05  7.115e+06  -0.026 0.979381    
    as.factor(NAICS)333993 -3.710e+06  7.115e+06  -0.521 0.602963    
    as.factor(NAICS)334111 -3.713e+06  7.115e+06  -0.522 0.602684    
    as.factor(NAICS)334119 -3.711e+06  7.115e+06  -0.521 0.602920    
    as.factor(NAICS)334220 -3.711e+06  6.162e+06  -0.602 0.548110    
    as.factor(NAICS)334412 -3.731e+06  7.115e+06  -0.524 0.600929    
    as.factor(NAICS)334413 -3.491e+06  5.625e+06  -0.621 0.535950    
    as.factor(NAICS)335224 -3.713e+06  7.115e+06  -0.522 0.602659    
    as.factor(NAICS)335921 -3.482e+06  6.162e+06  -0.565 0.572975    
    as.factor(NAICS)336111 -3.737e+06  7.115e+06  -0.525 0.600383    
    as.factor(NAICS)336211 -3.302e+06  7.115e+06  -0.464 0.643362    
    as.factor(NAICS)336330 -3.711e+06  7.115e+06  -0.522 0.602864    
    as.factor(NAICS)336399 -3.711e+06  7.115e+06  -0.522 0.602895    
    as.factor(NAICS)336411  2.402e+07  7.115e+06   3.376 0.000972 ***
    as.factor(NAICS)336412  4.397e+05  6.162e+06   0.071 0.943234    
    as.factor(NAICS)336413 -3.713e+06  7.115e+06  -0.522 0.602725    
    as.factor(NAICS)336414 -3.710e+06  7.115e+06  -0.521 0.602968    
    as.factor(NAICS)336415  1.253e+07  7.115e+06   1.761 0.080661 .  
    as.factor(NAICS)337214 -3.710e+06  7.115e+06  -0.521 0.602932    
    as.factor(NAICS)337910 -3.713e+06  7.115e+06  -0.522 0.602705    
    as.factor(NAICS)339112 -3.732e+06  6.162e+06  -0.606 0.545861    
    as.factor(NAICS)339113 -3.710e+06  7.115e+06  -0.521 0.603008    
    as.factor(NAICS)423930 -3.712e+06  7.115e+06  -0.522 0.602802    
    as.factor(NAICS)424510 -3.712e+06  7.115e+06  -0.522 0.602737    
    as.factor(NAICS)448120 -3.748e+06  7.115e+06  -0.527 0.599282    
    as.factor(NAICS)453998 -3.717e+06  7.115e+06  -0.522 0.602258    
    as.factor(NAICS)481111 -4.332e+05  7.115e+06  -0.061 0.951545    
    as.factor(NAICS)482111  6.232e+06  7.115e+06   0.876 0.382710    
    as.factor(NAICS)483111 -3.712e+06  7.115e+06  -0.522 0.602799    
    as.factor(NAICS)483113 -3.715e+06  7.115e+06  -0.522 0.602531    
    as.factor(NAICS)486110 -3.717e+06  7.115e+06  -0.522 0.602260    
    as.factor(NAICS)486210 -3.749e+06  5.277e+06  -0.710 0.478731    
    as.factor(NAICS)486990 -3.712e+06  7.115e+06  -0.522 0.602765    
    as.factor(NAICS)488119 -3.722e+06  7.115e+06  -0.523 0.601850    
    as.factor(NAICS)488330 -3.710e+06  7.115e+06  -0.521 0.602951    
    as.factor(NAICS)525920 -3.710e+06  7.115e+06  -0.521 0.602976    
    as.factor(NAICS)525990 -3.712e+06  5.512e+06  -0.674 0.501823    
    as.factor(NAICS)531190 -3.710e+06  7.115e+06  -0.521 0.602964    
    as.factor(NAICS)541711 -3.711e+06  7.115e+06  -0.522 0.602872    
    as.factor(NAICS)551112 -4.442e+06  7.136e+06  -0.622 0.534716    
    as.factor(NAICS)562212 -3.978e+06  7.118e+06  -0.559 0.577220    
    as.factor(NAICS)562219 -4.017e+06  6.166e+06  -0.652 0.515858    
    as.factor(NAICS)562920 -3.805e+06  7.116e+06  -0.535 0.593784    
    as.factor(NAICS)611310 -3.718e+06  7.115e+06  -0.523 0.602195    
    as.factor(NAICS)713110 -3.720e+06  7.115e+06  -0.523 0.602008    
    as.factor(NAICS)713990 -3.747e+06  7.115e+06  -0.527 0.599343    
    as.factor(NAICS)721120 -3.714e+06  7.115e+06  -0.522 0.602587    
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 5031000 on 129 degrees of freedom
      (56 observations deleted due to missingness)
    Multiple R-squared:  0.359, Adjusted R-squared:  -0.2324 
    F-statistic: 0.607 on 119 and 129 DF,  p-value: 0.997

## Question 5: What is the equation that describes the linear regression above? Please include an explanation of the variables and subscripts.

$$
lobby_i = \beta_0 + \beta_1 \times Total.GHG_i + \epsilon_i
$$

where $i$ represents each company

## Question 6: What fixed effects can be included in the regression? What does each fixed effects control for? Please include a new equation that incorporates the fixed effects.

We already included a fixed effect which was a dummie variable for
NAICS336411 after finding it to be the only significant NAICS sector
predictor.

## Question 7: Run a new regression with the fixed effects. Does the RMSE improve?

Step 9: Change the document format to gfm

Step 10: Change the filename to README.qmd. Render the document

Step 11: Push the document back to GitHub and observe your beautiful
document in your repository!

## Sources in APA

Bogardus, K., & Reilly , A. (2016, June 27). 7 years later, failed
Waxman-Markey bill still makes waves. E&E News by POLITICO.
http://www.eenews.net/articles/7-years-later-failed-waxman-markey-bill-still-makes-waves/

Brock, C. Partisan polarization and corporate lobbying: information,
demand, and conflict. Int Groups Adv 10, 95–113 (2021).
https://doi.org/10.1057/s41309-021-00112-5

Brulle, R.J. The climate lobby: a sectoral analysis of lobbying spending
on climate change in the USA, 2000 to 2016. Climatic Change 149, 289–303
(2018). https://doi.org/10.1007/s10584-018-2241-z

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
Determinants and Effects of Corporate Lobbying. Financial Management,
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
lobbying. Social Network Analysis and Mining, 12(1), 48.

Weiser, D. (2024, September 20). Why lobbying is legal and important in
the U.S. Investopedia.
https://www.investopedia.com/articles/investing/043015/why-lobbying-legal-and-important-us.asp#:~:text=Lobbying%20is%20an%20integral%20part,participation%20in%20our%20democratic%20environment
