### Pandas command
/Users/kit/Dropbox/cheaters-master/cheaters/cheatsheets/pandas.md

/Users/kit/Dropbox/cheaters-master/cheaters/index-example.html


Pandas Command|Description
--|--
pd.pivot_table |
df['column_name'].unique() | display unique list
df[['column1_name','column2_name']] | display two or more columns

Pandas Navigation/filter | Description
--|--
df[df['column_name'] == True] | filter
df.sort_values(by=['columns_name'],ascending=[True/False]) | sort by value
df.loc[df['col_name'] == 'xxx'] | display records with the records

Dataframe manipulation|Description
--|--
df.append(df2)|join dataframe
df = pd.concat(df,axis=0,ignore_index=True)|Merge list of dataframe into a single big df, axis0 mean merge as rows


String manipulation|Description
--|--
str.strip() | remove all the white space
pd.to_numeric(xxx,errors="coerce") | force convert to number
str.replace(",","") | replace "," to ""
str.index(" ") | return the character position

list manupulation|Description
--|--
list_name.append() | create a list_name = list() and add items to it
