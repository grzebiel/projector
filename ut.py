#!/bin/python
import subprocess

def run(command):
    return subprocess.run(command, shell=True, capture_output="True")


def assert_usage_printeed(result):
    assert b"usage" in result.stdout


def assert_succes(result):
    assert result.returncode == 0


def assert_fail(result):
    assert result.returncode != 0


def test_fails_if_no_args():
    res = run("./prj")
    assert_fail(res)
    assert_usage_printeed(res)


def test_fails_with_unknown_command():
    res = run("./prj unknown_command")
    assert_fail(res)

def test_printing_help_does_not_fail():
    res = run("./prj help")
    assert_succes(res)
    assert_usage_printeed(res)

