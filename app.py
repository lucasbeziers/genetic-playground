import streamlit as st
from src.utils import GenesType, FitnessName
from src.population import Population

st.title('Genetic algorithm playground :dna:')

st.write('This page allows you to better understand genetic algorithm.')

st.header('Parameters')
col1, col2 = st.columns(2)
col1.subheader('Population :earth_africa:')
with col1:
    population_size = st.number_input('Population size', value=10, min_value=1, max_value=10000, step=1)
    mutation_rate = st.slider('Mutation rate', value=0.1, min_value=0., max_value=1., step=0.01)
    max_generations = st.number_input('Max nb of generations', value=1000, min_value=1, max_value=1000, step=10)
    fitness_name_values = {e.value: e for e in FitnessName}
    fitness_name_selected = st.selectbox('Fitness function', [e.value for e in FitnessName])
    fitness_name = fitness_name_values[fitness_name_selected]

col2.subheader('Individual :standing_person:')
with col2:
    genes_length = st.number_input('Genome size', value=10, min_value=1, max_value=999999, step=1)
    genes_max_value = st.number_input('Max value for each gene', value=10, min_value=1, max_value=999999, step=1)
    genes_type_values = {e.value: e for e in GenesType}
    genes_type_selected = st.selectbox('Genome type', [GenesType.INTEGER.value])
    genes_type = genes_type_values[genes_type_selected]
    

st.header('Simulation')
if st.button('Start'):
    with st.spinner('Wait the execution...'):
        population = Population(population_size=population_size,
                                mutation_rate=mutation_rate,
                                genes_length=genes_length,
                                max_generations=max_generations,
                                genes_type=genes_type,
                                genes_max_value=genes_max_value,
                                fitness_name=fitness_name)
        succes, last_generation, best_individual = population.evolve()
    not_word = "" if succes else "not"
    if succes:
        st.success("Optimal solution has been found! :partying_face:")
    else:
        st.error("Optimal solution was not found :smiling_face_with_tear:")
    st.write(f"Algorithm ran for {last_generation} generations")
    st.write(f"Best individual is {best_individual.genes} with a fitness score of {best_individual.fitness_score}")