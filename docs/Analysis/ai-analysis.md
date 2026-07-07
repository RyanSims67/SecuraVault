[Back to Main Doc](../../README.md)

# AI Analysis — SecuraVault AI

This document is Part B of the analysis task.

For this part, I analyse an AI start-up idea based on my SecuraVault project.

The idea is **SecuraVault AI**, an AI-assisted password manager that helps users understand password risks, unsafe habits and simple security improvements.

This is not part of my current implemented SecuraVault version. It is a possible future extension / start-up idea.

[Prompt used: “Help me structure an AI-specific start-up analysis for a password manager project without making unrealistic security claims.”]

---

## 1. AI Start-up Idea

Explain the idea shortly.

Example direction:

SecuraVault AI would be a password manager with an additional AI assistant. The AI would not know or reveal the real passwords. Instead, it would help users understand weak password habits, repeated password patterns, unsafe storage behaviour and basic security risks.

The goal is to make password security easier to understand for normal users.

---

## 2. Problem and Target Users

Classic analysis point.

Explain who has the problem.

Possible users:

* students
* small teams
* non-technical users
* people who reuse passwords
* people who do not understand security warnings

The problem is not only storing passwords. The bigger problem is that users often do not understand why their habits are risky.

---

## 3. Scope and Boundaries

Explain what SecuraVault AI should and should not do.

In scope:

* explain password strength in simple language
* warn about password reuse
* give security suggestions
* explain risks without technical wording
* help users improve habits

Out of scope:

* automatic hacking protection
* guaranteed phishing detection
* reading private messages or emails
* storing passwords in an AI model
* replacing professional security tools

This is important because AI security claims should stay realistic.

---

## 4. AI Role in This Analysis

This section connects directly to the AI-analysis slides.

AI has two roles here.

First, AI is a tool for analysis. I used AI to help structure the analysis, compare risks and improve the wording.

Second, AI is the subject of analysis. SecuraVault AI would contain AI features, so the AI itself creates new requirements, risks and responsibilities.

[Prompt used: “Explain the difference between AI as a tool for analysis and AI as the subject of analysis for my SecuraVault AI idea.”]

---

## 5. Methodology / Tooling Layer

This section matches the slide about the methodological/tooling layer.

For the analysis, AI can help with:

* brainstorming possible users
* finding possible risks
* checking if the requirements are complete
* improving wording
* comparing the idea with similar tools
* creating first drafts of analysis points

However, I should still validate the output myself. AI can miss important security problems or suggest unrealistic features.

The most useful AI support for this analysis was structuring the AI-specific risks, because a normal password manager has different risks than a password manager with an AI assistant.

---

## 6. Stakeholder Layer

This section matches the stakeholder slide.

The stakeholders for SecuraVault AI would include:

* end users
* app developer
* possible data owner
* AI component provider
* security reviewer
* privacy reviewer
* future testers
* possible supervisors or regulators

Compared to the classic SecuraVault project, the AI version has more stakeholders because the AI feature creates extra responsibility.

For example, someone would need to decide what data the AI is allowed to use and who checks that the AI advice is safe.

---

## 7. Data Layer

This section matches the data layer slide.

SecuraVault AI would need careful data handling.

Possible data used by the AI:

* password strength score
* password length
* character variety
* reuse status
* user security settings
* anonymised risk patterns

The AI should not receive or store plain-text passwords.

A safer approach would be to analyse passwords locally and only pass non-sensitive indicators to the AI, such as “short password”, “reused password” or “missing special characters”.

Important data questions:

* What data is collected?
* Is the password itself ever sent to an AI model?
* Can the data be anonymised?
* How long is the data stored?
* Can the user delete the data?

[Prompt used: “Give me simple data-layer questions for an AI password manager assistant, focusing on privacy and password safety.”]

---

## 8. AI-Specific Requirements

This section matches the requirements layer slide.

Functional AI requirements:

* the system should explain why a password is weak
* the system should warn if a password pattern is reused
* the system should give simple improvement suggestions
* the system should explain security risks in beginner-friendly language
* the system should avoid showing the real password in AI explanations

Non-functional AI requirements:

* the AI advice should be understandable
* the AI output should be safe and not misleading
* the AI should not expose private password data
* the system should make clear that AI advice is only support
* the system should be testable
* the system should be reproducible where possible

This section is important because normal requirements are not enough when AI is part of the product.

---

## 9. Legal and Privacy Layer

This section matches the legal/regulatory slide.

The biggest legal and privacy concern is password data.

SecuraVault AI must avoid sending sensitive password data to an external model.

Important legal/privacy points:

* user consent
* data minimisation
* clear privacy policy
* no unnecessary personal data
* deletion option
* secure storage
* careful handling of logs

If the AI uses a cloud model, the privacy risk becomes higher. A local model or local rule-based analysis would be safer for this type of product.

---

## 10. Ethics and Trustworthy AI

This section matches the ethics and trustworthy AI slide.

The AI assistant should not make the user overtrust the system.

For example, it should not say:

```text
Your account is fully safe.
```

A better message would be:

```text
This password looks stronger than before, but no password manager can guarantee complete safety.
```

Trustworthy AI points:

* explain advice clearly
* avoid false confidence
* allow the user to ignore suggestions
* do not shame the user for weak passwords
* keep the user in control
* be transparent that the advice is AI-assisted

[Prompt used: “Help me identify ethics risks for an AI assistant inside a password manager.”]

---

## 11. Security Layer

This section matches the security slide.

Security is the most important layer for this project.

Main security risks:

* plain-text password exposure
* prompt injection
* AI hallucination
* unsafe advice
* sensitive data in logs
* overreliance on AI suggestions
* external API data leakage

Possible security controls:

* never send plain-text passwords to the AI
* keep password analysis local where possible
* remove sensitive data from logs
* add clear warning messages
* test AI outputs with unsafe examples
* separate password storage from AI explanation logic

The AI feature should improve understanding, not reduce security.

---

## 12. Quality Assurance Layer

This section matches the QA layer slide.

Testing SecuraVault AI would need more than normal software tests.

Classic tests:

* password saving works
* password loading works
* validation works
* encryption still works
* GUI or CLI still works

AI-specific tests:

* AI advice is not misleading
* AI does not reveal passwords
* AI does not suggest unsafe actions
* AI handles empty or strange input safely
* AI explanations are understandable
* repeated tests give reasonable results

A human reviewer should check the AI advice because security advice can be dangerous if it is wrong.

---

## 13. Process and Lifecycle Layer

This section matches the process/lifecycle slide.

The AI version should be developed in small steps.

Possible development steps:

```text
1. Build normal password manager features.
2. Add local password risk scoring.
3. Add simple explanation text without AI.
4. Add AI explanation as an optional feature.
5. Test privacy and security risks.
6. Add user warnings and consent.
7. Review AI output with test cases.
```

This process is safer than adding AI immediately.

It also keeps the project understandable because the normal password manager remains separate from the AI assistant.

---

## 14. Economic / Strategy Layer

This section matches the economic/strategy slide.

The AI feature could make SecuraVault more attractive because users often want simple explanations, not only technical password scores.

Possible value:

* easier for non-technical users
* better user education
* more helpful than a normal password strength bar
* possible start-up feature for students or small teams

Possible costs:

* AI API cost
* testing time
* privacy review
* security review
* maintenance of AI prompts or models

For a small start-up, a local or rule-based first version may be cheaper and safer than using a paid AI API from the beginning.

---

## 15. Conclusion

SecuraVault AI is a possible future extension of my SecuraVault project.

The idea is useful because it does not only store passwords. It helps users understand their security habits.

However, adding AI also adds new risks. The most important risks are privacy, security, hallucination and overtrust.

Because of that, the AI feature should be limited, transparent and carefully tested.

My conclusion is that SecuraVault AI could be a good start-up idea, but only if the AI assistant never receives plain-text passwords and only gives careful support instead of guaranteed security claims.