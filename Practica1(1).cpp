//Cитников
#include <iostream>    
#include <vector>       
#include <cstdlib>      
#include <ctime>        
#include <chrono>       
#include <locale>       
using namespace std;

vector<int> generateRandomVector(int size) {
    vector<int> vec;
    for (int i = 0; i < size; ++i) {
        vec.push_back(rand() % 10); // числа от 0 до 9
    }
    return vec;
}

// Сложность: O(n * m)
bool isSublist(const vector<int>& mainList, const vector<int>& subList) {
    if (subList.size() > mainList.size()) return false;

    for (size_t i = 0; i <= mainList.size() - subList.size(); ++i) {
        bool match = true;
        for (size_t j = 0; j < subList.size(); ++j) {
            if (mainList[i + j] != subList[j]) {
                match = false;
                break;
            }
        }
        if (match) return true;
    }

    return false;
}

int main() {
    setlocale(LC_ALL, "Russian"); 
    srand(time(nullptr));         

    int mainSize, subSize;

    cout << "Введите размер основного списка (mainList): ";
    cin >> mainSize;

    cout << "Введите размер подсписка (subList): ";
    cin >> subSize;

    if (subSize > mainSize) {
        cout << "Ошибка: подсписок не может быть больше основного списка." << endl;
        return 1;
    }

    vector<int> mainList = generateRandomVector(mainSize);
    vector<int> subList = generateRandomVector(subSize);


    cout << "Основной список: ";
    for (int num : mainList) cout << num << " ";
    cout << endl;

    cout << "Подсписок:       ";
    for (int num : subList) cout << num << " ";
    cout << endl;

 
    auto start = chrono::high_resolution_clock::now();
    bool found = isSublist(mainList, subList);
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double, milli> duration = end - start;

    if (found) {
        cout << "Подсписок найден в основном списке." << endl;
    }
    else {
        cout << "Подсписок НЕ найден." << endl;
    }

    cout << "Время выполнения: " << duration.count() << " мс" << endl;

    return 0;
}

