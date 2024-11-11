import streamlit as st
from src.utils import GenesType, FitnessName
from src.population import Population

# Title and Introduction
st.title('Genetic Algorithm Playground :dna:')

st.write(
    """
    Welcome to the Genetic Algorithm Playground! 🎉
    
    This interactive page allows you to explore and experiment with **genetic algorithms (GA)** — a powerful optimization 
    technique inspired by the process of natural selection. With this tool, you can tweak various parameters of the algorithm 
    and see how they influence the performance and results. Whether you're a beginner looking to understand the basics 
    or an enthusiast wanting to fine-tune parameters, this playground is designed for you!
    """
)

# Explanation Section
st.header('What is a Genetic Algorithm?')
st.write(
    """
    Genetic algorithms are optimization techniques that mimic the process of natural evolution. 
    They are used to find solutions to problems by evolving a population of potential solutions over time. 
    Here are the key steps involved in a genetic algorithm:
    
    1. **Initialization**: A population of individuals (solutions) is randomly generated.
    2. **Evaluation**: Each individual is evaluated using a fitness function to determine its quality.
    3. **Selection**: The best-performing individuals are selected to pass their genes to the next generation.
    4. **Crossover**: Selected individuals are paired to produce offspring, combining their genes.
    5. **Mutation**: Random changes are introduced to some genes to maintain diversity.
    6. **Iteration**: Steps 2-5 are repeated for a fixed number of generations or until an optimal solution is found.
    
    In this playground, you can adjust parameters like population size, mutation rate and fitness function, 
    to observe how they affect the algorithm's ability to find optimal solutions.
    """
)

# Parameter Configuration
st.header('Parameters')
st.write("Use the options below to configure your genetic algorithm experiment:")

col1, col2 = st.columns(2)

# Population Parameters
col1.subheader('Population :earth_africa:')
with col1:
    population_size = st.number_input(
        'Population Size',
        value=50,
        min_value=1,
        max_value=10000,
        step=1,
        help="Number of individuals in each generation. A larger population may increase accuracy but also computation time."
    )
    mutation_rate = st.slider(
        'Mutation Rate',
        value=0.1,
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        help="Probability of randomly mutating genes in an individual. Higher mutation rates introduce more diversity."
    )
    max_generations = st.number_input(
        'Max Generations',
        value=500,
        min_value=1,
        max_value=1000,
        step=10,
        help="Maximum number of generations the algorithm will run for. A higher value may lead to better solutions."
    )
    fitness_name_values = {e.value: e for e in FitnessName}
    fitness_name_selected = st.selectbox(
        'Fitness Function',
        [e.value for e in FitnessName],
        help="Choose how to evaluate the fitness of each individual."
    )
    fitness_name = fitness_name_values[fitness_name_selected]
    with st.expander("Click here to see details about fitness functions"):
        st.markdown(
            """
            **Select the fitness function to evaluate individuals**. Different functions measure success in different ways:
            
            - **Sum**: Fitness is the sum of all genes.
            - **Even**: Fitness is the count of even numbers in the genome.
            - **Alternate**: Fitness is the difference between the sum of even and odd index genes.
            """
        )


# Individual Parameters
col2.subheader('Individual :standing_person:')
with col2:
    genes_length = st.number_input(
        'Genome Size',
        value=6,
        min_value=1,
        max_value=100,
        step=1,
        help="Number of genes in each individual's genome. A larger genome may represent more complex solutions."
    )
    genes_max_value = st.number_input(
        'Max Value for Each Gene',
        value=10,
        min_value=1,
        max_value=999999,
        step=1,
        help="The upper bound for the values that genes can take. Adjust based on your problem requirements."
    )
    genes_type_values = {e.value: e for e in GenesType}
    genes_type_selected = st.selectbox(
        'Genome Type',
        [GenesType.INTEGER.value],
        help="Select the type of genes (e.g., integers, floats). This affects how solutions are represented."
    )
    genes_type = genes_type_values[genes_type_selected]

# Simulation Section
st.header('Run the Simulation')
if st.button('Start'):
    with st.spinner('Running the genetic algorithm... please wait.'):
        population = Population(
            population_size=population_size,
            mutation_rate=mutation_rate,
            genes_length=genes_length,
            max_generations=max_generations,
            genes_type=genes_type,
            genes_max_value=genes_max_value,
            fitness_name=fitness_name
        )
        succes, last_generation, best_individual = population.evolve()
        
    # Display results
    if succes:
        st.success("🎉 Optimal solution has been found!")
    else:
        st.error("😢 Optimal solution was not found within the given generations.")
    
    st.write(f"**Algorithm completed after {last_generation} generations**")
    st.write(f"**Best individual:** {best_individual.genes} with a fitness score of {best_individual.fitness_score}")
