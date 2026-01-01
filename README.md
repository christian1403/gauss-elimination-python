# Gaussian Elimination Solver

Program Python untuk menyelesaikan sistem persamaan linear menggunakan metode eliminasi Gauss dengan forward elimination (triangularisasi) dan back substitution.

## Deskripsi

Script ini mengimplementasikan algoritma eliminasi Gauss lengkap dengan:
- Input sistem persamaan linear dari user
- Pembentukan matrix augmented
- Forward elimination dengan partial pivoting
- Back substitution untuk mendapatkan solusi
- Tampilan step-by-step proses eliminasi

## Cara Penggunaan

```bash
python3 gaussian_elimination.py
```

### Format Input

Untuk sistem persamaan:
```
2x + 3y = 7
4x - y = 1
```

Input:
- Jumlah variabel: `2`
- Persamaan 1: `2 3 7`
- Persamaan 2: `4 -1 1`

### Contoh Output

```
=== SOLUSI SISTEM PERSAMAAN ===
x1 = 1.000000
x2 = 1.666667
```

## Struktur File

- `gaussian_elimination.py` - Script utama
- `gaussian_elimination_pseudocode.txt` - Pseudocode algoritma

## Requirements

- Python 3.x
- NumPy

```bash
pip install numpy
```

## Author

**Christian Chandra** - NPM: 06.2024.1.07763  
Tugas Komputasi Numerik - Eliminasi Gauss