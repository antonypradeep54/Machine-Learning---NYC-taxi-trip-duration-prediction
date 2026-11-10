# Target Customer Segment & Needs Analysis

**Project:** NYC Taxi Trip Duration Prediction  
**Portfolio initiative:** AI Product Management – Career Transition (AI-PM-CT)  
**Status:** Approved concept; customer assumptions not yet research-validated  
**Date:** 2026-11-08

## Target customer segment

**NYC Urban Commuters — Taxi & Ride-Hailing Users**

New York City residents and regular travelers who use taxis or ride-hailing for work, study, meetings, flights, and personal commitments.

- **Location:** New York City
- **Example profiles:** Working professionals, students, business travelers, and residents
- **Behavioral hypothesis:** Some users regularly plan trips in advance and value a travel-time estimate for a specific route and departure time
- **Scope:** This is a *customer segment*, not an individual fictional persona; no demographic proportions or usage-frequency statistics are claimed

## Goals

1. Obtain a useful trip-duration estimate before booking a taxi or ride-hailing trip.
2. Plan schedules and arrive on time for meetings, flights, events, and other commitments.
3. Make informed travel decisions when journey duration may vary by route, day, and time.

## Hypothesized pain points

1. Uncertainty about travel duration because of time-of-day patterns and variable traffic.
2. Difficulty planning departure times for future commitments.
3. Consequences of arriving late to important activities.

These are **hypotheses to validate**, not findings from interviews. This project does **not** claim that existing map products are generally inaccurate or inferior.

## Customer needs

- A simple, quick, accessible web interface.
- Pickup and drop-off location selection.
- A selected travel date and time.
- A clearly labeled estimated trip duration, with limitations communicated.
- Sufficient confidence in estimates to support planning; accuracy and usefulness must be evaluated with users.

## Problem statement

> NYC taxi and ride-hailing users who plan trips around time-sensitive commitments need an accessible way to estimate journey duration for a selected route, date, and time so they can make better departure and scheduling decisions.

## Proposed value proposition

A simple ML-powered web application that uses pickup location, destination, date, and time to estimate NYC taxi trip duration from historical patterns, helping users plan journeys. The proposition is **unvalidated** until user research and product testing are completed.

## Proposed MVP journey

1. Enter pickup location.
2. Enter destination.
3. Select planned pickup date and time.
4. Request an estimated trip duration.
5. View the estimate and an appropriate limitations note.

## Technical feasibility and boundaries

The current Random Forest notebook uses **passenger count, pickup hour, pickup day of week, and Haversine straight-line pickup-to-drop-off distance**. A website accepting only four user inputs (from, to, date, time) therefore needs:

- Geocoding to obtain pickup and destination coordinates.
- Haversine distance calculated consistently with the trained feature pipeline (not substituted road-network distance without retraining/testing).
- Time feature derivation using the intended NYC timezone.
- An explicit, validated policy for the required **passenger_count** feature (e.g., a user field or tested default).
- Saved model and preprocessing artifacts, with consistent versions.
- Clear disclosures that predictions are historical estimates, **not live traffic forecasts or guaranteed arrival times**.

The repository's reported validation MAE and RMSLE are not production performance guarantees.

## Validation plan

- Interview or survey representative NYC taxi/ride-hailing users to confirm actual planning problems.
- Compare user needs with existing route-planning alternatives.
- Test a clickable prototype for usability and usefulness.
- Evaluate model error by time of day, trip distance, and other relevant slices before public accuracy claims.
- Determine whether an estimate, range, or uncertainty message best supports user decisions.

## Portfolio progression

1. **Completed:** Develop and publish the initial NYC taxi trip-duration regression project.
2. **Current:** Define target customer segment and hypothesized needs.
3. **Next:** Define the MVP, user stories, acceptance criteria, and success measures.
4. **Then:** Build and deploy a small application.
5. **Later:** Compare regression models and optimize for user-relevant performance.

## Visual asset

The approved LinkedIn infographic is titled **“Target Customer Segment & Needs Analysis — Meet the NYC Urban Commuters.”** Its source image should be added to this repository separately as `docs/assets/nyc-urban-commuters-segment.png`. This document intentionally does not claim the graphic has been uploaded.

---
*Product discovery artifact — hypothesis-based, not primary customer research.*
