# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 10:25:06 EST`
Last processed slot: `manage_1030`

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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ADI           81.25               16            1.78              5.23        417.55                38.61         0.501            pass              0.149              8.5                           0.235                1.57              0.583                                 ok            True                  False
  INTC           66.67               21            3.01              1.27         60.00               129.60         0.751            pass              0.233             28.3                           0.342              -36.82             -4.951            downtrend_blocked_slope           False                  False
  SOXL           65.00               20            5.10              2.61         72.00               167.58         0.616            pass              0.237             36.3                           0.293              -32.79             -3.064            downtrend_blocked_slope           False                  False
  REGN           83.33                6            2.33             15.85        966.57                48.26         0.575            pass              0.185             12.9                           0.199               18.00              2.119                                 ok           False                  False
  DRAM           65.00               20            2.30              0.77         47.31                69.30         0.572            pass              0.236             37.4                           0.303               -5.32             -0.129                                 ok           False                  False
  ASML           72.73               11            2.41             26.17       1540.92                44.05         0.523            pass              0.134             25.0                           0.326               -9.54             -0.552            downtrend_blocked_slope           False                  False
  AVGO           75.00               28            0.99              2.31        331.14                44.04         0.522            pass              0.322             49.8                           0.367               -2.65             -0.029                                 ok           False                  False
  LRCX           67.50               40            0.62              1.01        230.29                62.98         0.504            pass              0.489             79.6                           0.540              -12.09             -0.545            downtrend_blocked_slope           False                  False
  NVDA           75.00               20            1.15              1.67        205.97                32.59         0.500 below_threshold              0.292             58.5                           0.470               -7.96             -0.707 downtrend_blocked_slope_and_streak           False                  False
  MCHP           92.00               25            1.47              0.80         77.56                45.40         0.498 below_threshold              0.470              0.0                           0.217               -0.51              0.258                                 ok           False                  False
  INSM           78.38               37            1.16              0.85        104.08                60.46         0.494 below_threshold              0.258              9.7                           0.167                9.77              1.683                                 ok           False                  False
   TXN           91.18               34            0.40              0.88        312.11                35.19         0.493 below_threshold              0.675             55.8                           0.346                9.87              1.063                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                            detail
2026-11-04T10:25:06.359695-05:00 early_entry_1025 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:20:05.681556-05:00 early_entry_1020 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:15:05.290161-05:00 early_entry_1015 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:10:06.483796-05:00 early_entry_1010 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:05:05.606953-05:00 early_entry_1005 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:00:05.152440-05:00 early_entry_1000 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T09:20:05.283761-05:00     data_refresh       data_refresh                                                                                                                                                         {'saved': 91, 'empty': 2}
2026-11-03T16:10:06.665587-05:00      manage_1600               exit {"asset_type": "option", "contract_symbol": "MDLZ261218C00067500", "fill_price": 1.305, "pnl": -6815.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MDLZ"}
2026-11-03T15:10:05.032509-05:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-11-03T15:05:04.979432-05:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104102506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104102506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104102506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104102506)

</details>
