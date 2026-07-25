from pathlib import Path

from ..src import mermaid_gen


def test_mermaid_gen(monkeypatch, flat_mmd_files):
    """
    test whether a run command is run for each input/output file,
    and test whether its run for each pair of input/output file
    """
    input_files = flat_mmd_files
    run_args = []
    monkeypatch.setattr(mermaid_gen, "run", lambda arg, check: run_args.append(arg))
    output_files = []
    for file in flat_mmd_files:
        output_files.append(Path(file).with_suffix(".pdf").as_posix())

    mermaid_gen.mermaid_gen(input_files, output_files, "boom")

    assert len(run_args) == len(input_files)
    for i in range(len(run_args)):
        assert "boom" in run_args[i]
        assert input_files[i] in run_args[i]
        assert output_files[i] in run_args[i]
