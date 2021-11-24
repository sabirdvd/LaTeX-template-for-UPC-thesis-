def testFunction_numpy_v2(C, Mi, C_new, Mi_new):
    Wg_new = np.linalg.solve(C_new, Mi_new)
    Cg_new = -0.5 * (Mi_new.conj() * Wg_new).sum(0)
    return C_new, Mi_new, Wg_new, Cg_new

@jax.jit
def testFunction_JAX_v2(C, Mi, C_new, Mi_new):
    Wg_new = jnp.linalg.solve(C_new, Mi_new)
    Cg_new = -0.5 * (Mi_new.conj() * Wg_new).sum(0)
    return C_new, Mi_new, Wg_new, Cg_new

%timeit testFunction_numpy_v2(C, Mi, C_new, Mi_new)
# 1000 loops, best of 3: 1.11 ms per loop
%timeit testFunction_JAX_v2(C_jax, Mi_jax, C_new_jax, Mi_new_jax)
# 1000 loops, best of 3: 1.35 ms per loop