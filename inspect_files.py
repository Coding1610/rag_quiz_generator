import faiss
import pickle
import os

def inspect_faiss_file(file_path):
    """Read and display FAISS file content"""
    print("INSPECTING FAISS FILE:")
    print("=" * 50)
    
    # Load the index
    index = faiss.read_index(file_path)
    
    # Basic info
    print(f"Total vectors: {index.ntotal}")
    print(f"Dimensions: {index.d}")
    print(f"Index type: {type(index).__name__}")
    
    # Show first few vectors
    print(f"\n First 3 vectors (showing first 5 dimensions each):")
    for i in range(min(3, index.ntotal)):
        vector = index.reconstruct(i)
        print(f"Vector {i}: {vector[:5]}...")  # First 5 dimensions
    
    return index

def inspect_pkl_file(file_path):
    """Read and display PKL file content"""
    print("\n INSPECTING PKL FILE:")
    print("=" * 50)
    
    with open(file_path, 'rb') as f:
        chunks = pickle.load(f)
    
    print(f"Total chunks: {len(chunks)}")
    
    # Show first few chunks
    print(f"\n First 3 chunks:")
    for i, chunk in enumerate(chunks[:3]):
        print(f"\n--- Chunk {i+1} ---")
        print(chunk[:200] + "..." if len(chunk) > 200 else chunk)
    
    return chunks

def inspect_storage():
    """Inspect all files in storage directory"""
    storage_dir = "faiss_storage"
    
    if not os.path.exists(storage_dir):
        print("Storage directory not found!")
        return
    
    files = os.listdir(storage_dir)
    faiss_files = [f for f in files if f.endswith('.faiss')]
    
    for faiss_file in faiss_files:
        pdf_hash = faiss_file.replace('.faiss', '')
        faiss_path = os.path.join(storage_dir, faiss_file)
        pkl_path = os.path.join(storage_dir, f"{pdf_hash}_chunks.pkl")
        
        print(f"\n ANALYZING: {pdf_hash[:16]}...")
        print("=" * 60)
        
        # Inspect both files
        if os.path.exists(faiss_path):
            inspect_faiss_file(faiss_path)
        
        if os.path.exists(pkl_path):
            inspect_pkl_file(pkl_path)

# Run the inspection
if __name__ == "__main__":
    inspect_storage()