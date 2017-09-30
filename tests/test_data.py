import pytest
from asc import data


def test_file_to_list():
    file_list = data.Data()

    with pytest.raises(IOError):
        file_list.file_to_list('wrong')
