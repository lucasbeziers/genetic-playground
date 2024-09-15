import streamlit as st
from src.utils import GenesType, FitnessName

st.title('Genetic algorithm visualization :dna:')

st.write('This page allows you to better understand genetic algorithm.')

st.header('Parameters')
col1, col2 = st.columns(2)
col1.subheader('Population :earth_africa:')
with col1:
    population_size = st.number_input('Population size', value=10, min_value=1, max_value=999999, step=1)
    mutation_rate = st.slider('Mutation rate', value=0.1, min_value=0., max_value=1., step=0.01)
    max_generations = st.number_input('Max nb of generations', value=1000, min_value=1, max_value=10000000, step=100)
    fitness_name = st.selectbox('Fitness function', [e.value for e in FitnessName])

col2.subheader('Individual :standing_person:')
with col2:
    genes_length = st.number_input('Genome size', value=10, min_value=1, max_value=999999, step=1)
    genes_type = st.selectbox('Genome type', [e.value for e in GenesType])
    genes_max_value = st.number_input('Max value for each gene', value=10, min_value=1, max_value=999999, step=1)

st.header('Simulation')
if st.button('Start'):
    pass