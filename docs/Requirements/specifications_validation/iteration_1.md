[Back to Requirements Doc](requirements.md)

# Iteration 1

## Goal

The goal of Iteration 1 is to implement the basic password vault entry functionality for SecuraVault.

## Related Requirements

- F1 — Users must be able to create password entries.
- F2 — Users must be able to view saved password entries.
- F3 — Users must be able to edit existing password entries.
- F4 — Users must be able to delete password entries.

## Specifications

| Field | Required | Description |
|---|---|---|
| Title | Yes | Name of the saved service or account |
| Username | Yes | Username or email address for the account |
| Password | Yes | Password value for the account |
| URL | No | Website or service URL |
| Notes | No | Optional extra information |

The system should allow the user to create, view, edit, and delete password entries.

## Validation Plan

Iteration 1 is valid when basic operations work correctly.

| Validation Check | Expected Result | Status |
|---|---|---|
| Create password entry | A new password entry can be added. | Not tested yet |
| View password entries | Saved entries can be displayed. | Not tested yet |
| Edit password entry | An existing entry can be changed. | Not tested yet |
| Delete password entry | An existing entry can be removed. | Not tested yet |
| Required field validation | Entries without a title or password are rejected. | Not tested yet |
