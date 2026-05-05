from pathlib import Path
from app.config import EMBEDDING_MODEL_NAME

STORAGE_DIR = Path("data/storage")


def get_embed_model():
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding

    return HuggingFaceEmbedding(
        model_name=EMBEDDING_MODEL_NAME
    )


def load_existing_index():
    from llama_index.core import StorageContext, load_index_from_storage

    if not STORAGE_DIR.exists():
        return None

    required_files = [
        STORAGE_DIR / "docstore.json",
        STORAGE_DIR / "index_store.json",
    ]

    has_required_files = all(path.exists() for path in required_files)
    has_vector_store = any(
        path.name.endswith("vector_store.json")
        for path in STORAGE_DIR.glob("*.json")
    )

    if not has_required_files or not has_vector_store:
        return None

    storage_context = StorageContext.from_defaults(
        persist_dir=str(STORAGE_DIR)
    )

    return load_index_from_storage(
        storage_context,
        embed_model=get_embed_model(),
    )


def add_text_to_index(text: str, source_name: str):
    from llama_index.core import Document, VectorStoreIndex
    from llama_index.core.node_parser import SentenceSplitter

    STORAGE_DIR.mkdir(parents=True, exist_ok=True)

    document = Document(text=text, metadata={"source": source_name})

    splitter = SentenceSplitter(chunk_size=512, chunk_overlap=50)
    nodes = splitter.get_nodes_from_documents([document])

    index = load_existing_index()

    if index is None:
        index = VectorStoreIndex(nodes, embed_model=get_embed_model())
    else:
        for node in nodes:
            index.insert_nodes([node])

    index.storage_context.persist(persist_dir=str(STORAGE_DIR))

    return index