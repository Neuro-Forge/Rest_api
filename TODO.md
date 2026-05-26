# TODO - Fix employe endpoints

- [x] Update `api/urls.py` to add `path('employe/', ...)` pointing to the existing DRF view (`class employe` in `api/views.py`).
- [x] Update `employe/urls.py` to include a route so `GET /employe/` returns the same data (added a forwarder view).
- [x] Run server and verify:
  - [x] `GET /api/employe/` returns 200 with JSON.
  - [x] `GET /employe/` returns the same JSON/200.


