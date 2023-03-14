
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

static inline void kfpu_begin(void)
{
#ifdef	CONFIG_ALTIVEC
	enable_kernel_altivec();
#endif
#ifdef	CONFIG_VSX
	enable_kernel_vsx();
#endif
#ifdef CONFIG_SPE
	enable_kernel_spe();
#endif
	preempt_disable();
}

#define	kfpu_end()				\
	{					\
#ifdef CONFIG_SPE				\
		disable_kernel_spe();		\
#endif						\
#ifdef	CONFIG_VSX				\
		disable_kernel_vsx();		\
#endif						\
#ifdef	CONFIG_ALTIVEC				\
		disable_kernel_altivec();	\
#endif						\
		preempt_enable();		\
	}

#endif /* _LINUX_SIMD_POWERPC_H */
