import streamlit as st
st.set_page_config(layout='wide')

st.title('🗓️ Day 22 st.form()')
st.write('#30DaysOfStreamlit')
col1, col2 = st.columns([2,1])
with col1:
    st.subheader('Coffee machine')
    with st.form('my_form'):
        st.write('**Order your coffee**')
        # Input widgets
        coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
        coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
        brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
        serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
        milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
        owncup_val = st.checkbox('Bring own cup')
        # Every form must have a submit button
        submitted = st.form_submit_button('Submit')
with col2:
    if submitted:
        st.markdown(f'''
            ### ☕ Your order list:
            - Coffee bean: `{coffee_bean_val}`
            - Coffee roast: `{coffee_roast_val}`
            - Brewing: `{brewing_val}`
            - Serving type: `{serving_type_val}`
            - Milk: `{milk_val}`
            - Bring own cup: `{owncup_val}`
            ''')
    else:
        st.write('☝️ Place your order!')