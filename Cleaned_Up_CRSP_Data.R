install.packages("dplyr")
library(dplyr)

df2<-X200908_201012CRSP_1_%>%
  group_by(TICKER, COMNAM) %>%  
  tally() %>%
  filter(n==18)

df3<-X200908_201012CRSP_1_ %>%
  group_by(TICKER, COMNAM, NAICS) %>%
  summarize(ASK=mean(PRC))

Cleaned_up<-merge(df2, df3, by=c("TICKER", "COMNAM"))

View(Cleaned_up)
