//�������� ������� ���
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

// ����� 1: ������� ����� (������������ ���������)
// ���������: O(n)
bool compareWithLoop(const vector<int>& a, const vector<int>& b) {
    if (a.size() != b.size()) return false;

    for (size_t i = 0; i < a.size(); ++i) {
        if (a[i] != b[i]) return false;
    }

    return true;
}

// ����� 2: ���������������� ����� � �������� ==
// ���������: O(n)
bool compareWithOperator(const vector<int>& a, const vector<int>& b) {
    return a == b;
}

int main() {
    setlocale(LC_ALL, "RU");
    srand(time(nullptr));

    int size1;
    cout << "������� ������ ������ 1 ��� ���������: ";
    cin >> size1;

    int size2;
    cout << "������� ������ ������ 2 ��� ���������: ";
    cin >> size2;

    vector<int> list1 = generateRandomVector(size1);
    vector<int> list2 = generateRandomVector(size2);

    // ��������� ����� ����
    auto start1 = chrono::high_resolution_clock::now();
    bool isEqualLoop = compareWithLoop(list1, list2);
    auto end1 = chrono::high_resolution_clock::now();
    chrono::duration<double> timeLoop = end1 - start1;

    // ��������� ����� �������� ==
    auto start2 = chrono::high_resolution_clock::now();
    bool isEqualOp = compareWithOperator(list1, list2);
    auto end2 = chrono::high_resolution_clock::now();
    chrono::duration<double> timeOp = end2 - start2;

    // ����� �����������
    cout << "\n���������� ���������:\n";
    cout << "������ ����� (����� ����)? " << (isEqualLoop ? "��" : "���") << endl;
    cout << "����� (����): " << timeLoop.count() << " ���\n";

    cout << "������ ����� (����� operator==)? " << (isEqualOp ? "��" : "���") << endl;
    cout << "����� (operator==): " << timeOp.count() << " ���\n";

    return 0;
}

