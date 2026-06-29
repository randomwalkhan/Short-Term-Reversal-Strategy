# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-29 10:10:06 EDT`
Last processed slot: `manage_1000`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   TRI           81.82               33            0.55              0.32         83.73                56.35         0.578          pass              0.429             56.6                           0.351                2.46              0.320                      ok            True                  False
  GILD           87.50               16            1.30              1.16        127.38                29.34         0.554          pass              0.331             11.7                           0.130                1.16              0.087                      ok            True                  False
  PCAR           84.62               26            0.90              0.76        120.35                36.52         0.530          pass              0.403             40.1                           0.479                0.90              0.033                      ok            True                  False
  SOXL           92.86               14            7.01             10.58        211.07               243.65         0.847          pass              0.460              1.9                           0.182              -14.57             -1.471 downtrend_blocked_slope           False                  False
  MRVL          100.00               13            5.06              9.44        262.72               157.15         0.781          pass              0.524              8.7                           0.162               -9.45             -1.139 downtrend_blocked_slope           False                  False
  ASML           97.14               35            0.22              2.78       1793.43                67.49         0.686          pass              0.829             64.5                           0.427               -3.91             -0.498 downtrend_blocked_slope           False                  False
  DRAM           83.33                6            5.91              2.98         70.60               125.47         0.667          pass              0.167              3.8                           0.106                4.03              0.457                      ok           False                  False
  MPWR           89.29               28            1.52             13.94       1307.34                89.21         0.628          pass              0.492             20.5                           0.227              -18.00             -1.951 downtrend_blocked_slope           False                  False
   TXN           92.86               14            2.47              4.93        283.31                70.58         0.628          pass              0.446              4.5                           0.148               -7.55             -0.689 downtrend_blocked_slope           False                  False
  QCOM           86.36               22            1.68              2.23        188.43                89.86         0.623          pass              0.321              3.0                           0.179              -12.05             -1.492 downtrend_blocked_slope           False                  False
  MCHP          100.00               20            2.08              1.28         87.38                74.63         0.618          pass              0.561             10.7                           0.187               -9.60             -1.074 downtrend_blocked_slope           False                  False
  NXPI           90.00               20            1.73              3.36        275.58                66.10         0.614          pass              0.399              1.3                           0.078              -10.40             -1.052 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                detail
2026-06-29T10:10:06.044962-04:00 early_entry_1010      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:05:56.914447-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T09:28:38.144853-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                         {'saved': 93}
2026-06-26T15:10:04.394440-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-26T15:05:02.631501-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-26T15:00:04.609792-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-26T14:55:05.737035-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-26T14:50:01.669190-04:00       entry_1500           entry_skipped                                                                                                                                                            {"budget": 14680.25, "entry_cost": 16617.5, "reason": "insufficient_cash", "ticker": "MU"}
2026-06-26T14:50:01.669190-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.416, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 3233.0, "option_spread_pct": 43.38, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "WBD", "timing_score": 0.62}
2026-06-26T14:50:01.669190-04:00       entry_1500          timing_overlay                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-26", "training_samples": 5312, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260629101006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260629101006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260629101006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260629101006)

</details>
