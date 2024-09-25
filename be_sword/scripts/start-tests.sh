#!/usr/bin/env bash
set -e

COVER_PROJECT_PATH=.
TESTS_PROJECT_PATH=tests
REPORTS_FOLDER_PATH=tests-reports

PYTHONPATH=. pytest $TESTS_PROJECT_PATH -n auto -vv --doctest-modules \
  --cov=$COVER_PROJECT_PATH \
  --junitxml=$REPORTS_FOLDER_PATH/junit.xml \
  --cov-report=xml:$REPORTS_FOLDER_PATH/coverage.xml \
  --cov-report=html:$REPORTS_FOLDER_PATH/html \
  --cov-report=term
