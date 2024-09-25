import pytest

from be_sword.utils import strtobool


class TestStrToBool:
    @pytest.mark.parametrize(
        "val, expected",
        [
            ("y", True),
            ("yes", True),
            ("t", True),
            ("true", True),
            ("on", True),
            ("1", True),
            ("n", False),
            ("no", False),
            ("f", False),
            ("false", False),
            ("off", False),
            ("0", False),
        ],
    )
    def test_strtobool(self, val: str, expected: bool):
        assert strtobool(val) == expected

    def test_strtobool_error(self):
        with pytest.raises(ValueError):
            strtobool("invalid")
