import os    # import the os module for interacting with the operating system

from dotenv import load_dotenv    # import the load_dotenv function from the dotenv package 

load_dotenv()    # load environment variables from a .env file

from google import genai    # import the genai module from the google package

api_key = os.getenv("GEMINI_API_KEY")    # retrieve the GEMINI_API_KEY from environment variables

client = genai.Client(api_key=api_key)  # create a client instance for interacting with the GenAI API

response = client.models.generate_content(
    model="gemini-2.5-flash",    # specify the model to be used for content generation
    contents="""
                You are a placement mentor.

                Student Scores:

                Aptitude: 60
                Communication: 55
                Coding: 90

                Provide:
                1. Strengths
                2. Weaknesses
                3. 30-day improvement plan
             """
)

print(response.text)  # print the response from the GenAI API