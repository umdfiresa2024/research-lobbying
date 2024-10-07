library(tidyverse)

combined_data <- read.csv("flight_2010.csv")

select_col <- combined_data %>%
  select(GHG.QUANTITY..METRIC.TONS.CO2e., PARENT.COMPANIES)

new_data <- select_col %>%
  separate("PARENT.COMPANIES", into = paste0("PARENT_COMPANY ", 1:3), sep = "; ", fill = "right")

data_long <- new_data %>%
  pivot_longer(cols = starts_with("PARENT"),
               names_to = "COMPANY TYPE",
               values_to = "PARENT_COMPANY")

data_long <- data_long %>%
  mutate(percentage = str_extract(`PARENT_COMPANY`, "\\d+(\\.\\d+)?%"))

data_long <- data_long %>%
  mutate(percentage = str_extract(`PARENT_COMPANY`, "\\d+(\\.\\d+)?%"),
         `PARENT_COMPANY` = str_remove(`PARENT_COMPANY`, "\\s*\\(\\d+(\\.\\d+)?%\\)"))

data_long <- data_long %>%
  mutate(numeric_percentage = as.numeric(gsub("%", "", percentage)) / 100)

data_long <- data_long %>%
  mutate(GHG.QUANTITY..METRIC.TONS.CO2e. = as.numeric(GHG.QUANTITY..METRIC.TONS.CO2e.))

data_long <- data_long %>%
  mutate(standardized_company = tolower(gsub("[[:punct:]\\s]+", "", PARENT_COMPANY))) %>%
  group_by(standardized_company) %>%
  summarize(
    GHG_sum = sum(GHG.QUANTITY..METRIC.TONS.CO2e., na.rm = TRUE),
    PARENT_COMPANY = first(PARENT_COMPANY)
  ) %>%
  # Drop the standardized column
  ungroup() %>%
  select(-standardized_company)

# View the summarized data
print(data_long)

data_summary <- data_long %>%
  group_by(PARENT_COMPANY) %>%
  summarize(GHG_sum = sum(GHG_sum, na.rm = TRUE), .groups = 'drop')

