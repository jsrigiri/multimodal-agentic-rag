import os


# =========================
# Environment flags
# =========================
USE_LLM_ROUTER = os.getenv("USE_LLM_ROUTER", "false").lower() == "true"
RENDER_LIGHTWEIGHT_MODE = os.getenv("RENDER_LIGHTWEIGHT_MODE", "false").lower() == "true"


# =========================
# Model Config
# =========================
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "llama3.2")
VISION_MODEL_NAME = os.getenv("VISION_MODEL_NAME", "llava")

EMBEDDING_MODEL_NAME = os.getenv(
    "EMBEDDING_MODEL_NAME",
    "sentence-transformers/all-MiniLM-L6-v2",
)


# =========================
# RAG / Retrieval Config
# =========================
TOP_K = int(os.getenv("TOP_K", "3"))
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "512"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))


# =========================
# Paths
# =========================
RAW_DATA_DIR = os.getenv("RAW_DATA_DIR", "data/raw")
STORAGE_DIR = os.getenv("STORAGE_DIR", "data/storage")


# =========================
# Monitoring
# =========================
ENABLE_METRICS = os.getenv("ENABLE_METRICS", "true").lower() == "true"