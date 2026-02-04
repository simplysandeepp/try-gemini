import os
from dotenv import load_dotenv
import google.generativeai as genai
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings

# --- CONFIGURATION ---
# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set. Please set it in your .env file.")
genai.configure(api_key=GOOGLE_API_KEY)

class GeminiEmbeddingFunction(EmbeddingFunction):
    """
    Custom embedding function for ChromaDB using Gemini's embedding model.
    """
    def __call__(self, input: Documents) -> Embeddings:
        model = "models/text-embedding-004"
        title = "OS RAG Query"
        return [
            genai.embed_content(model=model,
                                content=text,
                                task_type="retrieval_document",
                                title=title)['embedding']
            for text in input
        ]

class OSBot:
    def __init__(self):
        # 1. Initialize Vector Database (ChromaDB)
        self.chroma_client = chromadb.Client()
        # Using a new collection name for OS facts
        self.collection = self.chroma_client.create_collection(
            name="os_concepts",
            embedding_function=GeminiEmbeddingFunction()
        )
        
        # 2. Initialize Gemini Model
        self.model = genai.GenerativeModel('gemini-3-flash-preview')
        
        # 3. Load Knowledge Base
        self.load_knowledge_base()

    def load_knowledge_base(self):
        print("Loading Operating System Knowledge Base...")
        documents = [
            "An Operating System (OS) is system software that manages computer hardware, software resources, and provides common services for computer programs.",
            "A Process is a program in execution, whereas a Thread is a lightweight process and the smallest unit of CPU execution within a process.",
            "Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.",
            "The four necessary conditions for Deadlock are: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait.",
            "Paging is a memory management scheme that eliminates the need for contiguous allocation of physical memory by dividing memory into fixed-size pages.",
            "Virtual Memory is a memory management capability of an OS that uses hardware and software to allow a computer to compensate for physical memory shortages by temporarily transferring data from RAM to disk storage.",
            "CPU Scheduling algorithms decide which process runs next. Common algorithms include First-Come, First-Served (FCFS), Round Robin (RR), and Shortest Job Next (SJN).",
            "A Kernel is the core component of an operating system, with complete control over everything in the system. It connects the application software to the hardware of a computer."
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
        You are an expert Professor specializing in Operating Systems. 
        Use the following technical context to answer the student's question accurately and concisely.
        If the answer is not in the context, use your general knowledge but mention that the specific context didn't contain the answer.

        Context:
        {context_text}

        Student Question: {user_query}
        """

        # Step 3: Generate Answer
        response = self.model.generate_content(prompt)
        return response.text

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    if GOOGLE_API_KEY == "YOUR_GEMINI_API_KEY":
        print("Error: Please set your GOOGLE_API_KEY in the code.")
    else:
        bot = OSBot()
        print("--- Operating System Expert Bot (Type 'quit' to exit) ---")
        
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ['quit', 'exit']:
                break
            
            try:
                answer = bot.chat(user_input)
                print(f"Bot: {answer}")
            except Exception as e:
                print(f"An error occurred: {e}")
