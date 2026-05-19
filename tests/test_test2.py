


import os, pytest
from test2 import scan_files

def test_grouping_by_prefix(tmp_path):
    (tmp_path / "aamfile.txt").write_text("x" * 100)
    (tmp_path / "aamother.txt").write_text("x" * 50)
    (tmp_path / "zzzfile.txt").write_text("x" * 10)

    result = scan_files(tmp_path)
    assert 'aam' in result
    assert 'zzz' in result

def test_sorted_descending(tmp_path):
    (tmp_path / "abcbig.txt").write_text("x" * 200)
    (tmp_path / "abcsmall.txt").write_text("x" * 10)

    result = scan_files(tmp_path)
    sizes = [size for size, _ in result['abc']]
    assert sizes == sorted(sizes, reverse=True)

def test_recursive(tmp_path):
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    (subdir / "aamdeep.txt").write_text("hello")

    result = scan_files(tmp_path)
    assert any('aamdeep.txt' in name for _, name in result.get('aam', []))

def test_empty_dir(tmp_path):
    assert scan_files(tmp_path) == {}