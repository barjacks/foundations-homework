# Obsticles working with Swiss road accident from the past three years

#### SOURCE: Federal Roads Office of Switzerland [(FEDRO)](http://www.astra.admin.ch/?lang=en)

## Setting up the files
The data consists of 15 data sheets from 2011 to 2015, 5 sheets per year, with data on the vehicles, the people involved and the actual accidents. The size of the data files made an import difficult. And it turned out 2015 was formated slightl differently. Bevore I imported the data into Pandas, I made sure I deleted two extra columns and corrected some headers that were misspelt. Instead of Latin-1 encoding I used UTF-8. What I didn't touch were the date fields. These are formatted in a different way than the other years.

Once I had imported the files I concatenated them using the command: 
df_XXX = pd.concat([XXXXX, XXXXX, .....], ignore_index=True)

## Codes 
One the biggest challenges of this files ist that a lot of the information in it is coded. To understand the results we need to refer to [this data dictionary](https://docs.google.com/spreadsheets/d/1vjiEl-b6JOFxO3GrUDhSWDL1N5v3eRjIU8s0r9-WGFQ/edit#gid=1760004913) supplied by FEDRO. In some cases the encoding was easy to adapt in the Pandas Dataframe. But when FEDRO have put I am yet to manage to adapt the encoding (cf. question 3).

## Problems with queries
Groupy by 'Jahr' to find out a tendency:
Example: df_unfaelle.groupby('Jahr')[(df_unfaelle['Lichtverhältnis UAP'] == 622) & (df_unfaelle['Strassenbeleuchtung UAP'] == 641)]

Group by years to find our tendencies. 
Anoter data query.