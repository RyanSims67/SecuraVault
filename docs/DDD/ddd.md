[Back to Main Doc](../../README.md)

# DDD

This document is to show the Domain-Driven Design to SecuraVault using Event Storming, Core Domain Chart, domain mapping, and Bounded Context Canvas.

## Project Context

SecuraVault is a basic password manager. The application allows users to create, view, edit, delete, search, and generate password entries. Passwords must be encrypted before storage.


## Requirements Used

| ID | Requirement |
|---|---|
| F1 | Users must be able to create password entries. |
| F2 | Users must be able to view saved password entries. |
| F3 | Users must be able to edit existing password entries. |
| F4 | Users must be able to delete password entries. |
| F5 | Users must be able to generate strong random passwords. |
| F6 | Users must be able to search password entries. |
| S1 | Passwords must be encrypted before they are stored. |
| Q1 | Developers must be able to easily change password generator settings. |
| Q2 | Developers must be able to modify encryption settings without changing vault logic. |
| Q3 | Developers must be able to run automated tests for the core password manager logic. |


## Deliverables

| Deliverable |
|---|
| [Event Storming](event-storming.md) |
| [Domains](domains.md) |
| [Core Domain Chart](core-domain-chart.md) |
| [Bounded Context Canvas](bounded-context-canvas.md) |