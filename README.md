# Movie Graph Search Tool

This Streamlit app allows users to explore and query a movie database using natural language. It leverages a Neo4j graph database and the Gemini Pro language model to provide insightful answers about movie connections.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jayasuryagunasekharan/movies-graph-search-tool
   cd movie-graph-search-tool
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Setup

1. Create a `.env` file in the project root directory with the following content:
   ```bash
   GOOGLE_API_KEY=your_google_api_key
   NEO4J_URI=your_neo4j_uri
   NEO4J_USERNAME=your_neo4j_username
   NEO4J_PASSWORD=your_neo4j_password
   ```

2. Replace the placeholder values with your actual credentials:
   - `your_google_api_key`: Your Google API key for accessing the Gemini Pro model
   - `your_neo4j_uri`: The URI of your Neo4j database (e.g., `neo4j+s://xxxxxxxx.databases.neo4j.io`)
   - `your_neo4j_username`: Your Neo4j database username
   - `your_neo4j_password`: Your Neo4j database password

## Running the App Locally

To run the app locally, use the following command:

```
streamlit run app.py
```

The app should now be accessible at `http://localhost:8501`.

## Deployment to Streamlit Cloud

1. Create a GitHub repository and push your code to it.

2. Log in to [Streamlit Cloud](https://share.streamlit.io/).

3. Click on "New app" and select your GitHub repository.

4. In the app settings:
   - Set the Python file path to `app.py`
   - Add the following secrets under the "Secrets" section:
     ```bash
     GOOGLE_API_KEY = "your_google_api_key"
     NEO4J_URI = "your_neo4j_uri"
     NEO4J_USERNAME = "your_neo4j_username"
     NEO4J_PASSWORD = "your_neo4j_password"
     ```

5. Click "Deploy" to launch your app on Streamlit Cloud.

## Troubleshooting

- If you encounter connection issues with Neo4j, ensure that your database is running and accessible from your deployment environment.
- For Neo4j Aura users, make sure to whitelist the IP address of your Streamlit Cloud instance in the Neo4j Aura console.
- Check the Streamlit Cloud logs for any error messages or connection issues.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

#My Streamlit Deployment Link

https://movies-graph-search-tool-5pgyzv7ezyh2em53cjxspr.streamlit.app/
