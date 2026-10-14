$desktop = [Environment]::GetFolderPath("Desktop")
$folder = Join-Path $desktop "input_proof"

if (-not (Test-Path -LiteralPath $folder -PathType Container)) {
    Write-Error "Input proof folder not found: $folder"
    Read-Host "Press Enter to exit"
    exit 1
}

try {
    $fileInfo = Get-ChildItem -LiteralPath $folder -File -Filter "*.txt" -ErrorAction Stop |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1

    if ($null -eq $fileInfo) {
        throw "No .txt files found in: $folder"
    }

    $file = $fileInfo.FullName
    Write-Host "Checking newest file: $($fileInfo.Name)" -ForegroundColor Cyan

    $text = [IO.File]::ReadAllText($file)
    $text = $text.Replace("`r`n", "`n").Replace("`r", "`n")

    $marker = "--------------------------------------------------------------------`n"
    $i = $text.LastIndexOf($marker, [StringComparison]::Ordinal)

    if ($i -lt 0) {
        throw "Proof footer not found in $($fileInfo.Name)"
    }

    $payload = $text.Substring(0, $i)
    $sha = [Security.Cryptography.SHA256]::Create()

    try {
        $bytes = [Text.Encoding]::UTF8.GetBytes($payload)
        $hashBytes = $sha.ComputeHash($bytes)
        $actual = [BitConverter]::ToString($hashBytes).Replace("-", "").ToLowerInvariant()
    }
    finally {
        $sha.Dispose()
    }

    $expected = (Read-Host "Enter the expected SHA-256 hash").Trim()

    if ($expected -notmatch '^[a-fA-F0-9]{64}$') {
        Write-Host "INVALID: Enter exactly 64 hexadecimal characters." -ForegroundColor Yellow
    }
    elseif ($actual -eq $expected.ToLowerInvariant()) {
        Write-Host "CORRECT: SHA-256 matches." -ForegroundColor Green
    }
    else {
        Write-Host "INCORRECT: SHA-256 does not match." -ForegroundColor Red
    }
}
catch {
    Write-Host "ERROR: $($_.Exception.Message)" -ForegroundColor Red
}

Read-Host "Press Enter to exit"