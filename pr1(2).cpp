#include <iostream>
#include <vector>
#include <unordered_set>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <windows.h> // Для SetConsoleCP и SetConsoleOutputCP

using namespace std;

// Сложность: O(n)
vector<int> generateRandomVector(int size) {
    vector<int> vec;
    for (int i = 0; i < size; ++i) {
        vec.push_back(rand() % 1000);
    }
    return vec;
}

// Объединение с удалением дубликатов через обычный цикл
// Сложность: O(n * m)
vector<int> mergeWithLoop(const vector<int>& a, const vector<int>& b) {
    vector<int> result = a;
    for (int valB : b) {
        bool found = false;
        for (int valR : result) {
            if (valR == valB) {
                found = true;
                break;
            }
        }
        if (!found) result.push_back(valB);
    }
    return result;
}

// Объединение с удалением дубликатов через unordered_set
// Сложность: O(n + m)
vector<int> mergeWithSet(const vector<int>& a, const vector<int>& b) {
    unordered_set<int> seen;
    vector<int> result;
    for (int val : a) {
        if (seen.insert(val).second) result.push_back(val);
    }
    for (int val : b) {
        if (seen.insert(val).second) result.push_back(val);
    }
    return result;
}

int main() {
    // Установка русской кодировки для Windows
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    srand(time(nullptr));

    int sizeA, sizeB;

    cout << "Введите размер первого массива: ";
    cin >> sizeA;
    cout << "Введите размер второго массива: ";
    cin >> sizeB;

    vector<int> a = generateRandomVector(sizeA);
    vector<int> b = generateRandomVector(sizeB);

    auto start1 = chrono::high_resolution_clock::now();
    vector<int> mergedLoop = mergeWithLoop(a, b);
    auto end1 = chrono::high_resolution_clock::now();
    chrono::duration<double> timeLoop = end1 - start1;

    auto start2 = chrono::high_resolution_clock::now();
    vector<int> mergedSet = mergeWithSet(a, b);
    auto end2 = chrono::high_resolution_clock::now();
    chrono::duration<double> timeSet = end2 - start2;

    cout << "\nРезультаты:\n";
    cout << "Размер объединённого массива (через цикл): " << mergedLoop.size() << endl;
    cout << "Время выполнения (цикл): " << timeLoop.count() << " сек\n";
    cout << "Размер объединённого массива (через unordered_set): " << mergedSet.size() << endl;
    cout << "Время выполнения (unordered_set): " << timeSet.count() << " сек\n";

    return 0;
}