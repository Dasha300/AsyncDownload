import pytest
from show_files import print_files
from files import File, update_list_file_hashes, get_list_file_names
from random import randint
from main import main
from get_folders import download_folder, main_task, start_async


@pytest.fixture
def get_folder_name():
    return "./tmp/" + str(randint(0, 2))


@pytest.fixture
def get_file_names():
    return "./tmp/0/LICENSE"


@pytest.fixture
def get_file_name():
    return r"./tmp/0\LICENSE"


@pytest.fixture
def get_hashes():
    return "d3d24a1d385cf8ac3c07ff5df6068bc7f11517ea814c3d5feb919ec"


def test_print_files():
    print_files()


def test_main():
    main()


def test_get_list_file_names(get_folder_name):
    list_files = get_list_file_names(get_folder_name)
    for file in list_files:
        assert file.__class__ == File


def test_get_item_list_file_names(get_file_name):
    list_files = get_list_file_names("./tmp/0")
    assert list_files[0].name == get_file_name


def test_update_list_file_hashes():
    list_files = get_list_file_names("./tmp/0")
    update_list_file_hashes(list_files)
    for file in list_files:
        assert file.__class__ == File


def test_file_obj(get_file_names, get_hashes):
    file = File()
    assert file.name is None
    assert file.hash256 is None
    file.set_name(get_file_names)
    assert file.name == get_file_names
    file.set_hash256(get_hashes)
    assert file.hash256 == get_hashes


@pytest.mark.asyncio
async def test_download_folder_name():
    await download_folder(1)
    with pytest.raises(Exception):
        await download_folder(1)


@pytest.mark.asyncio
async def test_main_task():
    await main_task()


def test_start_async():
    start_async()
