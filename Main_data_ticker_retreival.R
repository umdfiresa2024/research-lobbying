install.packages(c("httr", "jsonlite"))
library(httr)
library(jsonlite)
library(tidyverse)

main_data<-read.csv("main_data.csv")

# get the column of firm names from main data
companies<-as.vector(main_data$firm_name)
companies

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
for (i in 11:length(companies)) {
  print(i)
  ticker <- get_sec(i)
  tickers<-rbind(tickers, ticker)
  
  if (i %% 5 == 0) {
    Sys.sleep(20)
  }
}

# create dataframe of tickers
tickers_df <- data.frame(ticker = tickers)
colnames(tickers_df)[colnames(tickers_df) == "ticker.input_name"] <- "firm_name"

# combine two data frames to make main_data include ticker symbols
merged_df <- merge(tickers_df, main_data, by = "firm_name")
head(merged_df)
write.csv(merged_df, "meng_with_tickers.csv")
