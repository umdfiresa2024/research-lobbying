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
```

    [1] "Ticker"           "Company"          "Total.GHG"        "NAICS"           
    [5] "US_revenue_share" "carbon_intensity" "lobby_amount"    

## Question 3: Which column represents the explanatory variable of interest?

Answer: Total.GHG and NAICS

## Question 4: Which column represents the outcome variable of interest?

Answer: lobby_amount

## Question 5: What is the equation that describes the linear regression above? Please include an explanation of the variables and subscripts.

$$
lobby_i = \beta_0 + \beta_1 \times Total.GHG_i + \beta_2 \times \delta_{NAIC} +  \epsilon_i
$$

where $i$ represents each company

**Results with 6-digit NAIC fixed effects.**

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

**Results with 2-digit NAIC fixed effects.**

``` r
df2<-df %>%
  mutate(NAICS2=substr(NAICS,1,2))

model2<-lm(lobby_amount ~ Total.GHG + as.factor(NAICS2), data=df2)

summary(model2)
```


    Call:
    lm(formula = lobby_amount ~ Total.GHG + as.factor(NAICS2), data = df2)

    Residuals:
         Min       1Q   Median       3Q      Max 
    -6734772 -1168793  -780145  -583043 48301117 

    Coefficients:
                          Estimate Std. Error t value Pr(>|t|)   
    (Intercept)          3.699e+06  4.585e+06   0.807  0.42067   
    Total.GHG            5.555e-02  2.110e-02   2.633  0.00904 **
    as.factor(NAICS2)21 -2.851e+06  4.667e+06  -0.611  0.54186   
    as.factor(NAICS2)22 -2.445e+06  4.650e+06  -0.526  0.59959   
    as.factor(NAICS2)31 -3.030e+06  4.711e+06  -0.643  0.52074   
    as.factor(NAICS2)32 -2.969e+06  4.622e+06  -0.642  0.52128   
    as.factor(NAICS2)33 -2.535e+06  4.629e+06  -0.548  0.58446   
    as.factor(NAICS2)42 -3.703e+06  5.616e+06  -0.659  0.51026   
    as.factor(NAICS2)44 -3.757e+06  6.485e+06  -0.579  0.56294   
    as.factor(NAICS2)45 -3.711e+06  6.485e+06  -0.572  0.56767   
    as.factor(NAICS2)48 -3.000e+06  4.711e+06  -0.637  0.52485   
    as.factor(NAICS2)52 -3.703e+06  4.953e+06  -0.748  0.45544   
    as.factor(NAICS2)53 -3.700e+06  6.485e+06  -0.571  0.56880   
    as.factor(NAICS2)54 -3.702e+06  6.485e+06  -0.571  0.56865   
    as.factor(NAICS2)55 -4.795e+06  6.498e+06  -0.738  0.46126   
    as.factor(NAICS2)56 -4.064e+06  5.128e+06  -0.792  0.42891   
    as.factor(NAICS2)61 -3.712e+06  6.485e+06  -0.572  0.56757   
    as.factor(NAICS2)71 -3.735e+06  5.616e+06  -0.665  0.50662   
    as.factor(NAICS2)72 -3.706e+06  6.485e+06  -0.572  0.56820   
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 4585000 on 230 degrees of freedom
      (56 observations deleted due to missingness)
    Multiple R-squared:  0.0507,    Adjusted R-squared:  -0.02359 
    F-statistic: 0.6824 on 18 and 230 DF,  p-value: 0.8271
    
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
