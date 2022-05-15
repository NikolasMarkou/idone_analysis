# ---------------------------------------------------------------------
# Deployment files only (models and utilities)
# ---------------------------------------------------------------------

import setuptools

# ---------------------------------------------------------------------

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    licence_text = f.read()

# ---------------------------------------------------------------------

setuptools.setup(
    name="idone_classifier",
    version="1.0.0",
    python_requires=">=3.6",
    description="",
    long_description=readme,
    author="Nikolas Markou",
    author_email="nikolas.markou@electiconsulting.com",
    license=licence_text,
    packages=setuptools.find_packages(
        exclude=[
            "tests",
            "images",
            "notebooks"
        ]),
    install_requires=[
        "numpy",
        "Keras",
        "pandas",
        "setuptools",
        "tensorflow>=2.6.2",
        "matplotlib>=3.3.4",
        "tensorflow-addons",
    ],
    url="https://github.com/NikolasMarkou/idone_analysis",
    include_package_data=True
)

# ---------------------------------------------------------------------
