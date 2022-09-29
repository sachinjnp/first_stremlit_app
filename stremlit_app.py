import streamlit;
import pandas;
import requests;
import snowflake.connector;
from urllib.error import URLError;

streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 & Blueberry Oatmeal")
streamlit.text("Kale, Spinach & Rocket Smoothie")
streamlit.text("Hard-Boiled Free-Range Egg")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)




#import requests

streamlit.header("Fruityvice Fruit Advice!")
#try:
  #if not fruit_choice :
    #stremlit.error("Please select a fruit to get details");
   # else:
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
      #streamlit.text(fruityvice_response.json())


      
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized);

# write your own comment -what does the next line do? 


# write your own comment - what does this do?

#except URLError as e:
  #streamlit.error();
#streamlite.stop();

  
fruit_choice = streamlit.text_input('What fruit would you like information about?',"Kiwi")
streamlit.write('The user entered ', fruit_choice);
if not fruit_choice:
  stremlit.error("Please select a fruit to get details")
else:
  stremlit.text("I got that")
  



#import snowflake.connector;

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from  fruit_load_list ");
my_data_row = my_cur.fetchone()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_row)
my_cur.execute("insert into  fruit_load_list values ('from streamlit')");

fruit_choice = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice);
streamlit.stop();
my_cur.execute("insert into  fruit_load_list values ('from streamlit')");



