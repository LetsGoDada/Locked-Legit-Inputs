# LLI — Locked Legit Inputs; Input Proof

LLI is a Windows desktop application that combines an Input Proof recorder and a SHA-256 verification tool in one simple launcher.

## Features

- **Input Proof:** Records keyboard and mouse input during an active recording session and exports a proof report as a text file.
- **SHA-256 Checker:** Calculates and checks a SHA-256 hash to help verify whether proof content matches an expected hash.
- **Automatic saving:** Proof files are saved to a folder named `input_proof` on the user's Desktop.
- **Simple launcher:** Access both tools through the LLI home screen.
- **Portable distribution:** The packaged application is designed to run from a single `LLI.exe` file.

## Getting Started

1. Download `LLI.exe` from the repository's Releases section.
2. Run `LLI.exe` on Windows.
3. Select **Input Proof** or **SHA-256 Checker** from the home screen.
4. Find exported proof files in the `input_proof` folder on your Desktop.

## Verification Notes

SHA-256 can help detect changes when a file is compared against a trusted expected hash. It does not, by itself, establish who created a file or guarantee that the file has never been tampered with.

## Platform

- Windows
- Packaged as a standalone executable using PyInstaller

## Responsible Use

Use input recording only on your own device or with the permission of the people involved. Input recordings may contain sensitive information, so handle exported proof files carefully.

## License

Add your chosen license here before redistributing the project.
