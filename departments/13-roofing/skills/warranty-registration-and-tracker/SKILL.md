---
name: warranty-registration-and-tracker
description: Register manufacturer and system warranties on time, issue the workmanship certificate and keep an inspection and repair log that protects validity.
---
# Warranty Registration and Tracker

## When to use
At project completion, and whenever a warranty event occurs.

## Inputs
Completion certificate, installed product list and lot data, installer certification status, manufacturer program rules, photos, permit final.

## Steps
1. Identify the layers that apply: installer workmanship warranty (ours), manufacturer material warranty, extended or system warranty (requires certified installer and registration). Residential and commercial differ; commercial warranties may be no-dollar-limit, labor-and-material prorated or material-only.
2. Confirm the installer is certified for the tier sold. If not, the tier cannot be promised.
3. Register within the program window, commonly about 30 days (**VERIFY** the program). Put the due date in `../../templates/warranty-registration-record.md` and calendar it at {{REGISTRATION_ALERT_DAYS}} days before.
4. Issue the workmanship warranty certificate (`../../templates/workmanship-warranty-certificate.md`) after owner approval, describing term, coverage and exclusions: installation by others, storm damage, lack of maintenance, foot traffic, unapproved changes.
5. Store registration confirmations and the certificate with the project.
6. Log every inspection, service visit and repair to preserve validity; commercial roofs also follow the maintenance program (`../maintenance-program-builder/SKILL.md`).
7. Review the register monthly for expirations and unregistered jobs.

## Outputs
Registration record, certificate, warranty register, alerts.

## Gates
- Owner approves every certificate.
- Do not describe a manufacturer warranty as ours or vice versa.
- Do not promise coverage for events the form excludes. Use "undetermined until inspected".
- A missed registration window is escalated to the owner the same day.

Workflow: `../../workflows/10-warranty-and-service-call.md`.
