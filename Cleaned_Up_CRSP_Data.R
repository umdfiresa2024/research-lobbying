install.packages("dplyr")
library(dplyr)

df<-read.csv("200908-201012CRSP.csv")

df2<-df %>%
  group_by(TICKER, COMNAM) %>%  
  tally() %>%
  filter(n>=18)

df3<-df %>%
  group_by(TICKER) %>%
  summarize(ASK=mean(PRC, na.rm = TRUE))

df4<-df3 %>%
  filter(TICKER %in% df2$TICKER)

write.csv(df4, "clean_ask.csv", row.names=F)
