# LLI — Locked Legit Inputs
### Legitimate Proof

LLI (Locked Legit Inputs) is a Windows desktop application that combines an input-proof recorder and a SHA-256 verification tool in one launcher. It is designed to help users document input sessions and check the integrity of exported proof files.

## Features

- **Input Proof Recorder** — Records keyboard and mouse input during an active recording session and exports a proof report as a text file.
- **SHA-256 Checker** — Checks whether proof content matches an expected SHA-256 hash.
- **Automatic Saving** — Saves exported proof files to an `input_proof` folder on the user's Desktop.
- **Unified Launcher** — Opens both tools from the LLI home screen.
- **Single-File Distribution** — The packaged application is designed to run from a single `LLI.exe` file.

## Getting Started

1. Open the **Releases** section of this GitHub repository.
2. Download `LLI.exe`.
3. Run `LLI.exe` on a compatible Windows computer.
4. Choose **Input Proof** or **SHA-256 Checker** from the home screen.
5. After exporting a proof, look for the `.txt` file in the `input_proof` folder on your Desktop.

> **Note:** The first launch may be delayed while Windows checks the executable. Only run software you trust.

## Input Proof

The Input Proof tool records keyboard and mouse input during an active recording session and exports the collected events to a text file.

Proof files are saved in:

`Desktop\input_proof`

These files may contain sensitive information. Review and protect them carefully before sharing them.

## SHA-256 Verification

The SHA-256 Checker calculates or checks a cryptographic hash of proof content against an expected value.

A matching SHA-256 hash can help establish that the checked content matches the content used to produce the expected hash. However, a hash alone does **not** prove who created the file, when it was created, or whether the expected hash is trustworthy.

For stronger verification, keep the expected hash in a separate, trusted location.

## Responsible Use and Permission

**LLI may only be used on devices you own or on devices whose owner has explicitly given you permission to use it.**

By using LLI, you agree to the following rules:

- Obtain permission before using LLI on another person's device.
- Only record keyboard or mouse input when you are authorized to do so.
- Never use LLI to secretly monitor another person or collect input without appropriate permission.
- Respect other people's privacy and applicable laws.
- Handle exported proof files responsibly and do not share sensitive information without authorization.

**Unauthorized use is not permitted.**

## Platform and Technology

- **Operating system:** Windows
- **Packaging:** PyInstaller
- **Application format:** `LLI.exe`

The executable is intended to bundle the application's components. Compatibility may depend on the Windows environment and system security settings.

## License and Redistribution

LLI is provided under a custom license with the following conditions:

- Use is limited to devices you own or devices whose owner has explicitly permitted your use.
- Recording must be authorized and must respect privacy.
- Redistribution, modification, or publication of modified versions requires prior written permission from the copyright holder, unless separately authorized.

All rights reserved unless otherwise stated by the copyright holder.

These terms describe the intended conditions of use; consult a qualified legal professional if a legally enforceable license is required.

## Disclaimer

LLI is provided **"as is"**, without warranties of any kind to the fullest extent permitted by applicable law.

The author is not responsible for misuse of the software or for decisions made solely on the basis of generated proof files or hash comparisons.

---

**LLI — Locked Legit Inputs: Legitimate Proof**

*Record responsibly. Verify carefully. Respect permission.*
