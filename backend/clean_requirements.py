import pkg_resources

def is_valid_package(line):
    return (
        "==" in line and
        "@" not in line and
        not line.strip().startswith("#") and
        not line.strip().startswith("file:")
    )

raw_file = "raw_requirements.txt"
clean_file = "backend/requirements.txt"

with open(raw_file) as f:
    lines = f.readlines()

installed = {pkg.key for pkg in pkg_resources.working_set}
clean = []

for line in lines:
    line = line.strip()
    if is_valid_package(line):
        pkg_name = line.split("==")[0].lower()
        if pkg_name in installed:
            clean.append(line)

with open(clean_file, "w") as f:
    f.write("\n".join(sorted(set(clean))))

print(f"✅ Cleaned list saved to {clean_file} with {len(clean)} packages.")

