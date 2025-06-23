
import streamlit as st
import datetime

# Simulated memory
if "grocery_list" not in st.session_state:
    st.session_state.grocery_list = []
if "chores" not in st.session_state:
    st.session_state.chores = []

st.title("🏡 Household AI Assistant")

# Tabs for different functions
tab1, tab2, tab3 = st.tabs(["🛒 Grocery List", "🧹 Chore Reminders", "🍽️ Meal Ideas"])

with tab1:
    st.header("Grocery List")
    new_item = st.text_input("Add an item:")
    if st.button("Add to list") and new_item:
        st.session_state.grocery_list.append(new_item)
        st.success(f"Added '{new_item}' to grocery list!")

    if st.session_state.grocery_list:
        st.subheader("Your Grocery List:")
        for item in st.session_state.grocery_list:
            st.markdown(f"- {item}")

with tab2:
    st.header("Chore Reminders")
    chore = st.text_input("Add a new chore:")
    date = st.date_input("When?")
    if st.button("Add reminder") and chore:
        st.session_state.chores.append((chore, date))
        st.success(f"Reminder set for '{chore}' on {date}")

    if st.session_state.chores:
        st.subheader("Upcoming Chores:")
        for c, d in sorted(st.session_state.chores, key=lambda x: x[1]):
            st.markdown(f"✅ **{c}** on {d.strftime('%A, %b %d')}")

with tab3:
    st.header("Meal Ideas")
    ingredients = st.text_input("What's in your fridge?")
    if st.button("Suggest Meal") and ingredients:
        # Simulated suggestion
        st.info(f"With '{ingredients}', you could make: stir-fry, a wrap, or a salad!")
