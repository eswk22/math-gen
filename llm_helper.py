import os
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

# Set model configuration
model_name = "gemini-pro"  # Replace with actual model name or access method

# Initialize language model (adjust based on chosen model and library)
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Define function to generate math problem
def generate_math_problem(problem_type, difficulty_level, word_problem):
    word_str = "word" if word_problem == True else ""
    prompt = PromptTemplate.from_template(
    """You are like a math teacher who provide the list of math problems in a sheet, 
    Generate group of {problem_type} math {word_str} problems for kids at a {difficulty_level} level and show how to solve the problems at the end of the list."""
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain.invoke({"problem_type": problem_type, "word_str": word_str, "difficulty_level": difficulty_level})