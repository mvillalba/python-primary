import primary


def test_version():
    """Tests package declares version correctly"""
    assert len(primary.__version__.split('.')) in [3, 4], "Version should follow SEMVER."
