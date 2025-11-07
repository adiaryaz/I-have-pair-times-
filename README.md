# I have pair times?

Sebuah program untuk membuat fungsi yang menentukan properti kelipatan dalam sebuah array (list) integer.

## 📝 Description

Program ini mengimplementasikan sebuah fungsi untuk mengecek apakah sebuah array integer memiliki properti tertentu. Program ini akan menentukan apakah **elemen terakhir** dari array tersebut merupakan **kelipatan dari hasil kali (product)** dari **dua elemen bersebelahan (adjacent)** yang ada di dalam array.

-----

## 🎯 Problem Statement

### Input:

  * Sebuah array (list) 1-dimensi berisi integer.

### Output:

  * Sebuah nilai boolean (`True` atau `False`).

### Rules:

1.  Program harus mendapatkan nilai elemen terakhir (`last_element`) dari array.
2.  Program harus mengiterasi (looping) melalui semua *pasangan elemen yang bersebelahan* (misalnya, `arr[i]` dan `arr[i+1]`).
3.  Untuk setiap pasangan, hitung **hasil kalinya** (misalnya, `product = arr[i] * arr[i+1]`).
4.  Periksa apakah `last_element` habis dibagi oleh `product` tersebut (`last_element % product == 0`).
5.  Jika kondisi ini terpenuhi *setidaknya satu kali* untuk pasangan mana pun, fungsi akan mengembalikan `True`.
6.  Jika, setelah memeriksa semua pasangan, tidak ada yang memenuhi kondisi, fungsi akan mengembalikan `False`.
7.  Asumsikan array memiliki setidaknya 3 elemen untuk memiliki pasangan dan elemen terakhir.

-----

## 💡 Examples

### Example 1 (Sample 1)

**Input:**

```
[3, 2, 4, 6, 8]
```

**Output:**

```
True
```

**Explanation:** Elemen terakhir adalah 8. Program memeriksa pasangan (2, 4). Hasil kalinya adalah `2 * 4 = 8`. Karena `8 % 8 == 0`, hasilnya `True`.

### Example 2 (Sample 2)

**Input:**

```
[3, 3, 8, 9, 6]
```

**Output:**

```
False
```

**Explanation:** Elemen terakhir adalah 6. Hasil kali pasangan yang ada adalah (9, 24, 72, 54). Angka 6 tidak habis dibagi oleh salah satu dari hasil kali tersebut.

### Example 3 (Sample 3)

**Input:**

```
[1, 1, 2, 3, 5, 6]
```

**Output:**

```
True
```

**Explanation:** Elemen terakhir adalah 6. Program memeriksa pasangan pertama (1, 1). Hasil kalinya adalah `1 * 1 = 1`. Karena `6 % 1 == 0`, hasilnya `True`.

### Example 4 (Sample 4)

**Input:**

```
[1, 2, 3, 4]
```

**Output:**

```
False
```

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/check-pair-multiple.git
    cd check-pair-multiple
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Masukkan array dalam format list (misalnya, `[3, 2, 4]`) saat diminta untuk melihat hasilnya.
