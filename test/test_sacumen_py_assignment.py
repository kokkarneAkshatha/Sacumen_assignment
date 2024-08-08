import pytest
import sacumen_py_assignment

@pytest.mark.parametrize("inp1 ,exp", [(".//file_input_dir//images//","push to s3")])
def test_images_dir(inp1, exp):
    assert sacumen_py_assignment.read_all_files(inp1) == exp

@pytest.mark.parametrize("inp1 ,exp", [(".//file_input_dir//documents//","push to google drive")])
def test_document_dir(inp1, exp):
    assert sacumen_py_assignment.read_all_files(inp1) == exp

@pytest.mark.parametrize("inp1 ,exp", [(".//file_input_dir//text//","Not categorized")])
def test_different_file(inp1, exp):
    assert sacumen_py_assignment.read_all_files(inp1) == exp



    