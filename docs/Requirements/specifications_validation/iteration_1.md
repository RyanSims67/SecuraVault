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
| Create password entry | A new password entry can be added. | Passed |
| View password entries | Saved entries can be displayed. | Passed |
| Edit password entry | An existing entry can be changed. | Passed |
| Delete password entry | An existing entry can be removed. | Passed |
| Required field validation | Entries without a title or password are rejected. | Passed |

Iteration 1 was developed and tested on the [`feature/securavault-deploy`](https://github.com/RyanSims67/SecuraVault/tree/feature/securavault-deploy) branch.


## Screenshots

### Menu

![create](iteration1_screenshots/iteration1-menu.png?raw=true)


### Create Password entry

![create](iteration1_screenshots/iteration1-create-entry.png?raw=true)

### View Password entries

![view](iteration1_screenshots/iteration1-view-entry.png?raw=true)

### Edit password entry

![edit](iteration1_screenshots/iteration1-edit-entry.png?raw=true)

![edit](iteration1_screenshots/iteration1-edit-entry-new.png?raw=true)

### Delete password entry

![delete](iteration1_screenshots/iteration1-delete-entry.png?raw=true)

![delete](iteration1_screenshots/iteration1-delete-entry-new.png?raw=true)

### Required field validation

![invalid](iteration1_screenshots/iteration1-invalid-id.png?raw=true)

![invalid](iteration1_screenshots/iteration1-validation-error-option.png?raw=true)

![invalid](iteration1_screenshots/iteration1-validation-error.png?raw=true)

