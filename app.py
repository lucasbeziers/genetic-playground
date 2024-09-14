import streamlit as st

st.title('Genetic algorithm visualization :dna:')

st.write('This page allows you to better understand genetic algorithm.')

st.header('Parameters')
col1, col2 = st.columns(2)
col1.subheader('Population')
with col1:
    population_size = st.number_input('Population size', value=10, min_value=1)
    mutation_rate = st.slider('Mutation rate', value=0.1, min_value=0., max_value=1., step=0.01)
    max_generations = st.number_input('Max nb of generations', value=1000, min_value=1)

col2.subheader('Individual')
with col2:
    genome_size = st.text_input('Genome size', value=1)