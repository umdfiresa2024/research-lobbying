library(tidyverse)
library(stringdist)

# Read the CSV file
combined_data <- read.csv("flight_2010.csv")

# Select specific columns
select_col <- combined_data %>% select(GHG.QUANTITY..METRIC.TONS.CO2e., PARENT.COMPANIES)

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
  mutate(PARENT_COMPANY=toupper(PARENT_COMPANY)) %>%
  mutate(PARENT_COMPANY=str_remove_all(PARENT_COMPANY,"COMPANY")) %>%
  mutate(PARENT_COMPANY=str_remove_all(PARENT_COMPANY,"CORPORATION")) %>%
  mutate(PARENT_COMPANY=str_remove_all(PARENT_COMPANY,", INC")) %>%
  mutate(PARENT_COMPANY=str_remove_all(PARENT_COMPANY,"INC.")) %>%
  # Drop the standardized column
  ungroup() 

write.csv(companies, "flight_cleaned.csv", row.names=F)

#####Fuzzy Merge#############################################################
library(stringdist)

flight.name = data_long6$PARENT_COMPANY

flight.name<-as.data.frame(flight.name)

tickers<-read.csv("finaldatasets/3. join naics with ghgs/final.csv")

com_w_ticks<-tickers$Company

flight_output<-c()

for(i in 1:nrow(flight.name)) {
#for(i in 1:100) {
  print(i)
  
  distmatrix <- stringdist::stringdistmatrix(flight.name[i,],
                                             com_w_ticks,
                                             method='lcs',
                                             p=0.1)
  best_fit <- apply(distmatrix,1,which.min) %>% as.integer()
  similarity <- apply(distmatrix,1,min)
  output<-as.data.frame(cbind(flight.name[i,], com_w_ticks[best_fit], round(similarity,3)))
  flight_output<-rbind(flight_output, output)
                      
}

flight<-flight_output %>%
  mutate(V3=as.numeric(V3)) |>
  arrange(V3) 

flight_match<-flight |>
  filter(V3<=1)

flight_match2<-flight |>
  filter(V3>1 &V3<=5) |>
  group_by(V2) |>
  mutate(obs=n()) |>
  arrange(obs, V2) |>
  filter(V2!="CMS ENERGY") |>
  filter(V2!="CVR ENERGY") |>
  filter(V2!="NV ENERGY") |>
  filter(V2!="VALE SA") |>
  filter(V2 !="DTE ENERGY") |>
  filter(V2 !="AMEREN") |>
  filter(V2 != "GEVO")

flight_match3<-bind_rows(flight_match, flight_match2) |>
  rename(PARENT_COMPANY=V1) |>
  rename(Company=V2)

#################merge data back################################################
flight_tick<-merge(flight_match3, tickers, by="Company")  |>
  select(Company, PARENT_COMPANY, Ticker)

flight_tick2<-merge(flight_tick, data_long6, by="PARENT_COMPANY") |>
  group_by(Ticker) |>
  summarise(GHG_TR=sum(GHG_sum))

#check tickers GHG
check<-merge(flight_tick2, tickers, by="Ticker") |>
  mutate(pct_df=(Total.GHG-GHG_TR)*100 / GHG_TR) |>
  filter(abs(pct_df)<20)

#124 out of 182 has less than 20 percent difference