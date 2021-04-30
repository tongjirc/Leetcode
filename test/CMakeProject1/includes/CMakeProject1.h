// CMakeProject1.h: 标准系统包含文件的包含文件
// 或项目特定的包含文件。

#pragma once

#define _CRTDBG_MAP_ALLOC

#ifdef _MSC_VER
#include <crtdbg.h>

#else
#define _ASSERT(expr) ((void)0)

#define _ASSERTE(expr) ((void)0)
#endif


#include <stdlib.h>
#include <unordered_map>
#include <hash_set>
#include <map>
#include <memory>
#include <iostream>
#include <vector>

// TODO: 在此处引用程序需要的其他标头。
