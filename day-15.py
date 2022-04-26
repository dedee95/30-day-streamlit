import streamlit as st

st.title('Day 15 st.latex()')
st.write('#30DaysOfStreamlit')


st.latex(r'''a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =\sum_{k=0}^{n-1} ar^k =a \left(\frac{1-r^{n}}{1-r}\right)''')
st.write('Derivative')
st.latex(r'''f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}''')
st.write('Continuity')
st.latex(r'''\lim_{x \to a^-} f(x) = f(a) = \lim_{x \to a^+} f(x)''')