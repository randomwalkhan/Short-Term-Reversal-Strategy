# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-01 10:15:02 EDT`
Last processed slot: `early_entry_1015`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$46,498.30`
- Equity: `$82,998.30`
- Realized PnL: `$75,238.30`
- Unrealized PnL: `$-2,240.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META261120C00735000       2026-09-30                   1      8     38740.0                 36500.0        48.42          45.62      733.79        723.11          bid_ask_mid                      45.62                bid_ask_mid                    True         -2240.0                  -5.78         84.38               32              0.68         44.85           47.81                   54.8                 798.0          103.0               0.02                      ok
```

## Today's Closed Trades (2026-10-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  SOXL           85.29               34            0.97              1.01        147.43               113.77         0.702          pass              0.529             52.5                           0.313               27.60              1.770                       ok            True                  False
  AMGN           85.00               20            1.06              3.14        420.17                46.02         0.605          pass              0.417             52.2                           0.340                9.81              1.006                       ok            True                  False
  INTC           88.57               35            1.35              1.14        119.74                73.63         0.567          pass              0.582             43.4                           0.360                9.01              0.512                       ok            True                  False
  MPWR           91.18               34            0.56              5.32       1344.94                50.40         0.538          pass              0.671             53.1                           0.400               14.71              1.127                       ok            True                  False
  ASML           82.35               34            0.52              6.60       1808.84                42.37         0.538          pass              0.399             41.0                           0.256               10.59              0.945                       ok            True                  False
   STX           87.88               33            0.99              6.36        919.61                53.17         0.514          pass              0.620             68.2                           0.426               13.80              0.961                       ok            True                  False
  MRVL           82.35               34            1.13              2.09        263.31                55.88         0.506          pass              0.438             54.9                           0.382                8.50              0.648                       ok            True                  False
  DRAM           79.41               34            0.53              0.22         60.26                53.77         0.566          pass              0.352             45.3                           0.259                3.91              0.092                       ok           False                  False
  META           87.18               39            0.22              1.11        724.71                55.93         0.562          pass              0.625             61.4                           0.261                6.14              0.532                       ok           False                  False
  CRWD           89.13               46            0.25              0.46        264.55                63.45         0.538          pass              0.761             88.0                           0.631                7.49              0.893                       ok           False                  False
  QCOM           92.68               41            0.22              0.28        183.92                56.29         0.521          pass              0.753             54.3                           0.327               -2.69             -0.223 downtrend_blocked_streak           False                  False
   XEL           83.33               18            0.70              0.34         70.33                18.32         0.518          pass              0.344             49.9                           0.559               -4.94             -0.447  downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-10-01T10:15:02.462190-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:10:05.306830-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:05:05.587824-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "FTNT261120C00175000", "current_drop_pct": 0.7, "early_entry_score": 0.716, "early_reclaim_pct": 66.3, "entry_ask": 17.55, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 16.425, "hypothetical_budget": 23249.15, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 78.0, "option_spread_pct": 13.7, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.567, "shadow_only": true, "success_rate": 90.24, "ticker": "FTNT", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.716, "early_reclaim_pct": 66.3, "matched_signals": 41, "recovery_stability_score": 0.567, "success_rate": 90.24, "ticker": "FTNT", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-01T10:00:05.588413-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T00:00:05.224460-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 92, 'empty': 1}
2026-09-30T15:10:04.050158-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-30T15:05:04.200259-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-30T15:00:05.217258-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-30T14:55:06.123157-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-09-30T14:50:06.616315-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"allocated_cash": 38740.0, "asset_type": "option", "contract_symbol": "META261120C00735000", "contracts": 8, "early_entry_score": 0.534, "entry_mode": "regular", "entry_option_price": 48.425, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 798.0, "option_spread_pct": 1.55, "option_volume": 103.0, "success_rate": 84.38, "ticker": "META", "timing_score": 0.562}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261001101502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261001101502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261001101502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261001101502)

</details>
