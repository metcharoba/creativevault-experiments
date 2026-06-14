# screenshots/refs/  — GATE 2 artifact lives here

Put the **real screenshot of the chosen lead reference** here before any
decompose/observe/build work:

    lead_firstview.png        (required — GATE 2)
    lead_full.png             (optional)
    support_*.png             (optional)

Auto capture (default):

    python3 ../../tools/rfm_shot.py "<lead-url>" screenshots/refs/lead_firstview.png

If rfm_shot.py prints SUSPECT/FAIL (cookie wall / login / blocked / blank),
capture the page manually and save it here with the same name (manual fallback).

No verified file here = GATE 2 is closed = the build does not start.
