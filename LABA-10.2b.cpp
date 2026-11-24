#include <iostream>
#include <Windows.h>
#include <string>
#include "LABA-10.2b/student2b.h"

using namespace std;

int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    int N;
    cout << "Введіть кількість студентів: ";
    while (!(cin >> N) || N <= 0)
    {
        cout << "Помилка! Введіть додатне ціле число: ";
        cin.clear();
        cin.ignore(10000, '\n');
    }

    Student* p = new Student[N];
    int* idx = new int[N];

    Create(p, N);
    cout << "Початковий масив студентів:" << endl;
    Print(p, N);

    int menuItem;
    do
    {
        cout << "Виберіть дію:" << endl;
        cout << "  [1] - фізичне впорядкування масиву" << endl;
        cout << "  [2] - індексне впорядкування та вивід масиву" << endl;
        cout << "  [3] - бінарний пошук студента" << endl;
        cout << "  [0] - вихід та завершення роботи програми" << endl;
        cout << "Введіть значення: ";
        if (!(cin >> menuItem))
        {
            cin.clear();
            cin.ignore(10000, '\n');
            menuItem = -1;
        }
        cout << endl;

        switch (menuItem)
        {
        case 1:
            PhysicalSort(p, N);
            cout << "Масив після фізичного впорядкування:" << endl;
            Print(p, N);
            break;
        case 2:
            BuildIndexArray(p, N, idx);
            cout << "Масив за індексним впорядкуванням:" << endl;
            PrintWithIndex(p, N, idx);
            break;
        case 3:
        {
            PhysicalSort(p, N);
            string prizv;
            unsigned kurs;
            int physics;
            cin.get();
            cin.sync();
            cout << "Введіть дані студента для пошуку:" << endl;
            cout << "  прізвище: "; getline(cin, prizv);
            cout << "  курс: "; cin >> kurs;
            cout << "  оцінка з фізики: "; cin >> physics;

            int found = BinarySearch(p, N, prizv, kurs, physics);
            if (found != -1)
                cout << "Знайдено студента на позиції № " << found + 1 << " у відсортованому масиві." << endl << endl;
            else
                cout << "Шуканого студента не знайдено." << endl << endl;
            break;
        }
        case 0:
            break;
        default:
            cout << "Ви ввели помилкове значення! Спробуйте ще раз." << endl << endl;
        }
    } while (menuItem != 0);

    delete[] idx;
    delete[] p;
    return 0;
}
