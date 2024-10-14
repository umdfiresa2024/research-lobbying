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
print(data_long)

# Summarize GHG quantities by parent company
data_summary <- data_long %>%
  group_by(PARENT_COMPANY) %>%
  summarize(GHG_sum = sum(GHG_sum, na.rm = TRUE), .groups = 'drop')

# View the final summary
print(data_summary)
