from fastapi import FastAPI
from langcorn import create_service


app: FastAPI = create_service("llm_chain_file:chain_var")
