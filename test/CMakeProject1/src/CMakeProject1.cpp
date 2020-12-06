

#define _CRTDBG_MAP_ALLOC
#ifdef _MSC_VER
#include <crtdbg.h>

#include <stdlib.h>
#include "CMakeProject1.h"

#else
#define _ASSERT(expr) ((void)0)

#define _ASSERTE(expr) ((void)0)
#endif

using namespace std;

typedef struct VehicleSize {
	long	 width;
	long	 length;
	long* height	/* OPTIONAL */;
	~VehicleSize() {
		delete height;
	}
} VehicleSize_t;

int main()
{
	VehicleSize_t* vs;
	vs = new VehicleSize_t;
	vs->width = 100;
	vs->length = 100;
	vs->height = new long(100);
	delete vs;
	
	//int* p=nullptr;
	//p = (int*)malloc(sizeof(int));
	// *p = 1;

	// if (p == NULL)cout << "p si null" << endl;
	// if (*p == 0)cout << "p is 0" << endl;
	// delete p;
	// p = NULL;
#ifdef _MSC_VER
	_CrtDumpMemoryLeaks();
#endif 
	return 0;
}