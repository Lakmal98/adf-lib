import json

from samples.generate_samples import generate_samples


def test_samples_generate_valid_adf_documents(tmp_path):
    generated_files = generate_samples(tmp_path)

    assert {sample_file.name for sample_file in generated_files} == {
        "basic.json",
        "rich.json",
        "table.json",
    }

    for sample_file in generated_files:
        document = json.loads(sample_file.read_text(encoding="utf-8"))
        assert document["version"] == 1
        assert document["type"] == "doc"
        assert document["content"]

    table_document = json.loads((tmp_path / "table.json").read_text(encoding="utf-8"))
    assert any(node["type"] == "table" for node in table_document["content"])