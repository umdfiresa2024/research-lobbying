library(tidyverse)
library(httr)
library(jsonlite)

# Read the CSV file
combined_data <- read.csv("flight_2010.csv")

# Select specific columns
select_col <- combined_data %>%
  select(GHG.QUANTITY..METRIC.TONS.CO2e., PARENT.COMPANIES)

# Separate parent companies into multiple columns
new_data <- select_col %>%
  separate("PARENT.COMPANIES", into = paste0("PARENT_COMPANY ", 1:3), sep = "; ", fill = "right")

# Pivot the data to a long format
data_long <- new_data %>%
  pivot_longer(cols = starts_with("PARENT"),
               names_to = "COMPANY TYPE",
               values_to = "PARENT_COMPANY")

# Extract the percentage from the parent company names
data_long2 <- data_long %>%
  mutate(percentage = str_extract(`PARENT_COMPANY`, "\\d+(\\.\\d+)?%"))

# Remove percentage information from the parent company names
data_long3 <- data_long2 %>%
  mutate(percentage = str_extract(`PARENT_COMPANY`, "\\d+(\\.\\d+)?%"),
         `PARENT_COMPANY` = str_remove(`PARENT_COMPANY`, "\\s*\\(\\d+(\\.\\d+)?%\\)"))

# Convert percentage to numeric
data_long4 <- data_long3 %>%
  mutate(numeric_percentage = as.numeric(gsub("%", "", percentage)) / 100)

# Convert GHG quantity to numeric
data_long5 <- data_long4 %>%
  mutate(GHG.QUANTITY..METRIC.TONS.CO2e. = as.numeric(GHG.QUANTITY..METRIC.TONS.CO2e.))

# Replace & with and, drop all punctuation, convert to lowercase, remove all spaces, and standardize company names
data_long6 <- data_long5 %>%
  mutate(PARENT_COMPANY = str_replace_all(PARENT_COMPANY, "&", "and")) %>%  # Replace & with and
  mutate(standardized_company = tolower(gsub("[[:punct:]]", "", PARENT_COMPANY))) %>%  # Drop all punctuation
  mutate(standardized_company = gsub("\\s+", "", standardized_company)) %>%  # Remove all spaces
  filter(PARENT_COMPANY!="") %>%
  group_by(standardized_company) %>%
  summarize(
    GHG_sum = sum(GHG.QUANTITY..METRIC.TONS.CO2e.*numeric_percentage, na.rm = TRUE),
    PARENT_COMPANY = first(PARENT_COMPANY)
  ) %>%
  # Drop the standardized column
  ungroup() 

# View the summarized data

companies<-as.vector(data_long6$PARENT_COMPANY)
companies

get_sec <- function(i) {
  tryCatch(
    #try to do this
    {
      name<- companies[i]
      api<-"0b2ca623403335d8c3d2e75932b87231a96f7fa6e3d7e68f569edf05fd614e97"
      url<-paste0("https://api.sec-api.io/mapping/name/", name, "?token=", api)
      
      filename<-"flight_sec/file.json"
      GET(url,write_disk(filename, overwrite = TRUE))
      
      data <- fromJSON("flight_sec/file.json")
      
      # if data doesn't have a ticker for a company, make that cell NA
      if (!is.null(data$ticker)) {
        ticker <- data$ticker[1]
        print(data$ticker[1])
      } else {
        ticker <- NA
      }
      
    },
    #if an error occurs, tell me the error
    error=function(e) {
      message('An Error Occurred')
      print(e)
    },
    #if a warning occurs, tell me the warning
    warning=function(w) {
      message('A Warning Occurred')
      print(w)
      return(NA)
    }
  )
}

# function to look up the ticker symbols from sec data and store the data of companies and symbols as data
get_sec <- function(i) {
  name<- companies[i]
  api<-"0b2ca623403335d8c3d2e75932b87231a96f7fa6e3d7e68f569edf05fd614e97"
  url<-paste0("https://api.sec-api.io/mapping/name/", name, "?token=", api)
  
  filename<-"flight_sec/file.json"
  GET(url,write_disk(filename, overwrite = TRUE))
  
  data <- fromJSON("flight_sec/file.json")
  
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
for (i in 1:5) {
  print(i)
  ticker <- get_sec(i)
  tickers<-rbind(tickers, ticker)
}

# create dataframe of tickers
tickers_df <- data.frame(ticker = tickers)

#write.csv(tickers_df, "sec_api/tickers_df_1_5.csv", row.names = F)
