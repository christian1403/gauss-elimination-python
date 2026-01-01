"""
Tugas Komputasi Numerik - Eliminasi Gauss
Nama: Christian Chandra
NPM: 06.2024.1.07763
Script Python untuk menghitung sistem persamaan linear menggunakan eliminasi Gauss
dengan forward elimination (triangularisasi) dan back substitution
"""

import numpy as np
from typing import List, Tuple, Optional

def print_matrix(matrix: np.ndarray, title: str = "Matrix") -> None:
    """cetak matrix"""
    print(f"\n{title}:")
    print("-" * (len(title) + 1))
    rows, cols = matrix.shape
    for i in range(rows):
        row_str = "["
        for j in range(cols):
            if j == cols - 1:  # Kolom terakhir (konstanta)
                row_str += f" | {matrix[i,j]:8.4f}"
            else:
                row_str += f" {matrix[i,j]:8.4f}"
        row_str += " ]"
        print(row_str)
    print()

def input_matrix() -> np.ndarray:
    """Input matrix augmented dari user input"""
    print("=== INPUT SISTEM PERSAMAAN LINEAR ===")
    print("Masukkan sistem persamaan dalam bentuk Ax = b")
    
    while True:
        try:
            n = int(input("Masukkan jumlah variabel/persamaan: "))
            if n <= 0:
                print("Jumlah variabel harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid!")
    
    print(f"\nMasukkan koefisien untuk {n} persamaan:")
    print("Format: a11 a12 ... a1n b1")
    print("Contoh untuk 2x + 3y = 5: 2 3 5")
    
    matrix = np.zeros((n, n + 1), dtype=float)
    
    for i in range(n):
        while True:
            try:
                print(f"Persamaan {i+1}: ", end="")
                coeffs = list(map(float, input().split()))
                if len(coeffs) != n + 1:
                    print(f"Masukkan {n + 1} angka (koefisien + konstanta)!")
                    continue
                matrix[i] = coeffs
                break
            except ValueError:
                print("Masukkan angka yang valid!")
    
    return matrix

def forward_elimination(matrix: np.ndarray) -> Tuple[np.ndarray, bool]:

    n = matrix.shape[0]
    augmented = matrix.copy()
    
    print("=== FORWARD ELIMINATION (TRIANGULARISASI) ===")
    print_matrix(augmented, "Matrix Augmented Awal")
    
    for i in range(n):
        # Mencari pivot (elemen terbesar di kolom i untuk stabilitas numerik)
        max_row = i
        for k in range(i + 1, n):
            if abs(augmented[k, i]) > abs(augmented[max_row, i]):
                max_row = k
        
        # Tukar baris jika diperlukan
        if max_row != i:
            augmented[[i, max_row]] = augmented[[max_row, i]]
            print(f"Menukar baris {i+1} dengan baris {max_row+1}")
            print_matrix(augmented, f"Setelah pertukaran baris")
        
        # Cek apakah pivot adalah nol
        if abs(augmented[i, i]) < 1e-10:
            print(f"Pivot pada baris {i+1} adalah nol atau sangat kecil!")
            print("Sistem mungkin tidak memiliki solusi unik.")
            return augmented, False
        
        # Eliminasi untuk baris di bawah pivot
        for j in range(i + 1, n):
            if abs(augmented[j, i]) > 1e-10:  # Hindari pembagian dengan nol
                factor = augmented[j, i] / augmented[i, i]
                print(f"Eliminasi baris {j+1}: P{j+1} = P{j+1} - ({factor:.4f}) × P{i+1}")
                
                for k in range(i, n + 1):
                    augmented[j, k] -= factor * augmented[i, k]
                
                print_matrix(augmented, f"Setelah eliminasi baris {j+1}")
    
    return augmented, True

def back_substitution(matrix: np.ndarray) -> Optional[np.ndarray]:

    n = matrix.shape[0]
    x = np.zeros(n)
    
    print("=== BACK SUBSTITUTION ===")
    
    # Mulai dari persamaan terakhir
    for i in range(n - 1, -1, -1):
        # Cek konsistensi
        if abs(matrix[i, i]) < 1e-10:
            if abs(matrix[i, n]) < 1e-10:
                print(f"Persamaan {i+1}: 0 = 0 (infinite solutions)")
                return None
            else:
                print(f"Persamaan {i+1}: 0 = {matrix[i, n]} (no solution)")
                return None
        
        # Hitung nilai x[i]
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += matrix[i, j] * x[j]
        
        x[i] = (matrix[i, n] - sum_ax) / matrix[i, i]
        
        # Tampilkan perhitungan
        if i == n - 1:
            print(f"x{i+1} = {matrix[i, n]:.4f} / {matrix[i, i]:.4f} = {x[i]:.4f}")
        else:
            print(f"x{i+1} = ({matrix[i, n]:.4f} - {sum_ax:.4f}) / {matrix[i, i]:.4f} = {x[i]:.4f}")
    
    return x

def main():
    """Fungsi utama program"""
    print("=" * 80)
    print("    PROGRAM ELIMINASI GAUSS, Christian Chandra - 06.2024.1.07763")
    print("=" * 80)
    
    # Input matrix dari user
    matrix = input_matrix()
    original_matrix = matrix.copy()
    
    # Forward elimination
    triangular_matrix, is_solvable = forward_elimination(matrix)
    
    if not is_solvable:
        print("Sistem tidak dapat diselesaikan dengan metode ini.")
        return
    
    print_matrix(triangular_matrix, "Matrix Upper Triangular")
    
    # Back substitution
    solution = back_substitution(triangular_matrix)
    
    if solution is None:
        print("Sistem tidak memiliki solusi unik.")
        return
    
    # Tampilkan solusi
    print("=== SOLUSI SISTEM PERSAMAAN ===")
    for i, val in enumerate(solution):
        print(f"x{i+1} = {val:.6f}")
    
    print("=" * 60)
    print("Program selesai!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh user.")
    except Exception as e:
        print(f"\nTerjadi error: {e}")