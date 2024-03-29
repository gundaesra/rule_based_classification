
# Rule-Based Classification for Calculating Potential Customer Yield

# Business Problem

A game company wants to create level-based new customer definitions (personas) by using some characteristics of its customers, create segments according to these new customer definitions, and estimate how much new customers can bring to the company on average based on these segments.

For example: It is desired to determine how much money a 25-year-old male user from Turkey, who is an IOS user, can save to company on average.

# Dataset Story

Persona.csv data set contains the prices of the products sold by an international game company and some demographic information of the users who purchased these products. The data set consists of records created in each sales transaction. This means the table is not deduplicated. In other words, a user with certain demographic characteristics may have made more than one purchase.

Price: Customer's spending amount
Source: The type of device the customer is connected to
Sex: Customer's gender
Country: Customer's country
Age: Customer's age

# Before Application

| PRICE | SOURCE  | SEX  | COUNTRY | AGE |
|-------|---------|------|---------|-----|
| 39    | android | male | bra     | 17  |
| 39    | android | male | bra     | 17  |
| 49    | android | male | bra     | 17  |
| 29    | android | male | tur     | 17  |
| 49    | android | male | tur     | 17  |

# After Application

| customers_level_based       | PRICE      | SEGMENT |
|-----------------------------|------------|---------|
| BRA_ANDROID_FEMALE_0_18     | 1139.80    | A       |
| BRA_ANDROID_FEMALE_19_23    | 1070.60    | A       |
| BRA_ANDROID_FEMALE_24_30    | 508.14     | A       |
| BRA_ANDROID_FEMALE_31_40    | 233.17     | C       |
| BRA_ANDROID_FEMALE_41_66    | 236.67     | C       |

