
#ifndef _LINUX_SIMD_POWERPC_H
#define	_LINUX_SIMD_POWERPC_H

static inline void preempt_disable(void) { printf("%s() line:%d\n", __func__, __LINE__); }
static inline void preempt_enable(void) { printf("%s() line:%d\n", __func__, __LINE__); }

static inline void enable_kernel_altivec(void) { printf("%s() line:%d\n", __func__, __LINE__); }
static inline void disable_kernel_altivec(void) { printf("%s() line:%d\n", __func__, __LINE__); }

static inline void enable_kernel_vsx(void) { printf("%s() line:%d\n", __func__, __LINE__); }
static inline void disable_kernel_vsx(void) { printf("%s() line:%d\n", __func__, __LINE__); }

static inline void enable_kernel_spe(void) { printf("%s() line:%d\n", __func__, __LINE__); }
static inline void disable_kernel_spe(void) { printf("%s() line:%d\n", __func__, __LINE__); }

#ifdef	CONFIG_ALTIVEC
#define	ENABLE_KERNEL_ALTIVEC	enable_kernel_altivec();
#define	DISABLE_KERNEL_ALTIVEC	disable_kernel_altivec();
#else
#define	ENABLE_KERNEL_ALTIVEC
#define	DISABLE_KERNEL_ALTIVEC
#endif

#ifdef	CONFIG_VSX
#define	ENABLE_KERNEL_VSX	enable_kernel_vsx();
#define	DISABLE_KERNEL_VSX	disable_kernel_vsx();
#else
#define	ENABLE_KERNEL_VSX
#define	DISABLE_KERNEL_VSX
#endif

#ifdef	CONFIG_SPE
#define	ENABLE_KERNEL_SPE	enable_kernel_spe();
#define	DISABLE_KERNEL_SPE	disable_kernel_spe();
#else
#define	ENABLE_KERNEL_SPE
#define	DISABLE_KERNEL_SPE
#endif

#define	kfpu_begin()				\
	{					\
		preempt_disable();		\
		ENABLE_KERNEL_ALTIVEC		\
		ENABLE_KERNEL_VSX		\
		ENABLE_KERNEL_SPE		\
	}

#define	kfpu_end()				\
	{					\
		DISABLE_KERNEL_SPE		\
		DISABLE_KERNEL_VSX		\
		DISABLE_KERNEL_ALTIVEC		\
		preempt_enable();		\
	}

#endif /* _LINUX_SIMD_POWERPC_H */
