#!/bin/bash
uvicorn src.model_server:app --host 0.0.0.0 --port 5000
