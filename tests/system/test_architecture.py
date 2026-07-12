import re
from pathlib import Path
import pytest

# Localización de la raíz del repositorio relativa a este archivo (tests/system/test_architecture.py)
REPO_ROOT = Path(__file__).resolve().parents[2]


def test_root_structure():
    """Valida la estructura de directorios Blueprint v8.1.5."""
    required_dirs = [
        "config",
        "data",
        "docs/vaults",
        "docs/management",
        "docs/readings",
        "docs/syllabus",
        "docs/writing",
        "reports",
        "scratch",
        "scripts",
        "src",
        "tests/system",
    ]

    for d in required_dirs:
        assert (REPO_ROOT / d).is_dir(), f"Directorio requerido ausente: {d}"


def test_zero_floating_doctrine():
    """Enfuerza la Doctrina Zero Floating en la raíz."""
    forbidden_ext = [".ipynb", ".csv", ".xlsx", ".pdf", ".do", ".dta"]
    forbidden_dirs = ["writing_legacy", "deliveries", "notebooks", "vaults_legacy"]

    for item in REPO_ROOT.iterdir():
        if item.is_file() and item.suffix in forbidden_ext:
            if item.name not in ["README.md", "main.py"]:
                pytest.fail(
                    f"Archivo flotante detectado en raíz: {item.name}. Muévelo a una bóveda."
                )

        if item.is_dir() and item.name in forbidden_dirs:
            pytest.fail(f"Carpeta legada/prohibida detectada en raíz: {item.name}.")


def test_governance_files():
    """Valida la presencia de archivos críticos de gobernanza."""
    required_files = ["AGENTS.md", "pyproject.toml"]
    for f in required_files:
        assert (REPO_ROOT / f).is_file(), f"Archivo de gobernanza requerido ausente: {f}"
