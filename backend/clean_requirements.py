def is_valid_package(line):
    return "==" in line and "@" not in line and not line.startswith("#") and not line.strip().startswith("file:")

with open("requirements.txt", "r") as infile:
    lines = infile.readlines()

cleaned = sorted([line.strip() for line in lines if is_valid_package(line)])

with open("requirements_clean.txt", "w") as outfile:
    for line in cleaned:
        outfile.write(line + "\n")

print(f"✅ Cleaned list saved to requirements_clean.txt with {len(cleaned)} packages.")
