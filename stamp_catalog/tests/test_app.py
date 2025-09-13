import os
import json
import cv2
import numpy as np
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.app import app, load_log


def _create_image(path, color=(0, 0, 0)):
    img = np.zeros((20, 20, 3), dtype=np.uint8)
    img[:] = color
    cv2.imwrite(str(path), img)


@pytest.fixture
def client(tmp_path):
    upload_dir = tmp_path / "uploads"
    log_file = tmp_path / "log.json"
    os.makedirs(upload_dir, exist_ok=True)
    app.config["UPLOAD_FOLDER"] = str(upload_dir)
    app.config["LOG_FILE"] = str(log_file)
    with open(log_file, "w") as f:
        json.dump([], f)
    return app.test_client()


def test_upload_and_duplicate_detection(client, tmp_path):
    image_path = tmp_path / "stamp.jpg"
    _create_image(image_path, color=(10, 20, 30))

    with open(image_path, "rb") as img:
        data = {"file": (img, "stamp.jpg")}
        resp1 = client.post("/upload", data=data, content_type="multipart/form-data")
    assert resp1.status_code == 200

    with open(image_path, "rb") as img:
        data = {"file": (img, "stamp.jpg")}
        resp2 = client.post("/upload", data=data, content_type="multipart/form-data")
    assert resp2.status_code == 400
    assert resp2.get_json()["error"] == "Duplicate stamp detected"

    log = load_log()
    assert len(log) == 1
    assert "colors" in log[0]["features"]
    assert len(log[0]["features"]["colors"]) > 0
