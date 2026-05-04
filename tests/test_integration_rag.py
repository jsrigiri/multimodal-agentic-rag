import shutil
from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_upload_index_and_ask_txt_document():
    storage_dir = Path("data/storage")
    raw_dir = Path("data/raw")

    shutil.rmtree(storage_dir, ignore_errors=True)
    storage_dir.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)

    test_content = (
        "Acme Insurance policy covers flood damage, fire damage, "
        "and theft claims for eligible customers."
    )

    response = client.post(
        "/upload",
        files={
            "file": (
                "test_policy.txt",
                test_content.encode("utf-8"),
                "text/plain",
            )
        },
    )

    assert response.status_code == 200
    assert response.json()["status"] == "uploaded_and_indexed"

    ask_response = client.post(
        "/ask",
        json={"question": "What does the Acme Insurance policy cover?"},
    )

    assert ask_response.status_code == 200

    result = ask_response.json()

    assert "answer" in result
    assert "sources" in result
    assert len(result["sources"]) > 0
    assert result["sources"][0]["source"] == "test_policy.txt"