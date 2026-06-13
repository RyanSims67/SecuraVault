[Back to DDD Doc](ddd.md)

# Core Domain Chart

## Diagram

![Core Domain Chart](diagram/core-domain-chart-diagram.jpg?raw=true)


## Classification

| Subdomain | Classification | Status | Explanation |
|---|---|---|---|
| Vault Management | Core | Current | This contains SecuraVault's central user value: creating, viewing, editing, deleting, and searching password entries. |
| Password Generation | Supporting | Current | It helps users create strong passwords and supports the vault, but it is not the central purpose of the application. |
| Encryption | Generic | Current | SecuraVault relies on standard cryptographic functionality rather than developing a unique encryption algorithm. It is placed near the Supporting boundary because its configuration and integration are important to the application. |
| Storage | Generic | Current | Saving and loading encrypted data is necessary but common technical functionality with little business differentiation. |
| Master Password / Authentication | Supporting | Future | This would control access to the vault and protect the application with a master password. It is important, but not the main differentiating feature of SecuraVault. |
| Password Strength Analysis | Supporting | Future | This would evaluate saved passwords and help users detect weak credentials. It supports security, but is not the central purpose of the application. |
| Backup and Export | Generic / Supporting | Future | This would allow users to back up or export vault data securely. It is useful, but not a unique differentiating capability. |
| Audit Log | Supporting | Future | This would record important actions such as entry updates, deletions, or authentication events. It supports traceability and security, but is not a core differentiator. |
| Notifications | Generic | Future | This would notify users about weak passwords, old passwords, or security reminders. It is helpful, but common supporting functionality. |

## Interpretation


The chart shows that Vault Management deserves most of the project's
domain-design attention because it combines relatively high complexity
with high business differentiation.

Encryption is critical for security, but it is not classified as Core because
SecuraVault should rely on established cryptographic libraries rather than
building unique encryption functionality from scratch. Password Generation
supports the core workflow, while Storage is common infrastructure functionality.

The chart also includes several future domains to show how SecuraVault could
grow beyond the current implementation. Master Password / Authentication,
Password Strength Analysis, Backup and Export, Audit Log, and Notifications
are included as future scope so that the DDD design reflects a larger product
vision without claiming that these features are already implemented.