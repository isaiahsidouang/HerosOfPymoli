{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Note\n",
    "* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies and Setup\n",
    "import pandas as pd\n",
    "import os\n",
    "# File to Load (Remember to Change These)\n",
    "file_to_load = \"../HerosOfPymoli/Resources/purchase_data.csv\"\n",
    "\n",
    "# Read Purchasing File and store into Pandas data frame\n",
    "purchase_data = pd.read_csv(file_to_load)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Player Count"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Display the total number of players\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "576"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#using len, count the total amount of players. \n",
    "#Not using \"Purchase ID\" becuase there is a space\n",
    "total_players = len(purchase_data[\"SN\"].value_counts())\n",
    "total_players"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Purchasing Analysis (Total)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Run basic calculations to obtain number of unique items, average price, etc.\n",
    "\n",
    "\n",
    "* Create a summary data frame to hold the results\n",
    "\n",
    "\n",
    "* Optional: give the displayed data cleaner formatting\n",
    "\n",
    "\n",
    "* Display the summary data frame\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>total_unique_items</th>\n",
       "      <th>average_price</th>\n",
       "      <th>total_number_of_purchases</th>\n",
       "      <th>total_revenue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>179</td>\n",
       "      <td>3.050987</td>\n",
       "      <td>780</td>\n",
       "      <td>2379.77</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   total_unique_items  average_price  total_number_of_purchases  total_revenue\n",
       "0                 179       3.050987                        780        2379.77"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Basic Calculations to obtain unique items\n",
    "total_unique_items = len(purchase_data[\"Item Name\"].unique())\n",
    "\n",
    "#Basic Calulations to obtain Average Price\n",
    "average_price = (purchase_data[\"Price\"].mean())\n",
    "\n",
    "#Basic Calculations to obtain total number of purchases\n",
    "total_number_of_purchases = len(purchase_data[\"Purchase ID\"])\n",
    "\n",
    "#Total Revenue\n",
    "total_revenue = (purchase_data[\"Price\"]).sum()\n",
    "\n",
    "#DataFrame holding the results\n",
    "purchasing_analysis_df = pd.DataFrame({\n",
    "    \"total_unique_items\": [total_unique_items],\n",
    "    \"average_price\": [average_price],\n",
    "    \"total_number_of_purchases\": [total_number_of_purchases],\n",
    "    \"total_revenue\": [total_revenue]}) \n",
    "\n",
    "\n",
    "purchasing_analysis_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Gender Demographics"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Percentage and Count of Male Players\n",
    "\n",
    "\n",
    "* Percentage and Count of Female Players\n",
    "\n",
    "\n",
    "* Percentage and Count of Other / Non-Disclosed\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Count</th>\n",
       "      <th>Percentage</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Male</th>\n",
       "      <td>484</td>\n",
       "      <td>84.03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Female</th>\n",
       "      <td>81</td>\n",
       "      <td>14.06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Other / Non-Disclosed</th>\n",
       "      <td>11</td>\n",
       "      <td>1.91</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Count  Percentage\n",
       "Male                     484       84.03\n",
       "Female                    81       14.06\n",
       "Other / Non-Disclosed     11        1.91"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gender_df = purchase_data[[\"Gender\",\"SN\"]].drop_duplicates()\n",
    "\n",
    "gender_count = gender_df[\"Gender\"].value_counts(0)\n",
    "gender_percentage = gender_df[\"Gender\"].value_counts(1)\n",
    "\n",
    "gender_count_df = pd.DataFrame(gender_count)\n",
    "gender_percentage_df = round(pd.DataFrame(gender_percentage) * 100, 2)\n",
    "\n",
    "summary_df = gender_count_df.merge(gender_percentage_df, left_index = True, right_index = True)\n",
    "summary_df.columns = [\"Count\", \"Percentage\"]\n",
    "\n",
    "\n",
    "summary_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## Purchasing Analysis (Gender)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "* Create a summary data frame to hold the results\n",
    "\n",
    "\n",
    "* Optional: give the displayed data cleaner formatting\n",
    "\n",
    "\n",
    "* Display the summary data frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Count per gender\n",
    "male = len(purchase_data.loc[purchase_data[\"Gender\"]==\"Male\", :])\n",
    "female = len(purchase_data.loc[purchase_data[\"Gender\"]==\"Female\", :])\n",
    "other = len(purchase_data.loc[purchase_data[\"Gender\"]==\"Other / Non-Disclosed\", :])\n",
    "\n",
    "other"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.3460000000000005"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Average Purchase Price per Gender\n",
    "male_average_price = purchase_data.loc[purchase_data[\"Gender\"]==\"Male\", \"Price\"].mean()\n",
    "female_average_price = purchase_data.loc[purchase_data[\"Gender\"]==\"Female\", \"Price\"].mean()\n",
    "other_avgerage_price = purchase_data.loc[purchase_data[\"Gender\"]==\"Other / Non-Disclosed\", \"Price\"].mean()\n",
    "\n",
    "other_avgerage_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50.19"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Total Purchase Value\n",
    "total_male_value = purchase_data.loc[purchase_data[\"Gender\"]==\"Male\", \"Price\"].sum()\n",
    "total_female_value = purchase_data.loc[purchase_data[\"Gender\"]==\"Female\", \"Price\"].sum()\n",
    "total_other_value = purchase_data.loc[purchase_data[\"Gender\"]==\"Other / Non-Disclosed\", \"Price\"].sum()\n",
    "\n",
    "total_other_value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50.19"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Average purchase total per gender\n",
    "\n",
    "male_avg_purchase_total = total_male_value / male\n",
    "female_avg_purchase_total = total_female_value / female\n",
    "other_avg_purchase_total = total_other_value / other\n",
    "\n",
    "total_other_value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Purchase Count</th>\n",
       "      <th>Average Purchase Price</th>\n",
       "      <th>Total Purchase Value</th>\n",
       "      <th>Avg Purchase Total Per Person</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Female</th>\n",
       "      <td>652</td>\n",
       "      <td>3.017853</td>\n",
       "      <td>1967.64</td>\n",
       "      <td>3.017853</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Male</th>\n",
       "      <td>113</td>\n",
       "      <td>3.203009</td>\n",
       "      <td>361.94</td>\n",
       "      <td>3.203009</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Other / Non-Disclosed</th>\n",
       "      <td>15</td>\n",
       "      <td>3.346000</td>\n",
       "      <td>50.19</td>\n",
       "      <td>3.346000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Purchase Count  Average Purchase Price  \\\n",
       "Female                            652                3.017853   \n",
       "Male                              113                3.203009   \n",
       "Other / Non-Disclosed              15                3.346000   \n",
       "\n",
       "                       Total Purchase Value  Avg Purchase Total Per Person  \n",
       "Female                              1967.64                       3.017853  \n",
       "Male                                 361.94                       3.203009  \n",
       "Other / Non-Disclosed                 50.19                       3.346000  "
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gender_df = pd.DataFrame(\n",
    "[[male, male_average_price, total_male_value, male_avg_purchase_total],\n",
    "[female, female_average_price, total_female_value, female_avg_purchase_total],\n",
    "[other, other_avgerage_price, total_other_value, other_avg_purchase_total]],\n",
    "index=[\"Female\",\"Male\", \"Other / Non-Disclosed\"],\n",
    "columns=[\"Purchase Count\", \"Average Purchase Price\", \"Total Purchase Value\", \"Avg Purchase Total Per Person\"])\n",
    "\n",
    "gender_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Age Demographics"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Establish bins for ages\n",
    "\n",
    "\n",
    "* Categorize the existing players using the age bins. Hint: use pd.cut()\n",
    "\n",
    "\n",
    "* Calculate the numbers and percentages by age group\n",
    "\n",
    "\n",
    "* Create a summary data frame to hold the results\n",
    "\n",
    "\n",
    "* Optional: round the percentage column to two decimal points\n",
    "\n",
    "\n",
    "* Display Age Demographics Table\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 9.9, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99, 99999]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Set bins for age \n",
    "bins = [0, 9.90, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99, 99999]\n",
    "\n",
    "bins"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bin_groups = [\"<10\",\"10-14\",\"15-19\",\"20-24\",\"25-29\",\"30-34\",\"35-39\",\"40+\"]\n",
    "\n",
    "bin_groups"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Purchase ID</th>\n",
       "      <th>SN</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Item ID</th>\n",
       "      <th>Item Name</th>\n",
       "      <th>Price</th>\n",
       "      <th>age group</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Lisim78</td>\n",
       "      <td>20</td>\n",
       "      <td>Male</td>\n",
       "      <td>108</td>\n",
       "      <td>Extraction, Quickblade Of Trembling Hands</td>\n",
       "      <td>3.53</td>\n",
       "      <td>20-24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Lisovynya38</td>\n",
       "      <td>40</td>\n",
       "      <td>Male</td>\n",
       "      <td>143</td>\n",
       "      <td>Frenzied Scimitar</td>\n",
       "      <td>1.56</td>\n",
       "      <td>40+</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Ithergue48</td>\n",
       "      <td>24</td>\n",
       "      <td>Male</td>\n",
       "      <td>92</td>\n",
       "      <td>Final Critic</td>\n",
       "      <td>4.88</td>\n",
       "      <td>20-24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Chamassasya86</td>\n",
       "      <td>24</td>\n",
       "      <td>Male</td>\n",
       "      <td>100</td>\n",
       "      <td>Blindscythe</td>\n",
       "      <td>3.27</td>\n",
       "      <td>20-24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Iskosia90</td>\n",
       "      <td>23</td>\n",
       "      <td>Male</td>\n",
       "      <td>131</td>\n",
       "      <td>Fury</td>\n",
       "      <td>1.44</td>\n",
       "      <td>20-24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>775</th>\n",
       "      <td>775</td>\n",
       "      <td>Aethedru70</td>\n",
       "      <td>21</td>\n",
       "      <td>Female</td>\n",
       "      <td>60</td>\n",
       "      <td>Wolf</td>\n",
       "      <td>3.54</td>\n",
       "      <td>20-24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>776</th>\n",
       "      <td>776</td>\n",
       "      <td>Iral74</td>\n",
       "      <td>21</td>\n",
       "      <td>Male</td>\n",
       "      <td>164</td>\n",
       "      <td>Exiled Doomblade</td>\n",
       "      <td>1.63</td>\n",
       "      <td>20-24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>777</th>\n",
       "      <td>777</td>\n",
       "      <td>Yathecal72</td>\n",
       "      <td>20</td>\n",
       "      <td>Male</td>\n",
       "      <td>67</td>\n",
       "      <td>Celeste, Incarnation of the Corrupted</td>\n",
       "      <td>3.46</td>\n",
       "      <td>20-24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>778</th>\n",
       "      <td>778</td>\n",
       "      <td>Sisur91</td>\n",
       "      <td>7</td>\n",
       "      <td>Male</td>\n",
       "      <td>92</td>\n",
       "      <td>Final Critic</td>\n",
       "      <td>4.19</td>\n",
       "      <td>&lt;10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>779</th>\n",
       "      <td>779</td>\n",
       "      <td>Ennrian78</td>\n",
       "      <td>24</td>\n",
       "      <td>Male</td>\n",
       "      <td>50</td>\n",
       "      <td>Dawn</td>\n",
       "      <td>4.60</td>\n",
       "      <td>20-24</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>780 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Purchase ID             SN  Age  Gender  Item ID  \\\n",
       "0              0        Lisim78   20    Male      108   \n",
       "1              1    Lisovynya38   40    Male      143   \n",
       "2              2     Ithergue48   24    Male       92   \n",
       "3              3  Chamassasya86   24    Male      100   \n",
       "4              4      Iskosia90   23    Male      131   \n",
       "..           ...            ...  ...     ...      ...   \n",
       "775          775     Aethedru70   21  Female       60   \n",
       "776          776         Iral74   21    Male      164   \n",
       "777          777     Yathecal72   20    Male       67   \n",
       "778          778        Sisur91    7    Male       92   \n",
       "779          779      Ennrian78   24    Male       50   \n",
       "\n",
       "                                     Item Name  Price age group  \n",
       "0    Extraction, Quickblade Of Trembling Hands   3.53     20-24  \n",
       "1                            Frenzied Scimitar   1.56       40+  \n",
       "2                                 Final Critic   4.88     20-24  \n",
       "3                                  Blindscythe   3.27     20-24  \n",
       "4                                         Fury   1.44     20-24  \n",
       "..                                         ...    ...       ...  \n",
       "775                                       Wolf   3.54     20-24  \n",
       "776                           Exiled Doomblade   1.63     20-24  \n",
       "777      Celeste, Incarnation of the Corrupted   3.46     20-24  \n",
       "778                               Final Critic   4.19       <10  \n",
       "779                                       Dawn   4.60     20-24  \n",
       "\n",
       "[780 rows x 8 columns]"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Categorize the existing players using the age bins using pd.cut()\n",
    "purchase_data[\"age group\"] = pd.cut(purchase_data[\"Age\"],bins, labels=bin_groups)\n",
    "\n",
    "purchase_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fa45014dc70>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "age_group = purchase_data.groupby(\"age group\")\n",
    "\n",
    "age_group"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age group\n",
       "<10       17\n",
       "10-14     22\n",
       "15-19    107\n",
       "20-24    258\n",
       "25-29     77\n",
       "30-34     52\n",
       "35-39     31\n",
       "40+       12\n",
       "Name: SN, dtype: int64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "total_age_count = age_group[\"SN\"].nunique()\n",
    "\n",
    "total_age_count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age group\n",
       "<10       2.951389\n",
       "10-14     3.819444\n",
       "15-19    18.576389\n",
       "20-24    44.791667\n",
       "25-29    13.368056\n",
       "30-34     9.027778\n",
       "35-39     5.381944\n",
       "40+       2.083333\n",
       "Name: SN, dtype: float64"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "age_percentage = (total_age_count/total_players) * 100\n",
    "\n",
    "age_percentage"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Percentage of Players</th>\n",
       "      <th>Total Count</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>age group</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>&lt;10</th>\n",
       "      <td>2.951389</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10-14</th>\n",
       "      <td>3.819444</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15-19</th>\n",
       "      <td>18.576389</td>\n",
       "      <td>107</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20-24</th>\n",
       "      <td>44.791667</td>\n",
       "      <td>258</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25-29</th>\n",
       "      <td>13.368056</td>\n",
       "      <td>77</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30-34</th>\n",
       "      <td>9.027778</td>\n",
       "      <td>52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35-39</th>\n",
       "      <td>5.381944</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40+</th>\n",
       "      <td>2.083333</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Percentage of Players  Total Count\n",
       "age group                                    \n",
       "<10                     2.951389           17\n",
       "10-14                   3.819444           22\n",
       "15-19                  18.576389          107\n",
       "20-24                  44.791667          258\n",
       "25-29                  13.368056           77\n",
       "30-34                   9.027778           52\n",
       "35-39                   5.381944           31\n",
       "40+                     2.083333           12"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Create DataFrame\n",
    "age_demographics_df = pd.DataFrame({\"Percentage of Players\": age_percentage, \"Total Count\": total_age_count})\n",
    "\n",
    "age_demographics_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Purchasing Analysis (Age)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Bin the purchase_data data frame by age\n",
    "\n",
    "\n",
    "* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below\n",
    "\n",
    "\n",
    "* Create a summary data frame to hold the results\n",
    "\n",
    "\n",
    "* Optional: give the displayed data cleaner formatting\n",
    "\n",
    "\n",
    "* Display the summary data frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fa4813035b0>"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Purchasing Analysis by age\n",
    "age_group = purchase_data.groupby(\"age group\")\n",
    "age_group"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age group\n",
       "<10       23\n",
       "10-14     28\n",
       "15-19    136\n",
       "20-24    365\n",
       "25-29    101\n",
       "30-34     73\n",
       "35-39     41\n",
       "40+       13\n",
       "Name: age group, dtype: int64"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Getting Purchase Count\n",
    "purchase_count = age_group[\"age group\"].count()\n",
    "purchase_count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age group\n",
       "<10      3.353478\n",
       "10-14    2.956429\n",
       "15-19    3.035956\n",
       "20-24    3.052219\n",
       "25-29    2.900990\n",
       "30-34    2.931507\n",
       "35-39    3.601707\n",
       "40+      2.941538\n",
       "Name: Price, dtype: float64"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Getting Avg. Purchase Price\n",
    "average_purchase_price = age_group[\"Price\"].mean()\n",
    "\n",
    "average_purchase_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age group\n",
       "<10        77.13\n",
       "10-14      82.78\n",
       "15-19     412.89\n",
       "20-24    1114.06\n",
       "25-29     293.00\n",
       "30-34     214.00\n",
       "35-39     147.67\n",
       "40+        38.24\n",
       "Name: Price, dtype: float64"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Getting Avg. Purchase Total per Age\n",
    "toal_purchase_value = age_group[\"Price\"].sum()\n",
    "\n",
    "toal_purchase_value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age group\n",
       "<10      0.133906\n",
       "10-14    0.143715\n",
       "15-19    0.716823\n",
       "20-24    1.934132\n",
       "25-29    0.508681\n",
       "30-34    0.371528\n",
       "35-39    0.256372\n",
       "40+      0.066389\n",
       "Name: Price, dtype: float64"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avg_total_purchase_per_person =  purchase_data.groupby([\"age group\", \"SN\"])[\"Price\"].sum().groupby([\"age group\"]).mean()\n",
    "\n",
    "avg_total_purchase_per_person"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Purchase Count</th>\n",
       "      <th>Average Purchase Price</th>\n",
       "      <th>Average Purchase Total Value</th>\n",
       "      <th>Avg Total Purchase Per Person</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>age group</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>&lt;10</th>\n",
       "      <td>23</td>\n",
       "      <td>3.353478</td>\n",
       "      <td>77.13</td>\n",
       "      <td>0.133906</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10-14</th>\n",
       "      <td>28</td>\n",
       "      <td>2.956429</td>\n",
       "      <td>82.78</td>\n",
       "      <td>0.143715</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15-19</th>\n",
       "      <td>136</td>\n",
       "      <td>3.035956</td>\n",
       "      <td>412.89</td>\n",
       "      <td>0.716823</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20-24</th>\n",
       "      <td>365</td>\n",
       "      <td>3.052219</td>\n",
       "      <td>1114.06</td>\n",
       "      <td>1.934132</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25-29</th>\n",
       "      <td>101</td>\n",
       "      <td>2.900990</td>\n",
       "      <td>293.00</td>\n",
       "      <td>0.508681</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30-34</th>\n",
       "      <td>73</td>\n",
       "      <td>2.931507</td>\n",
       "      <td>214.00</td>\n",
       "      <td>0.371528</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35-39</th>\n",
       "      <td>41</td>\n",
       "      <td>3.601707</td>\n",
       "      <td>147.67</td>\n",
       "      <td>0.256372</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40+</th>\n",
       "      <td>13</td>\n",
       "      <td>2.941538</td>\n",
       "      <td>38.24</td>\n",
       "      <td>0.066389</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Purchase Count  Average Purchase Price  \\\n",
       "age group                                           \n",
       "<10                    23                3.353478   \n",
       "10-14                  28                2.956429   \n",
       "15-19                 136                3.035956   \n",
       "20-24                 365                3.052219   \n",
       "25-29                 101                2.900990   \n",
       "30-34                  73                2.931507   \n",
       "35-39                  41                3.601707   \n",
       "40+                    13                2.941538   \n",
       "\n",
       "           Average Purchase Total Value  Avg Total Purchase Per Person  \n",
       "age group                                                               \n",
       "<10                               77.13                       0.133906  \n",
       "10-14                             82.78                       0.143715  \n",
       "15-19                            412.89                       0.716823  \n",
       "20-24                           1114.06                       1.934132  \n",
       "25-29                            293.00                       0.508681  \n",
       "30-34                            214.00                       0.371528  \n",
       "35-39                            147.67                       0.256372  \n",
       "40+                               38.24                       0.066389  "
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Display DataFrame\n",
    "age_purchasing_analysis_df = pd.DataFrame({\"Purchase Count\": purchase_count,\n",
    "                                            \"Average Purchase Price\": average_purchase_price,\n",
    "                                            \"Average Purchase Total Value\": toal_purchase_value,\n",
    "                                            \"Avg Total Purchase Per Person\": avg_total_purchase_per_person})\n",
    "\n",
    "age_purchasing_analysis_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Top Spenders"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Run basic calculations to obtain the results in the table below\n",
    "\n",
    "\n",
    "* Create a summary data frame to hold the results\n",
    "\n",
    "\n",
    "* Sort the total purchase value column in descending order\n",
    "\n",
    "\n",
    "* Optional: give the displayed data cleaner formatting\n",
    "\n",
    "\n",
    "* Display a preview of the summary data frame\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fa45014d790>"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Group data by screen name\n",
    "top_spenders_stats = purchase_data.groupby(\"SN\")\n",
    "\n",
    "top_spenders_stats"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SN\n",
       "Adairialis76     1\n",
       "Adastirin33      1\n",
       "Aeda94           1\n",
       "Aela59           1\n",
       "Aelaria33        1\n",
       "                ..\n",
       "Yathecal82       3\n",
       "Yathedeu43       2\n",
       "Yoishirrala98    1\n",
       "Zhisrisu83       2\n",
       "Zontibe81        3\n",
       "Name: Purchase ID, Length: 576, dtype: int64"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#define Purchase Count Variable\n",
    "number_of_purchases = top_spenders_stats[\"Purchase ID\"].count()\n",
    "\n",
    "number_of_purchases"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SN\n",
       "Adairialis76     2.280000\n",
       "Adastirin33      4.480000\n",
       "Aeda94           4.910000\n",
       "Aela59           4.320000\n",
       "Aelaria33        1.790000\n",
       "                   ...   \n",
       "Yathecal82       2.073333\n",
       "Yathedeu43       3.010000\n",
       "Yoishirrala98    4.580000\n",
       "Zhisrisu83       3.945000\n",
       "Zontibe81        2.676667\n",
       "Name: Price, Length: 576, dtype: float64"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Find Average Purchase Price per Top Spender\n",
    "\n",
    "avg_purchase_price_top_spender = top_spenders_stats[\"Price\"].mean()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SN\n",
       "Adairialis76     2.28\n",
       "Adastirin33      4.48\n",
       "Aeda94           4.91\n",
       "Aela59           4.32\n",
       "Aelaria33        1.79\n",
       "                 ... \n",
       "Yathecal82       6.22\n",
       "Yathedeu43       6.02\n",
       "Yoishirrala98    4.58\n",
       "Zhisrisu83       7.89\n",
       "Zontibe81        8.03\n",
       "Name: Price, Length: 576, dtype: float64"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Total Purchase Value\n",
    "\n",
    "purchase_total_top_spender = top_spenders_stats[\"Price\"].sum()\n",
    "\n",
    "purchase_total_top_spender"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Purchase Count</th>\n",
       "      <th>Average Purchase Price</th>\n",
       "      <th>Total Purchase Value</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SN</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Lisosia93</th>\n",
       "      <td>5</td>\n",
       "      <td>3.792000</td>\n",
       "      <td>18.96</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Idastidru52</th>\n",
       "      <td>4</td>\n",
       "      <td>3.862500</td>\n",
       "      <td>15.45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Chamjask73</th>\n",
       "      <td>3</td>\n",
       "      <td>4.610000</td>\n",
       "      <td>13.83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Iral74</th>\n",
       "      <td>4</td>\n",
       "      <td>3.405000</td>\n",
       "      <td>13.62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Iskadarya95</th>\n",
       "      <td>3</td>\n",
       "      <td>4.366667</td>\n",
       "      <td>13.10</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Purchase Count  Average Purchase Price  Total Purchase Value\n",
       "SN                                                                       \n",
       "Lisosia93                 5                3.792000                 18.96\n",
       "Idastidru52               4                3.862500                 15.45\n",
       "Chamjask73                3                4.610000                 13.83\n",
       "Iral74                    4                3.405000                 13.62\n",
       "Iskadarya95               3                4.366667                 13.10"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Create DataFrame\n",
    "top_five_spenders = pd.DataFrame({\"Purchase Count\": number_of_purchases,\n",
    "                             \"Average Purchase Price\": avg_purchase_price_top_spender,\n",
    "                             \"Total Purchase Value\":purchase_total_top_spender})\n",
    "\n",
    "top_five_spenders.sort_values(\"Total Purchase Value\", ascending = False, inplace=True)\n",
    "\n",
    "top_five_spenders.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Most Popular Items"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Retrieve the Item ID, Item Name, and Item Price columns\n",
    "\n",
    "\n",
    "* Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value\n",
    "\n",
    "\n",
    "* Create a summary data frame to hold the results\n",
    "\n",
    "\n",
    "* Sort the purchase count column in descending order\n",
    "\n",
    "\n",
    "* Optional: give the displayed data cleaner formatting\n",
    "\n",
    "\n",
    "* Display a preview of the summary data frame\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>Purchase Count</th>\n",
       "      <th>Item Price</th>\n",
       "      <th>Total Purchase Value</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Item ID</th>\n",
       "      <th>Item Name</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>92</th>\n",
       "      <th>Final Critic</th>\n",
       "      <td>13</td>\n",
       "      <td>4.614615</td>\n",
       "      <td>59.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>178</th>\n",
       "      <th>Oathbreaker, Last Hope of the Breaking Storm</th>\n",
       "      <td>12</td>\n",
       "      <td>4.230000</td>\n",
       "      <td>50.76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>145</th>\n",
       "      <th>Fiery Glass Crusader</th>\n",
       "      <td>9</td>\n",
       "      <td>4.580000</td>\n",
       "      <td>41.22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>132</th>\n",
       "      <th>Persuasion</th>\n",
       "      <td>9</td>\n",
       "      <td>3.221111</td>\n",
       "      <td>28.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>108</th>\n",
       "      <th>Extraction, Quickblade Of Trembling Hands</th>\n",
       "      <td>9</td>\n",
       "      <td>3.530000</td>\n",
       "      <td>31.77</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                      Purchase Count  \\\n",
       "Item ID Item Name                                                      \n",
       "92      Final Critic                                              13   \n",
       "178     Oathbreaker, Last Hope of the Breaking Storm              12   \n",
       "145     Fiery Glass Crusader                                       9   \n",
       "132     Persuasion                                                 9   \n",
       "108     Extraction, Quickblade Of Trembling Hands                  9   \n",
       "\n",
       "                                                      Item Price  \\\n",
       "Item ID Item Name                                                  \n",
       "92      Final Critic                                    4.614615   \n",
       "178     Oathbreaker, Last Hope of the Breaking Storm    4.230000   \n",
       "145     Fiery Glass Crusader                            4.580000   \n",
       "132     Persuasion                                      3.221111   \n",
       "108     Extraction, Quickblade Of Trembling Hands       3.530000   \n",
       "\n",
       "                                                      Total Purchase Value  \n",
       "Item ID Item Name                                                           \n",
       "92      Final Critic                                                 59.99  \n",
       "178     Oathbreaker, Last Hope of the Breaking Storm                 50.76  \n",
       "145     Fiery Glass Crusader                                         41.22  \n",
       "132     Persuasion                                                   28.99  \n",
       "108     Extraction, Quickblade Of Trembling Hands                    31.77  "
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "most_popular_items = purchase_data.groupby([\"Item ID\", \"Item Name\"])\n",
    "\n",
    "most_popular_count = most_popular_items[\"Price\"].count()\n",
    "total_purchase_value = most_popular_items[\"Price\"].sum()\n",
    "average_item_price = total_purchase_value/most_popular_count\n",
    "\n",
    "most_popular_items = pd.DataFrame({\"Purchase Count\" : most_popular_count,\n",
    "                                  \"Item Price\": average_item_price,\n",
    "                                  \"Total Purchase Value\": total_purchase_value})\n",
    "\n",
    "most_popular_items = most_popular_items.sort_values(\"Purchase Count\", ascending=False)\n",
    "\n",
    "most_popular_items.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Most Profitable Items"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Sort the above table by total purchase value in descending order\n",
    "\n",
    "\n",
    "* Optional: give the displayed data cleaner formatting\n",
    "\n",
    "\n",
    "* Display a preview of the data frame\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>Purchase Count</th>\n",
       "      <th>Item Price</th>\n",
       "      <th>Total Purchase Value</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Item ID</th>\n",
       "      <th>Item Name</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>92</th>\n",
       "      <th>Final Critic</th>\n",
       "      <td>13</td>\n",
       "      <td>4.614615</td>\n",
       "      <td>59.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>178</th>\n",
       "      <th>Oathbreaker, Last Hope of the Breaking Storm</th>\n",
       "      <td>12</td>\n",
       "      <td>4.230000</td>\n",
       "      <td>50.76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>82</th>\n",
       "      <th>Nirvana</th>\n",
       "      <td>9</td>\n",
       "      <td>4.900000</td>\n",
       "      <td>44.10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>145</th>\n",
       "      <th>Fiery Glass Crusader</th>\n",
       "      <td>9</td>\n",
       "      <td>4.580000</td>\n",
       "      <td>41.22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>103</th>\n",
       "      <th>Singed Scalpel</th>\n",
       "      <td>8</td>\n",
       "      <td>4.350000</td>\n",
       "      <td>34.80</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                      Purchase Count  \\\n",
       "Item ID Item Name                                                      \n",
       "92      Final Critic                                              13   \n",
       "178     Oathbreaker, Last Hope of the Breaking Storm              12   \n",
       "82      Nirvana                                                    9   \n",
       "145     Fiery Glass Crusader                                       9   \n",
       "103     Singed Scalpel                                             8   \n",
       "\n",
       "                                                      Item Price  \\\n",
       "Item ID Item Name                                                  \n",
       "92      Final Critic                                    4.614615   \n",
       "178     Oathbreaker, Last Hope of the Breaking Storm    4.230000   \n",
       "82      Nirvana                                         4.900000   \n",
       "145     Fiery Glass Crusader                            4.580000   \n",
       "103     Singed Scalpel                                  4.350000   \n",
       "\n",
       "                                                      Total Purchase Value  \n",
       "Item ID Item Name                                                           \n",
       "92      Final Critic                                                 59.99  \n",
       "178     Oathbreaker, Last Hope of the Breaking Storm                 50.76  \n",
       "82      Nirvana                                                      44.10  \n",
       "145     Fiery Glass Crusader                                         41.22  \n",
       "103     Singed Scalpel                                               34.80  "
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Format the previous DataFrame to show Total Purchase Value in decending order\n",
    "most_popular_items = most_popular_items.sort_values([\"Total Purchase Value\"],\n",
    "                                                   ascending=False).head()\n",
    "\n",
    "#Display the new DataFrame with the top 5 results\n",
    "most_popular_items.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pop_count' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-95-7928d1c11daf>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# Create new DataFrame name using variables from previous code block\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mprof_df\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mDataFrame\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m{\u001b[0m\u001b[0;34m\"Purchase Count\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mpop_count\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"Avg Item Price\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mpop_price\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"Total Purchase Value\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mpop_tot\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;31m# Sort by Total Purchase Value\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mprof_df\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msort_values\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Total Purchase Value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mascending\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mFalse\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0minplace\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'pop_count' is not defined"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernel_info": {
   "name": "python3"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "latex_envs": {
   "LaTeX_envs_menu_present": true,
   "autoclose": false,
   "autocomplete": true,
   "bibliofile": "biblio.bib",
   "cite_by": "apalike",
   "current_citInitial": 1,
   "eqLabelWithNumbers": true,
   "eqNumInitial": 1,
   "hotkeys": {
    "equation": "Ctrl-E",
    "itemize": "Ctrl-I"
   },
   "labels_anchors": false,
   "latex_user_defs": false,
   "report_style_numbering": false,
   "user_envs_cfg": false
  },
  "nteract": {
   "version": "0.2.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
