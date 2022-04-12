import streamlit as st


st.title('Day 11 st.multiselect()')
st.write('#30DaysOfStreamlit')


st.header('Interests and learning styles')

# st.multiselect membutuhkan setidaknya 2 argument wajib yang berisi statment atau pertanyaan untuk pemilihan jawabannya dan argument kedua berisi option atau pilihan yang harus di pilih. Ketika menambahkan 3 argument maka argument terakhir berisi default option. Yang perlu di ingat bahwa default value harus berisi value dari argument kedua
option1 = st.multiselect('What is your favorite learning topic?', ['Machine Learning', 'Front End', 'Back End', 'Android', 'IOS Dev', 'Deep Learning', 'Cloud Computing'], ['Machine Learning', 'Deep Learning'])

option2 = st.multiselect('Which learning resource do you prefer?', ['Youtube', 'Free Code Camp', 'E-Book', 'Article', 'Bootcamp', 'Online Course'], ['E-Book'])

option3 = st.multiselect('When do you typically study?', ['Morning', 'Afternoon', 'Night'], ['Night'])

option1 = ' and '.join(option1)
option2 = ', '.join(option2)
option3 = ' '.join(option3)

data = f'You have an interest in **{option1}** with several learning resources that you use, including: **{option2}** and you like to study at **{option3}**.'
st.write(data)