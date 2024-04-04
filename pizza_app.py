#This app helps fleet 18 split the pizza and beer bill after sailing on a Tuesday night at Foster City

#Everyone eats pizza but only some people drink beer.  Find the portion of the bill attributed to each per person and then add each persons total.
#Assume tax is applied to both pizza and beer.

#inputs- number of people, total bill, pizza bill, beer bill.

import streamlit as st

total_bill=st.number_input('What is the total bill - Pizza + Beer.  Include tax.')
pizza_pre_tax=st.number_input('What was the amount of the pizza wihout tax?')
pizza_num=st.number_input('How many people ate pizza?')

st.write("Beer Portion")
beer_pre_tax=st.number_input('What was the amount of the beer?')
beer_num=st.number_input('How many people drank beer?')

#Do the math
pizza_ratio=(pizza_pre_tax+beer_pre_tax)/pizza_pre_tax
st.write(pizza_ratio)
beer_ratio=1-pizza_ratio
tax=total_bill-pizza_pre_tax-beer_pre_tax

pizza_tax=pizza_ratio*tax
beer_tax=beer_ratio*tax

beer_per_person=(beer_pre_tax+beer_tax)/beer_num
st.write(beer_per_person,"Beer Portion per person")


pizza_per_person=(pizza_pre_tax+pizza_tax)/pizza_num
st.write(pizza_per_person,"Pizza Portion per person")
st.write(pizza_per_person+beer_per_person,"Total for people having Pizza and Beer")

st.write("Validating the numbers")
total_validation=pizza_per_person*pizza_num+beer_per_person*beer_num
st.write(total_validation)




