# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 09:35:09 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$29,360.50`
- Equity: `$29,360.50`
- Realized PnL: `$19,360.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           90.48               21            1.69              0.85         71.48               125.47         0.838          pass              0.578             47.1                           0.429                8.64              0.654                                 ok            True                  False
    MU           89.29               28            1.60             12.65       1126.91               130.58         0.788          pass              0.551             34.8                           0.303               13.51              1.134                                 ok            True                  False
  INTC           92.59               27            1.81              1.62        127.62                98.20         0.672          pass              0.646             43.3                           0.282                1.15              0.551                                 ok            True                  False
   TRI           81.48               27            1.00              0.59         83.62                56.35         0.591          pass              0.212              0.0                           0.200                1.99              0.299                                 ok            True                  False
  GILD           85.00               20            0.84              0.76        127.56                29.34         0.559          pass              0.256              0.0                           0.223                1.63              0.108                                 ok            True                  False
  CPRT           84.62               13            2.00              0.43         30.37                31.57         0.522          pass              0.248             17.6                           0.206               -2.63             -0.119                                 ok            True                  False
  PCAR           87.10               31            0.70              0.59        120.43                36.52         0.514          pass              0.505             41.6                           0.448                1.11              0.042                                 ok            True                  False
   PEP           87.50               16            0.52              0.51        141.17                19.98         0.593          pass              0.395             31.8                           0.444               -2.50             -0.355            downtrend_blocked_slope           False                  False
  ROST           95.83               24            0.78              1.16        212.76                36.17         0.559          pass              0.627             25.9                           0.171              -11.88             -1.242 downtrend_blocked_slope_and_streak           False                  False
  PAYX          100.00               27            0.49              0.34         99.75                33.42         0.530          pass              0.769             67.5                           0.500               -1.21             -0.217                                 ok           False                  False
   KDP          100.00               28            0.24              0.06         33.38                25.91         0.521          pass              0.746             57.9                           0.315                5.83              0.542                                 ok           False                  False
  TMUS           76.92               13            1.80              2.30        181.70                27.84         0.511          pass              0.181             36.7                           0.325               -5.13             -0.393            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-06-29T09:28:38.144853-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-06-26T15:10:04.394440-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-06-26T15:05:02.631501-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-06-26T15:00:04.609792-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-06-26T14:55:05.737035-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-06-26T14:50:01.669190-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"budget": 14680.25, "entry_cost": 16617.5, "reason": "insufficient_cash", "ticker": "MU"}
2026-06-26T14:50:01.669190-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"early_entry_score": 0.416, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 3233.0, "option_spread_pct": 43.38, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "WBD", "timing_score": 0.62}
2026-06-26T14:50:01.669190-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-26", "training_samples": 5312, "window": 5}
2026-06-26T12:00:02.704488-04:00 early_entry_1200      early_entry_shadow {"contract_symbol": "TTWO260821C00240000", "current_drop_pct": 0.84, "early_entry_score": 0.702, "early_reclaim_pct": 62.3, "entry_ask": 17.3, "entry_bid": 16.2, "entry_mode": "early", "entry_option_price": 16.75, "hypothetical_budget": 14680.25, "hypothetical_contracts": 8, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 396.0, "option_spread_pct": 6.57, "option_volume": 80.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 91.43, "ticker": "TTWO", "timing_score": 0.438, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.702, "early_reclaim_pct": 62.3, "matched_signals": 35, "recovery_stability_score": 0.58, "success_rate": 91.43, "ticker": "TTWO", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-26T11:53:23.382476-04:00 early_entry_1150      early_entry_shadow  {"contract_symbol": "TTWO260821C00240000", "current_drop_pct": 0.68, "early_entry_score": 0.725, "early_reclaim_pct": 69.6, "entry_ask": 17.0, "entry_bid": 16.2, "entry_mode": "early", "entry_option_price": 16.6, "hypothetical_budget": 14680.25, "hypothetical_contracts": 8, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 396.0, "option_spread_pct": 4.82, "option_volume": 80.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.78, "shadow_only": true, "success_rate": 91.43, "ticker": "TTWO", "timing_score": 0.449, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.725, "early_reclaim_pct": 69.6, "matched_signals": 35, "recovery_stability_score": 0.78, "success_rate": 91.43, "ticker": "TTWO", "timing_score": 0.449, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629093509)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629093509)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629093509)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629093509)

</details>
