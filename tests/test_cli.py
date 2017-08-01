from click.testing import CliRunner
from asc import cli


def test_cmd_interface(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert not result.exception
