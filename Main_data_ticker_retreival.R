install.packages(c("httr", "jsonlite"))
library(httr)
library(jsonlite)

# get the column of firm names from main data
companies<-as.vector(main_data$firm_name)
companies

# function to look up the ticker symbols from sec data and store the data of companies and symbols as data
get_sec <- function(i) {
  name<- companies[i]
  api<-"40f5fb11bbb19188a44e56e2f2d10fa8a20616e21beabb93d1f7b16e95fdef84"
  url<-paste0("https://api.sec-api.io/mapping/name/", name, "?token=", api)
  
  filename<-"sec_api/file.json"
  GET(url,write_disk(filename, overwrite = TRUE))
  
  data <- fromJSON(paste0("sec_api/",name))

  # if data doesn't have a ticker for a company, make that cell NA
  if (!is.null(data$ticker)) {
   ticker <- data$ticker[1]
   print(data$ticker[1])
   } else {
     return(NA)
   }
} 

# make a list of the tickers for all companies with look
tickers <- c()
for (i in companies) {
  print(i)
  ticker <- get_sec(i)
  tickers<-rbind(tickers, ticker)
}

# create dataframe of tickers
tickers_df <- data.frame(ticker = tickers)

# combine two data frames to make main_data include ticker symbols
main_data <- rbind(main_data, tickers_df)
head(main_data)

