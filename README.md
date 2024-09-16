# Q1: How can we best predict each firm’s lobbying spending on the
Waxman-Markey bill? Q2: How do certain characteristics of a company
predict how much money they’ll spend on lobbying for the Waxman-Markey
bill?


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

## Question 5: What is the equation that describes the linear regression above? Please include an explanation of the variables and subscripts.

$$
lobby_i = \beta_0 + \beta_1 \times RevShare_i + \beta_2 \times CarbonIntensity_i + \sigma_{naic} + \epsilon_i
$$

where $i$ represents each company

## Question 6: What fixed effects can be included in the regression? What does each fixed effects control for? Please include a new equation that incorporates the fixed effects.

## Question 7: Run a new regression with the fixed effects. Does the RMSE improve?

Step 9: Change the document format to gfm

Step 10: Change the filename to README.qmd. Render the document

Step 11: Push the document back to GitHub and observe your beautiful
document in your repository!
