library(tidyverse)

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
data_long <- data_long %>%
  mutate(percentage = str_extract(`PARENT_COMPANY`, "\\d+(\\.\\d+)?%"))

# Remove percentage information from the parent company names
data_long <- data_long %>%
  mutate(percentage = str_extract(`PARENT_COMPANY`, "\\d+(\\.\\d+)?%"),
         `PARENT_COMPANY` = str_remove(`PARENT_COMPANY`, "\\s*\\(\\d+(\\.\\d+)?%\\)"))

# Convert percentage to numeric
data_long <- data_long %>%
  mutate(numeric_percentage = as.numeric(gsub("%", "", percentage)) / 100)

# Convert GHG quantity to numeric
data_long <- data_long %>%
  mutate(GHG.QUANTITY..METRIC.TONS.CO2e. = as.numeric(GHG.QUANTITY..METRIC.TONS.CO2e.))

# Replace & with and, drop all punctuation, convert to lowercase, remove all spaces, and standardize company names
data_long <- data_long %>%
  mutate(PARENT_COMPANY = str_replace_all(PARENT_COMPANY, "&", "and")) %>%  # Replace & with and
  mutate(standardized_company = tolower(gsub("[[:punct:]]", "", PARENT_COMPANY))) %>%  # Drop all punctuation
  mutate(standardized_company = gsub("\\s+", "", standardized_company)) %>%  # Remove all spaces
  mutate(GHG=GHG.QUANTITY..METRIC.TONS.CO2e.*numeric_percentage) %>%
  group_by(standardized_company) %>%
  summarize(
    GHG_sum = sum(GHG, na.rm = TRUE),
    PARENT_COMPANY = first(PARENT_COMPANY)
  ) %>%
  # Drop the standardized column
  ungroup() %>%
  select(-standardized_company)

#feed company name into ticker
com<-unique(data_long$PARENT_COMPANY)

library("httr")
for (i in 1:length(com)) {
  print(i)
  name<-com[i]
  api<-"67f15f74f937e7f6376252601326b292d0002f7e51431616c2b3a5384329c981"
  url<-paste0("https://api.sec-api.io/mapping/name/", name, "?token=", api)
  filename<-paste0("flight_sec/row_", i, ".json")
  GET(url,write_disk(filename, overwrite = TRUE)) 
}

