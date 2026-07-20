# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 10:50:05 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$31,411.75`
- Equity: `$31,411.75`
- Realized PnL: `$21,411.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260821C00290000      7          2026-07-17         2026-07-20        20.15      23.275 2187.5   15.508685 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           87.50               32            0.50              0.20         56.47                61.55         0.634          pass              0.643             77.7                           0.680               24.81              2.836                  ok            True                  False
   WBD           86.67               15            0.84              0.16         26.80                20.40         0.572          pass              0.343             25.0                           0.275                2.01              0.383                  ok            True                  False
  META           87.18               39            0.51              2.32        645.02                53.08         0.550          pass              0.640             66.9                           0.645                7.06              0.877                  ok            True                  False
  PAYX          100.00               28            0.83              0.67        114.10                33.31         0.529          pass              0.715             47.2                           0.671                7.63              0.819                  ok            True                  False
  GILD           92.00               25            0.69              0.65        134.00                34.72         0.526          pass              0.548             25.0                           0.260                2.89              0.042                  ok            True                  False
  MNST          100.00               25            0.57              0.39         97.33                20.09         0.514          pass              0.763             70.5                           0.389               -0.44              0.160                  ok            True                  False
  BKNG           85.71               21            1.73              2.20        180.74                41.44         0.514          pass              0.359             27.3                           0.325               -1.38              0.144                  ok            True                  False
   ADP           95.83               24            0.98              1.75        254.51                34.14         0.513          pass              0.668             41.2                           0.598                5.54              0.615                  ok            True                  False
  TEAM           85.00               40            0.72              0.47         93.09                69.60         0.513          pass              0.636             83.9                           0.770                8.33              0.795                  ok            True                  False
   CSX           91.30               23            0.60              0.21         50.66                17.40         0.513          pass              0.539             33.1                           0.223                3.35              0.447                  ok            True                  False
  PCAR           86.21               29            0.87              0.77        125.87                30.30         0.507          pass              0.383             13.4                           0.186               -0.64              0.106                  ok            True                  False
   ROP           92.86               28            1.04              2.63        362.01                31.85         0.503          pass              0.674             53.6                           0.711               -1.09             -0.038                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-07-20T10:50:05.022185-04:00 early_entry_1050 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:45:02.099135-04:00 early_entry_1045 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:40:04.090335-04:00 early_entry_1040 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:35:05.083590-04:00 early_entry_1035 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:30:04.102843-04:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:25:04.012806-04:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:20:01.111901-04:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:15:03.125789-04:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:10:05.108282-04:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T10:10:05.108282-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "TXN260821C00290000", "fill_price": 23.275, "pnl": 2187.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.51, "ticker": "TXN"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720105005)

</details>
