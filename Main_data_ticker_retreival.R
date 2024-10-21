install.packages(c("httr", "jsonlite"))
library(httr)
library(jsonlite)
library(tidyverse)

main_data<-read.csv("main_data.csv")

# get the column of firm names from main data
companies<-as.vector(main_data$firm_name)
companies

write.csv(companies, "meng_cleaned.csv", row.names=F)

# function to look up the ticker symbols from sec data and store the data of companies and symbols as data
get_sec <- function(i) {
  name<- companies[i]
  api<-"67f15f74f937e7f6376252601326b292d0002f7e51431616c2b3a5384329c981"
  #api<-"40f5fb11bbb19188a44e56e2f2d10fa8a20616e21beabb93d1f7b16e95fdef84"
  url<-paste0("https://api.sec-api.io/mapping/name/", name, "?token=", api)
  
  filename<-"sec_api/file.json"
  GET(url,write_disk(filename, overwrite = TRUE))
  
  data <- fromJSON("sec_api/file.json")

  # if data doesn't have a ticker for a company, make that cell NA
  if (!is.null(data$ticker)) {
   ticker <- data$ticker[1]
   print(data$ticker[1])
   } else {
     ticker <- NA
   }
} 

# make a list of the tickers for all companies with look
tickers <- c()
#for (i in 1:length(companies)) {
for (i in 1:5) {
  print(i)
  ticker <- get_sec(i)
  tickers<-rbind(tickers, ticker)
}

# create dataframe of tickers
tickers_df <- data.frame(ticker = tickers)

#write.csv(tickers_df, "sec_api/tickers_df_1_5.csv", row.names = F)

# combine two data frames to make main_data include ticker symbols
main_data <- rbind(main_data, tickers_df)
head(main_data)

