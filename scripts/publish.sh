#!/usr/bin/env bash
rm -rf dist/*  # Clean old builds
uv build
uv publish --token $PYPI_TOKEN
