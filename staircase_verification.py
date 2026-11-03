"""Exact-integer verification utilities for the odd-power staircase project.
 
The script uses only the Python standard library. It is a computational
reproducibility aid; finite tests do not replace the proofs in the report.
"""
# SPDX-License-Identifier: MIT
# Extracted from Appendix B of the accompanying report.
from __future__ import annotations
 
from math import gcd, isqrt, lcm, prod
from typing import Iterable
 
 
def primes_up_to(n: int) -> list[int]:
    """Return all primes p <= n by the sieve of Eratosthenes."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            for q in range(p * p, n + 1, p):
                sieve[q] = False
    return [p for p, flag in enumerate(sieve) if flag]
 
 
def vp(value: int, p: int) -> int:
    """The p-adic valuation v_p(value), for a positive integer value."""
    if value <= 0 or p < 2:
        raise ValueError("value and p must be positive, with p >= 2")
    e = 0
    while value % p == 0:
        value //= p
        e += 1
    return e
 
 
def power_sum(n: int, k: int) -> int:
    if n < 1 or k < 1:
        raise ValueError("n and k must be positive")
    return sum(j**k for j in range(1, n + 1))
 
 
def staircase_data(n: int, d: int, k: int) -> tuple[int, int, int]:
    """Return (r, Q_r(n), reduced remainder) using the reduction lemma."""
    if n < 2 or d <= 0 or d % 2 or k < 3 or k % 2 == 0:
        raise ValueError("require n>=2, positive even d, and odd k>=3")
    r = min(n, (k - 1) // 2)
    q = prod(range(n - r + 1, n + 1))
    rem = (pow(d, k - r, q) * sum(pow(j, k, q) for j in range(1, n + 1))) % q
    return r, q, rem
 
 
def staircase_test(n: int, d: int, k: int) -> bool:
    """Check D_r(n,d) | S_k(n,d) by an exact reduced modular computation."""
    return staircase_data(n, d, k)[2] == 0
 
 
def d_criterion_requires_prime(n: int, p: int) -> bool:
    """D criterion: whether odd prime p must divide d*(n), for p <= n."""
    if n < 2 or p not in primes_up_to(n):
        raise ValueError("p must be prime and no greater than n")
    if p == 2:
        return True
    b = vp(__import__('math').factorial(n), p)
    s = vp(n * (n + 1), p)
    return b > max(0, 2 * s - 1)
 
 
def d_star(n: int) -> int:
    """Compute d*(n) from finite formula A, using exact integer arithmetic."""
    if n < 2:
        raise ValueError("n must be at least 2")
    from math import factorial
    result = 1
    for p in primes_up_to(n):
        b = vp(factorial(n), p)
        eta = int(d_criterion_requires_prime(n, p))
        alpha = eta
        for t in range(1, max(0, b - 2) + 1):
            q_t = prod(range(n - t + 1, n + 1))
            p_sum = power_sum(n, 2 * t + 1)
            gap = vp(q_t, p) - vp(p_sum, p)
            c = max(0, (gap + (t + 1) - 1) // (t + 1))
            alpha = max(alpha, c)
        result *= p**alpha
    return result
 
 
def lambda_prime_power(p: int, exponent: int) -> int:
    """Carmichael lambda(p**exponent)."""
    if exponent < 1:
        raise ValueError("exponent must be positive")
    if p == 2:
        if exponent == 1:
            return 1
        if exponent == 2:
            return 2
        return 2 ** (exponent - 2)
    return (p - 1) * p ** (exponent - 1)
 
 
def lambda_factorial(n: int) -> int:
    """Carmichael lambda(n!) from its prime-power factorization."""
    from math import factorial
    return lcm(*(lambda_prime_power(p, vp(factorial(n), p))
                 for p in primes_up_to(n)))
 
 
def phi_factorial(n: int) -> int:
    """Euler phi(n!) from its prime-power factorization."""
    from math import factorial
    return prod((p - 1) * p ** (vp(factorial(n), p) - 1)
                for p in primes_up_to(n))
 
 
def finite_period(n: int, d: int) -> int:
    """A valid even period T_d for the tail k >= 2n+1."""
    from math import factorial
    if n < 2 or d <= 0 or d % 2:
        raise ValueError("require n>=2 and positive even d")
    periods = [2]
    for p in primes_up_to(n):
        if d % p:
            periods.append(lambda_prime_power(p, vp(factorial(n), p)))
    return lcm(*periods)
 
 
def finite_certificate_passes(n: int, d: int) -> bool:
    """Check all odd k in 3 <= k < 2n+1+T_d."""
    t = finite_period(n, d)
    upper = 2 * n + 1 + t
    return all(staircase_test(n, d, k) for k in range(3, upper, 2))
 
 
def maximal_depth(n: int, d: int, k: int) -> int:
    """Compute H(n,d,k) directly from the original integer quantities."""
    if n < 2 or d <= 0 or d % 2 or k < 1:
        raise ValueError("require n>=2, positive even d, and k>=1")
    s = d**k * power_sum(n, k)
    best = 0
    q = 1
    for h in range(1, n + 1):
        q *= (n - h + 1) * d
        if s % q == 0:
            best = h
    return best
 
 
def candidate_filter(n: int, d: int) -> bool:
    """D-only necessary-prime filter; passing does NOT prove d is sufficient."""
    return all(d % p == 0 for p in primes_up_to(n)
               if p != 2 and d_criterion_requires_prime(n, p))
 
 
def verify_report_claims() -> dict[str, object]:
    """Re-run the explicit test ranges reported in the revised document."""
    # Theorem classification: 96 values outside {2,3,5} have concrete
    # counterexamples (d=2,k=5, except n=9 where k=7 is used).
    counterexamples = []
    for n in range(2, 101):
        if n in {2, 3, 5}:
            continue
        k = 7 if n == 9 else 5
        if staircase_test(n, 2, k):
            raise AssertionError(f"unexpected pass in classification test: n={n}, k={k}")
        counterexamples.append((n, k))
 
    # Sufficiency examples for n=2,3,5: 30 d-values x 100 odd powers.
    basic_checks = 0
    for n in (2, 3, 5):
        for d in range(2, 61, 2):
            for k in range(3, 202, 2):
                assert staircase_test(n, d, k), (n, d, k)
                basic_checks += 1
 
    # Formula A: 99 n-values x 100 odd powers = 9,900 checks.
    astar_checks = 0
    d_values = {}
    for n in range(2, 101):
        ds = d_star(n)
        d_values[n] = ds
        for k in range(3, 202, 2):
            assert staircase_test(n, ds, k), (n, ds, k)
            astar_checks += 1
 
    # Independent candidate search over even divisors of lcm(1,...,n), n=2..20.
    from math import lcm as _lcm
    candidate_total = d_filter_kept = exact_pass = 0
    per_n = []
    for n in range(2, 21):
        L = 1
        for j in range(1, n + 1):
            L = _lcm(L, j)
        total_n = keep_n = pass_n = 0
        for d in range(2, L + 1, 2):
            if L % d:
                continue
            total_n += 1
            ok_d = candidate_filter(n, d)
            if ok_d:
                keep_n += 1
                if d % d_star(n) == 0:
                    pass_n += 1
        candidate_total += total_n
        d_filter_kept += keep_n
        exact_pass += pass_n
        per_n.append((n, total_n, keep_n, pass_n, d_star(n)))
 
    # Finite-period certificate and period table (compare against a direct
    # prefix check to k=1001 for each listed example).
    b_rows = []
    for n in (6, 8, 9, 10, 12):
        d = d_star(n)
        t = finite_period(n, d)
        assert finite_certificate_passes(n, d), (n, d, t)
        for k in range(3, 1002, 2):
            assert staircase_test(n, d, k), (n, d, k)
        phi_checks = n - 1 + phi_factorial(n) // 2
        lambda_checks = n - 1 + lambda_factorial(n) // 2
        b_rows.append((n, d, phi_checks, lambda_checks, t, n + t // 2 - 1))

 
    # H table for n=5; a transparent grid of 10 even d values and 16 powers.
    h_checks = 0
    for d in range(2, 22, 2):
        for k in range(3, 34, 2):
            actual = maximal_depth(5, d, k)
            if k == 3:
                expected = 2 if d % 4 == 0 else 1
            elif k == 5:
                expected = 4 if d % 8 == 0 else 3
            elif k == 7:
                expected = 5 if d % 4 == 0 else 4
            else:
                expected = 5
            assert actual == expected, (d, k, actual, expected)
            h_checks += 1
 
    return {
        "classification_counterexamples": len(counterexamples),
        "classification_examples": counterexamples,
        "sufficiency_checks": basic_checks,
        "A_formula_checks": astar_checks,
        "d_star_examples": {n: d_values[n] for n in (2, 3, 4, 5, 7, 9, 10, 12, 17)},
        "candidate_filter": {
            "total": candidate_total,
            "after_D": d_filter_kept,
            "exactly_sufficient_by_A": exact_pass,
            "D_only_false_positives": d_filter_kept - exact_pass,
            "per_n": per_n,
        },
        "B_period_rows": b_rows,
        "H_table_checks": h_checks,
    }
 
 
if __name__ == "__main__":
    import pprint
    pprint.pp(verify_report_claims(), sort_dicts=False)
    print("\nExample A: d*(17) =", d_star(17))
    print("Example check: staircase_test(5, 2, 7) =", staircase_test(5, 2, 7))
    print("Example check: staircase_test(9, 2, 7) =", staircase_test(9, 2, 7))
