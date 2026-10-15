# S4 — Coverage statement for TD-CP and its assumptions

## Setting
- f: a calibration fitted on primary-instrument spectra of the master set.
- r_1,…,r_n: calibration residuals of the primary instrument. In practice these are out-of-fold residuals.
- T: a transfer map fitted on k transfer pairs. δ_j = f(x_j^P) − f(T_{−j}(x_j^S)), j = 1,…,k, are the cross-fitted transfer discrepancies.
- For a new sample with unknown y and secondary spectrum x^S, write ŷ = f(T(x^S)) and decompose its error exactly:

  y − ŷ = r + δ,  with r = y − f(x^P) and δ = f(x^P) − f(T(x^S)).

  Neither r nor δ is observed for the new sample, because its primary spectrum x^P is never measured.

- Let S = {r_i + δ_j : i ≤ n, j ≤ k} (size nk), and m = ⌈(1 − α/2)(n + 1)k⌉. TD-CP sets U to the m-th smallest element of S and L to the m-th largest. If m > nk, then U = +∞ and L = −∞.

## Assumptions
- (A1) r_1,…,r_n, r are exchangeable.
- (A2) The discrepancies are independent of the residuals: (δ_1,…,δ_k, δ) ⟂ (r_1,…,r_n, r).
- (A3) δ_1,…,δ_k, δ are i.i.d. with continuous cdf F_δ.

## Proposition 1
(a) *Empirical-discrepancy coverage.* Let J be uniform on {1,…,k}, independent of everything else. Under (A1)–(A2),

  P(L ≤ r + δ_J ≤ U) ≥ 1 − α.

(b) *Coverage for a new sample.* Under (A1)–(A3), conditionally on δ_1,…,δ_k,

  P(L ≤ y − ŷ ≤ U | δ_{1:k}) ≥ 1 − α − 2 D_k,  where D_k = sup_t |F̂_k(t) − F_δ(t)|.

By the Dvoretzky–Kiefer–Wolfowitz inequality with Massart's constant, P(D_k > ε) ≤ 2 exp(−2kε²).

### Proof
(a) Write r_0 = r, and let S⁺ = {r_i + δ_j : 0 ≤ i ≤ n, 1 ≤ j ≤ k} (size (n+1)k). Adding elements to a multiset can only lower its m-th smallest element, so the m-th smallest element of S⁺ is ≤ U. Hence the event {r_0 + δ_J > U} implies that r_0 + δ_J has rank > m in S⁺.

Condition on the δ's. By (A1)–(A2), the vector (r_0,…,r_n) is exchangeable and independent of (δ, J). So the rank of r_0 + δ_J in S⁺ has the same distribution as the rank of r_I + δ_J, where I is uniform on {0,…,n} and independent of J. The cell (I, J) is then uniform over all (n+1)k cells, and so (breaking ties at random) the rank is uniform on {1,…,(n+1)k}. Therefore

  P(rank > m) ≤ ((n+1)k − m)/((n+1)k) ≤ α/2.

The lower tail is symmetric. A union bound over the two tails completes (a). The same argument applied to the single upper tail of |r_i + δ_j| at level α, with m = ⌈(1 − α)(n + 1)k⌉, proves (a) for the absolute-score interval of Eq. (4) in the main text. Part (b) carries over with one D_k term in place of two.

(b) Condition on δ_{1:k} and on the r's. The probability that r + δ > U is 1 − F_δ(U − r). The corresponding probability for δ_J is 1 − F̂_k(U − r). These differ by at most D_k. Taking expectations over r and applying (a) to each tail gives miscoverage ≤ α + 2D_k. ∎

## Remarks (stated honestly in the manuscript)
0. **TD-CP+ (Eq. 6) is not covered by Proposition 1.** Its validity is established empirically. The jackknife+ worst-case bound of 1 − 2α (Barber et al., 2021) would require exchangeable leave-one-out scores, and these hold for our combined radii only under (A1)–(A3).
1. **(A2) is an assumption, not a theorem.** It can fail when large residuals and large discrepancies occur in the same samples, for example at extreme compositions. The benchmark reports the held-out Spearman correlation between r and δ as a diagnostic (Table S1, Fig. 7 of the main text). This diagnostic uses reference values of test samples. It is not available in deployment and is never used by the method.
2. **Cross-fitting.** δ_j uses T_{−j}, which is fitted on k − 1 pairs, while the deployed map uses all k pairs. The cross-fitted discrepancies are therefore slightly pessimistic. This is the same price the jackknife+ pays (Barber et al., 2021). In-sample discrepancies are optimistic. For DS with k < p, the pseudo-inverse reproduces the transfer spectra exactly, so in-sample δ ≡ 0 and TD-CP would collapse to the naive interval. Ablation A1 tests this.
3. **Out-of-fold residuals.** (A1) holds exactly for split-conformal residuals. The study uses 10-fold out-of-fold residuals so that no calibration sample is lost. The naive interval evaluated on primary-instrument test spectra checks empirically that this choice is close to valid (method `naive_cp_primary_test`).
4. **Small k.** The bound in (b) becomes loose as k gets small: E[D_k] ≈ 0.87/√k. The k-sensitivity experiment shows how much of this gap appears in practice.
