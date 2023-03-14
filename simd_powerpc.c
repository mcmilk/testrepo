
#include <stdio.h>

//#define CONFIG_ALTIVEC
//#define CONFIG_VSX
//#define CONFIG_SPE

#include "simd_powerpc.h"

int main(void) {
  printf("kfpu_begin");
  kfpu_begin();

  printf("SIMD STUFF");

  printf("kfpu_end");
  kfpu_end();
}
