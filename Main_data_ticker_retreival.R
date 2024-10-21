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
  name2<-str_replace_all(name, " ", "%20")
  api<-"67f15f74f937e7f6376252601326b292d0002f7e51431616c2b3a5384329c981"
  url<-paste0("https://api.sec-api.io/mapping/name/", name2, "?token=", api)
  
  filename<-"sec_api/file.json"
  GET(url,write_disk(filename, overwrite = TRUE))
  
  data <- fromJSON("sec_api/file.json")

  # if data doesn't have a ticker for a company, make that cell NA
  if (!is.null(data$ticker)) {
   ticker <- as.data.frame(cbind(ticker=data$ticker[1], 
                                 name=data$name[1],
                                 input_name=name))
   print(ticker)
   } else {
     ticker <- as.data.frame(cbind(ticker=NA, name=NA, input_name=name))
   }
} 

# make a list of the tickers for all companies with look
tickers <- c()
for (i in 1:length(companies)) {
  print(i)
  ticker <- get_sec(i)
  tickers<-rbind(tickers, ticker)
  
  if (i %% 5 == 0) {
    Sys.sleep(20)
  }
}

# create dataframe of tickers
tickers_df2 <- tickers_df[-nrow(tickers_df), ]
tickers_df <- data.frame(ticker = tickers)

# combine two data frames to make main_data include ticker symbols
main_data <- rbind(main_data, tickers_df)
head(main_data)


blank <- sum(tickers_df$ticker == "", na.rm = TRUE)
print(blank)
