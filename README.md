# FlyRank Week 1 — BE-01: First API Endpoint

A minimal FastAPI server with two JSON endpoints.

## Setup

pip install -r requirements.txt
uvicorn main:app --reload

## Endpoints

GET /       → Returns a hello message and status
GET /info   → Returns intern info and project details

## Test with curl

curl http://localhost:8000/
curl http://localhost:8000/info

## Test in browser

Visit http://localhost:8000/ and http://localhost:8000/info

Interactive docs available at http://localhost:8000/docs
