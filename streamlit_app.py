import streamlit
import pandas
import requests
import snowflake.connector
streamlit.title('my parents new better menu')
streamlit.header(' new menu')
streamlit.text('cantaloupe')
streamlit.header(' moms  menu')


#import pandas
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
#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice !')
try:
    fruit_choice = streamlit.text_input('what fruit would you like information about?')
    if not fruit_choice:
       streamlit.error("Please enter a fruit to get information")
    else:
       fruityvice_repsonse = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
       fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       streamlit.dataframe(fruityvice_normalized)
  except URLError as e:
       streamlit.error()
   
   
   
  #import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)

streamlit.header('Fruityvice Fruit Advice2')
#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "cantaloupe")
# delete this line       streamlit.text(fruityvice_response.json())


#take the json version of the reponse and normalize it
 
#output it the screen as a table
streamlit.dataframe(fruityvice_normalized)
#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice !')
fruit_choice = streamlit.text_input('what fruit would you like information about?')
streamlit.write('the user entered', fruit_choice)
fruityvice_repsonse = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
#import snowflake.connector

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
streamlit.dataframe(my_data_rows)

fruit_choice = streamlit.text_input('what fruit would you like to add?', 'cantaloupe')
streamlit.write('Thanks for entering ', fruit_choice)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")

# dont run anything past here while we troubleshoot
streamlit.stop()
#import snowflake.connector
my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.datafram(my_data_rows)
