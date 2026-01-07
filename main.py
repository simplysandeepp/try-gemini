import os
import google.generativeai as genai
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings

# --- CONFIGURATION ---
# Replace with your actual API key or set it as an environment variable
GOOGLE_API_KEY = "AIzaSyASdkGdlPeiwJOCy40j-_8Iklbolp-70X4"
genai.configure(api_key=GOOGLE_API_KEY)

class GeminiEmbeddingFunction(EmbeddingFunction):
    """
    Custom embedding function for ChromaDB using Gemini's embedding model.
    """
    def __call__(self, input: Documents) -> Embeddings:
        model = "models/text-embedding-004"
        title = "WW2 RAG Query"
        return [
            genai.embed_content(model=model,
                                content=text,
                                task_type="retrieval_document",
                                title=title)['embedding']
            for text in input
        ]

class WW2Bot:
    def __init__(self):
        # 1. Initialize Vector Database (ChromaDB)
        self.chroma_client = chromadb.Client()
        self.collection = self.chroma_client.create_collection(
            name="ww2_facts",
            embedding_function=GeminiEmbeddingFunction()
        )
        
        # 2. Initialize Gemini Model
        self.model = genai.GenerativeModel('gemini-3-flash-preview')
        
        # 3. Load Knowledge Base (Simulated for this example)
        # In a real app, you would load these from PDFs or text files.
        self.load_knowledge_base()

    def load_knowledge_base(self):
        print("Loading WW2 Knowledge Base...")
        documents = [
            "World War II began on September 1, 1939, when Nazi Germany invaded Poland.",
            "The Battle of Stalingrad (1942-1943) was a major turning point on the Eastern Front, where the Soviets defeated the Germans.",
            "The D-Day landings occurred on June 6, 1944, on the beaches of Normandy, France. It was Operation Overlord.",
            "The atomic bombs were dropped on Hiroshima (August 6, 1945) and Nagasaki (August 9, 1945), leading to Japan's surrender.",
            "Winston Churchill was the Prime Minister of the UK, Franklin D. Roosevelt was the US President, and Joseph Stalin led the Soviet Union.",
            "The Enigma machine was used by Germans for encryption, but its code was cracked by Alan Turing and his team at Bletchley Park."
        ]
        ids = [str(i) for i in range(len(documents))]
        
        self.collection.add(
            documents=documents,
            ids=ids
        )
        print("Knowledge Base Ready!\n")

    def retrieve_context(self, query):
        """Finds the most relevant documents in the DB based on the query."""
        results = self.collection.query(
            query_texts=[query],
            n_results=2 # Return top 2 most relevant facts
        )
        return results['documents'][0]

    def chat(self, user_query):
        # Step 1: Retrieve relevant information (RAG)
        context_docs = self.retrieve_context(user_query)
        context_text = "\n".join(context_docs)

        # Step 2: Construct the prompt
        prompt = f"""
        You are an expert historian specializing in World War II. 
        Use the following historical context to answer the user's question accurately.
        If the answer is not in the context, use your general knowledge but mention that the specific context didn't contain the answer.

        Context:
        {context_text}

        User Question: {user_query}
        """

        # Step 3: Generate Answer
        response = self.model.generate_content(prompt)
        return response.text

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    if GOOGLE_API_KEY == "YOUR_GEMINI_API_KEY":
        print("Error: Please set your GOOGLE_API_KEY in the code.")
    else:
        bot = WW2Bot()
        print("--- WW2 Expert Bot (Type 'quit' to exit) ---")
        
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ['quit', 'exit']:
                break
            
            try:
                answer = bot.chat(user_input)
                print(f"Bot: {answer}")
            except Exception as e:
                print(f"An error occurred: {e}")