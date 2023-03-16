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


