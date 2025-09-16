//Ситников задание три
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <chrono>

using namespace std;


vector<int> generateRandomVector(int size) {
    vector<int> vec;
    for (int i = 0; i < size; ++i) {
        vec.push_back(rand() % 1000); 
    }
    return vec;
}

// Метод 1: Простой метод (поэлементное сравнение)
// Сложность: O(n)
bool compareWithLoop(const vector<int>& a, const vector<int>& b) {
    if (a.size() != b.size()) return false;

    for (size_t i = 0; i < a.size(); ++i) {
        if (a[i] != b[i]) return false;
    }

    return true;
}

// Метод 2: Оптимизированный метод — оператор ==
// Сложность: O(n)
bool compareWithOperator(const vector<int>& a, const vector<int>& b) {
    return a == b;
}

int main() {
    setlocale(LC_ALL, "RU");
    srand(time(nullptr));

    int size1;
    cout << "Введите размер списка 1 для сравнения: ";
    cin >> size1;

    int size2;
    cout << "Введите размер списка 2 для сравнения: ";
    cin >> size2;

    vector<int> list1 = generateRandomVector(size1);
    vector<int> list2 = generateRandomVector(size2);

    // Сравнение через цикл
    auto start1 = chrono::high_resolution_clock::now();
    bool isEqualLoop = compareWithLoop(list1, list2);
    auto end1 = chrono::high_resolution_clock::now();
    chrono::duration<double> timeLoop = end1 - start1;

    // Сравнение через оператор ==
    auto start2 = chrono::high_resolution_clock::now();
    bool isEqualOp = compareWithOperator(list1, list2);
    auto end2 = chrono::high_resolution_clock::now();
    chrono::duration<double> timeOp = end2 - start2;

    // Вывод результатов
    cout << "\nРезультаты сравнения:\n";
    cout << "Списки равны (через цикл)? " << (isEqualLoop ? "Да" : "Нет") << endl;
    cout << "Время (цикл): " << timeLoop.count() << " сек\n";

    cout << "Списки равны (через operator==)? " << (isEqualOp ? "Да" : "Нет") << endl;
    cout << "Время (operator==): " << timeOp.count() << " сек\n";

    return 0;
}

