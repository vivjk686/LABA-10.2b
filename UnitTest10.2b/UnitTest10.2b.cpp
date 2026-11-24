#include "pch.h"
#include "CppUnitTest.h"
#include "../LABA-10.2b/student2b.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest102b
{
    static Student MakeStudent(const std::string& prizv, unsigned kurs, Specialnist spec, int physics, int math, int third)
    {
        Student s;
        s.prizv = prizv;
        s.kurs = kurs;
        s.spec = spec;
        s.physics = physics;
        s.math = math;
        if (spec == KOMP_NAUKY)
            s.programming = third;
        else if (spec == INFORMATYKA)
            s.numericalMethods = third;
        else
            s.pedagogy = third;
        return s;
    }

    TEST_CLASS(UnitTest102b)
    {
    public:
        TEST_METHOD(TestPhysicalSort)
        {
            const int N = 4;
            Student students[N] = {
                MakeStudent("Коваленко", 1, KOMP_NAUKY,  5, 5, 5),
                MakeStudent("Іваненко",  2, INFORMATYKA, 4, 4, 4),
                MakeStudent("Петренко",  1, MAT_EKON,    3, 5, 4),
                MakeStudent("Сидоренко", 1, FIZ_INF,     5, 3, 5)
            };

            PhysicalSort(students, N);

            Assert::AreEqual(std::string("Петренко"), students[0].prizv);
            Assert::AreEqual(std::string("Іваненко"), students[1].prizv);
            Assert::AreEqual(std::string("Сидоренко"), students[2].prizv);
            Assert::AreEqual(std::string("Коваленко"), students[3].prizv);
        }

        TEST_METHOD(TestIndexSort)
        {
            const int N = 4;
            Student students[N] = {
                MakeStudent("Коваленко", 1, KOMP_NAUKY,  5, 5, 5),
                MakeStudent("Іваненко",  2, INFORMATYKA, 4, 4, 4),
                MakeStudent("Петренко",  1, MAT_EKON,    3, 5, 4),
                MakeStudent("Сидоренко", 1, FIZ_INF,     5, 3, 5)
            };

            int idx[N] = { 0 };
            BuildIndexArray(students, N, idx);

            Assert::AreEqual(2, idx[0]);
            Assert::AreEqual(1, idx[1]);
            Assert::AreEqual(3, idx[2]);
            Assert::AreEqual(0, idx[3]);
        }

        TEST_METHOD(TestBinarySearch)
        {
            const int N = 4;
            Student students[N] = {
                MakeStudent("Коваленко", 1, KOMP_NAUKY,  5, 5, 5),
                MakeStudent("Іваненко",  2, INFORMATYKA, 4, 4, 4),
                MakeStudent("Петренко",  1, MAT_EKON,    3, 5, 4),
                MakeStudent("Сидоренко", 1, FIZ_INF,     5, 3, 5)
            };

            PhysicalSort(students, N);

            int pos1 = BinarySearch(students, N, "Сидоренко", 1, 5);
            Assert::AreEqual(2, pos1);

            int pos2 = BinarySearch(students, N, "Петренко", 1, 3);
            Assert::AreEqual(0, pos2);

            int notFound = BinarySearch(students, N, "Мельник", 2, 4);
            Assert::AreEqual(-1, notFound);
        }
    };
}
