# Testing Guide - White Box Testing

## 📚 Dokumentasi Tambahan

- **[Control Flow Graph (CFG)](docs/CFG.md)** - Panduan lengkap membuat CFG dari kode dengan contoh dan diagram Mermaid
- **[CFG Summary](docs/CFG-SUMMARY.md)** - Ringkasan CFG untuk semua fungsi di app.py

---

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Unit Tests

```bash
python -m pytest test/ -v
```

### 3. Run dengan Coverage Report

```bash
python -m pytest test/ --cov=app --cov-report=html -v
```

### 4. Run Mutation Testing

```bash
cosmic-ray init config.toml session.sqlite
cosmic-ray exec config.toml session.sqlite
cr-report session.sqlite
cr-rate session.sqlite
cr-html session.sqlite > mutation-report.html
```

---

## Unit Testing

### Jalankan semua test:

```bash
python -m pytest test/ -v
```

### Test spesifik class:

```bash
python -m pytest test/test_app.py::TestValidateNama -v
```

### Test spesifik function:

```bash
python -m pytest test/test_app.py::TestValidateNama::test_nama_kosong -v
```

---

## Coverage Report

### Coverage Report (Terminal):

```bash
python -m pytest test/ --cov=app --cov-report=term-missing -v
```

### Coverage Report (HTML):

```bash
python -m pytest test/ --cov=app --cov-report=html -v
```

Buka `htmlcov/index.html` di browser.

### Coverage Summary:

```bash
python -m coverage report
```

---

## Mutation Testing

### Step 1: Inisialisasi Session

```bash
cosmic-ray init config.toml session.sqlite
```

Perintah ini membuat database session yang berisi daftar mutasi yang akan ditest.

### Step 2: Jalankan Mutation Testing

```bash
cosmic-ray exec config.toml session.sqlite
```

### Step 3: Lihat Hasil

```bash
# Lihat report lengkap
cr-report session.sqlite

# Lihat mutation score
cr-rate session.sqlite

# Lihat hanya yang survived
cr-report --surviving-only session.sqlite
```

### Step 4: Generate HTML Report

```bash
cr-html session.sqlite > mutation-report.html
```

Buka `mutation-report.html` di browser.

---

## Interpretasi Hasil

### Coverage Report:

- **Hijau**: Code sudah ter-test
- **Merah**: Code belum ter-test
- **Target**: Minimal 80-90% coverage

### Mutation Testing:

- **Killed**: Test detect mutasi (bagus!)
- **Survived**: Test tidak detect mutasi (perlu tambah test)
- **Mutation Score**: % mutant yang killed (target: > 80%)

---

## Workflow Testing Lengkap

```bash
# 1. Unit test dengan coverage
python -m pytest test/ -v --cov=app --cov-report=html

# 2. Inisialisasi mutation testing
cosmic-ray init config.toml session.sqlite

# 3. Jalankan mutation testing
cosmic-ray exec config.toml session.sqlite

# 4. Lihat hasil mutation
cr-report session.sqlite
cr-rate session.sqlite

# 5. Generate mutation HTML (optional)
cr-html session.sqlite > mutation-report.html
```

---

## Struktur Report

Setelah menjalankan testing:

```
fintechgo-unit-testing/
├── app.py
├── test/
│   └── test_app.py
├── config.toml           # Cosmic Ray config
├── htmlcov/              # Coverage HTML report
│   └── index.html
├── mutation-report.html  # Mutation HTML report
└── session.sqlite        # Cosmic Ray session database
```

---

## Membersihkan Cache

```bash
# Hapus coverage cache
rm -rf .coverage htmlcov/

# Hapus mutation cache
rm -rf session.sqlite mutation-report.html

# Hapus semua cache
rm -rf .coverage htmlcov/ session.sqlite mutation-report.html __pycache__ .pytest_cache
```
