import streamlit
streamlit.title('my parents new better menu')
streamlit.header(' new menu')
streamlit.text('eggs')
streamlit.header(' moms  menu')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
 
 
#lets put a pick list so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
 
   
  
  #new section to display fruityvice api response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header('Fruityvice Fruit Advice2')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# delete this line       streamlit.text(fruityvice_response.json())


#take the json version of the reponse and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the scree as a table
streamlit.dataframe(fruityvice_normalized)
#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice !')
fruit_choice = streamlit.text_input('what fruit would you like information about?', 'Kiwi')
streamlit.write('the user entered', fruit_choice)

import requests
fruityvice_repsonse = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("the fruit load list contains")
streamlit.text(my_data_row)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.header("the fruit load list contains")
streamlit.dataframe(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains")
streamlit.dataframe(my_data_rows
