#pragma once
#include <string>

enum Specialnist {
    KOMP_NAUKY,
    INFORMATYKA,
    MAT_EKON,
    FIZ_INF,
    TRUD_NAVCH
};

extern const std::string specialnistStr[];

struct Student {
    std::string prizv;
    unsigned kurs;
    Specialnist spec;
    int physics;
    int math;
    union {
        int programming;      // for KOMP_NAUKY
        int numericalMethods; // for INFORMATYKA
        int pedagogy;         // for others
    };
};

void Create(Student* p, int N);
void Print(const Student* p, int N);
bool compareStudents(const Student& a, const Student& b);
void PhysicalSort(Student* p, int N);
void BuildIndexArray(const Student* p, int N, int* idx);
void PrintWithIndex(const Student* p, int N, const int* idx);
int BinarySearch(const Student* p, int N, const std::string& prizv, unsigned kurs, int physics);
