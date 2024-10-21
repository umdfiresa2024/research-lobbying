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

write.csv(companies, "flight_cleaned.csv", row.names=F)
companies

get_sec <- function(i) {
  tryCatch(
    #try to do this
    {
      name<- companies[i]
      name2<-str_replace_all(name, " ", "%20")
      api<-"67f15f74f937e7f6376252601326b292d0002f7e51431616c2b3a5384329c981"
      url<-paste0("https://api.sec-api.io/mapping/name/", name2, "?token=", api)
      
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
