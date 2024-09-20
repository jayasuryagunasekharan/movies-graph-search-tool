import os
from dotenv import load_dotenv
import logging

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chains.graph_qa.cypher import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph

import streamlit as st
from neo4j import GraphDatabase

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# Try to get secrets from Streamlit, fall back to environment variables
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def main(query):
    logger.info(f"Attempting to connect to Neo4j at {NEO4J_URI}")
    logger.info(f"Using username: {NEO4J_USERNAME}")
    logger.info(f"Password length: {len(NEO4J_PASSWORD) if NEO4J_PASSWORD else 0}")

    try:
        graph = Neo4jGraph(
            url=NEO4J_URI,
            username=NEO4J_USERNAME,
            password=NEO4J_PASSWORD
        )
        logger.info("Successfully connected to Neo4j")
    except Exception as e:
        logger.error(f"Failed to connect to Neo4j: {str(e)}")
        return f"Error connecting to database: {str(e)}"

    try:
        schema = graph.schema
        logger.info(f"Graph schema: {schema}")
    except Exception as e:
        logger.error(f"Failed to retrieve schema: {str(e)}")
        return f"Error retrieving schema: {str(e)}"

    try:
        llm = ChatGoogleGenerativeAI(model="gemini-pro")
        chain = GraphCypherQAChain.from_llm(graph=graph, llm=llm, verbose=True)
        response = chain.invoke({"query": query})
        logger.info(f"Query response: {response}")
        return response['result']
    except Exception as e:
        logger.error(f"Error during query processing: {str(e)}")
        return f"Error processing query: {str(e)}"
