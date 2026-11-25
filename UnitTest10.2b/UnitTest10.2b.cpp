#include "pch.h"
#include "CppUnitTest.h"
#define UNIT_TEST
#include "../LABA-10.2b/LABA-10.2b.cpp"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest102b
{
    TEST_CLASS(UnitTest102b)
    {
    public:
        TEST_METHOD(TestPhysicalSort)
        {
            const int N = 4;
            Student p[N];
            p[0].prizv = "Andriyenko";  p[0].kurs = 2; p[0].spec = KN;  p[0].fizyka = 5; p[0].matematyka = 4; p[0].programuvannya = 5;
            p[1].prizv = "Zaharchenko"; p[1].kurs = 2; p[1].spec = INF; p[1].fizyka = 5; p[1].matematyka = 5; p[1].chyselni_metody = 4;
            p[2].prizv = "Boyko";       p[2].kurs = 1; p[2].spec = ME;  p[2].fizyka = 5; p[2].matematyka = 3; p[2].pedagogika = 4;
            p[3].prizv = "Koval";       p[3].kurs = 3; p[3].spec = FI;  p[3].fizyka = 3; p[3].matematyka = 5; p[3].pedagogika = 5;

            Sort(p, N);
            Assert::AreEqual(string("Koval"), p[0].prizv);
            Assert::AreEqual(string("Boyko"), p[1].prizv);
            Assert::AreEqual(string("Zaharchenko"), p[2].prizv);
            Assert::AreEqual(string("Andriyenko"), p[3].prizv);
        }

        TEST_METHOD(TestIndexSort)
        {
            const int N = 4;
            Student p[N];
            p[0].prizv = "Andriyenko";  p[0].kurs = 2; p[0].spec = KN;  p[0].fizyka = 5; p[0].matematyka = 4; p[0].programuvannya = 5;
            p[1].prizv = "Zaharchenko"; p[1].kurs = 2; p[1].spec = INF; p[1].fizyka = 5; p[1].matematyka = 5; p[1].chyselni_metody = 4;
            p[2].prizv = "Boyko";       p[2].kurs = 1; p[2].spec = ME;  p[2].fizyka = 5; p[2].matematyka = 3; p[2].pedagogika = 4;
            p[3].prizv = "Koval";       p[3].kurs = 3; p[3].spec = FI;  p[3].fizyka = 3; p[3].matematyka = 5; p[3].pedagogika = 5;

            int* I = IndexSort(p, N);
            Assert::AreEqual(3, I[0]);
            Assert::AreEqual(2, I[1]);
            Assert::AreEqual(1, I[2]);
            Assert::AreEqual(0, I[3]);
            delete[] I;
        }

        TEST_METHOD(TestBinarySearch)
        {
            const int N = 4;
            Student p[N];
            p[0].prizv = "Andriyenko";  p[0].kurs = 2; p[0].spec = KN;  p[0].fizyka = 5; p[0].matematyka = 4; p[0].programuvannya = 5;
            p[1].prizv = "Zaharchenko"; p[1].kurs = 2; p[1].spec = INF; p[1].fizyka = 5; p[1].matematyka = 5; p[1].chyselni_metody = 4;
            p[2].prizv = "Boyko";       p[2].kurs = 1; p[2].spec = ME;  p[2].fizyka = 5; p[2].matematyka = 3; p[2].pedagogika = 4;
            p[3].prizv = "Koval";       p[3].kurs = 3; p[3].spec = FI;  p[3].fizyka = 3; p[3].matematyka = 5; p[3].pedagogika = 5;

            Sort(p, N);
            Assert::AreEqual(2, BinSearch(p, N, "Zaharchenko", 2, 5));
            Assert::AreEqual(-1, BinSearch(p, N, "NonExistent", 1, 4));
        }
    };
}
