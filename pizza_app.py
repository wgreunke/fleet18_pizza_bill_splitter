#This app helps fleet 18 split the pizza and beer bill after sailing on a Tuesday night at Foster City

#Everyone eats pizza but only some people drink beer.  Find the portion of the bill attributed to each per person and then add each persons total.
#Assume tax is applied to both pizza and beer.

#inputs- number of people, total bill, pizza bill, beer bill.

import streamlit as st
st.title("Pizza and Beer Calculator for Fleet 18")
#Collect the data
total_bill=st.number_input('What is the total bill: Pizza + Beer.  Include tax.')
st.subheader("Pizza")
pizza_pre_tax=st.number_input('What was the amount of the pizza wihout tax?')
pizza_num=st.number_input('How many people ate pizza?',step=1)

st.subheader("Beer")
beer_pre_tax=st.number_input('What was the amount of the beer?')
beer_num=st.number_input('How many people drank beer?',step=1)

#Do the math
pizza_ratio=(pizza_pre_tax)/(pizza_pre_tax+beer_pre_tax+.001)
beer_ratio=1-pizza_ratio
tax=total_bill-pizza_pre_tax-beer_pre_tax

pizza_tax=pizza_ratio*tax
beer_tax=beer_ratio*tax

#Show the answer
fake_button=st.button("Add it Up!")
beer_per_person=round((beer_pre_tax+beer_tax)/(beer_num+.00001),2)
st.write(round(beer_per_person,2),"Beer Portion per person")


st.header("Final Numbers With Tax")
#st.divider()

pizza_per_person=round((pizza_pre_tax+pizza_tax)/(pizza_num+.00001),2)
st.write(pizza_per_person,"Per Person for people having just pizza")

pizza_and_beer_per_person=round(pizza_per_person+beer_per_person,2)
st.write(pizza_and_beer_per_person,"Per Person for people having Pizza and Beer")


st.subheader("Validate the numbers")
total_validation=round(pizza_per_person*pizza_num+beer_per_person*beer_num,2)
st.write("Pizza Ratio")
st.write(round(pizza_ratio,2))
st.write("Total of per portion X People")
st.write(round(total_validation,2))



st.write("Written by Ward Greunke")
