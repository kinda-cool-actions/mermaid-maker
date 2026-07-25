def fake_file_creator(fs, files_lst):
    """
    helps create fake files in subdirectories for testing against globbing patterns
    """
    for file in files_lst:
        fs.create_file(file)
