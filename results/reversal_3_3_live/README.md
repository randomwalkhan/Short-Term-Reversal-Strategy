# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 09:40:49 EDT`
Last processed slot: `manage_0930`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$32,833.50`
- Equity: `$32,833.50`
- Realized PnL: `$22,833.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-11)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  GOOG           85.71               28            0.98              2.72        395.89                37.66         0.549          pass              0.488             53.5                           0.539               12.81              1.450                                 ok            True                  False
  MSTR           91.43               35            1.78              2.34        186.59                70.10         0.538          pass              0.635             36.7                           0.322                8.89              1.458                                 ok            True                  False
  MRVL          100.00               27            1.28              1.52        169.48                55.66         0.537          pass              0.783             72.0                           0.771                6.16              0.808                                 ok            True                  False
  FAST           93.33               15            1.40              0.43         43.98                33.60         0.536          pass              0.461              6.1                           0.288               -3.31             -0.175                                 ok            True                  False
   ADP           92.31               26            0.85              1.26        212.46                34.95         0.527          pass              0.660             57.4                           0.404                7.08              0.486                                 ok            True                  False
  ASML           86.67               15            2.87             31.98       1578.31                48.89         0.525          pass              0.287              7.8                           0.249                7.95              1.224                                 ok            True                  False
  TMUS           85.29               34            0.67              0.90        193.24                36.59         0.521          pass              0.472             39.4                           0.258                5.25              0.279                                 ok            True                  False
   WMT           87.50               24            0.83              0.76        130.11                19.38         0.503          pass              0.432             29.4                           0.253                1.57              0.173                                 ok            True                  False
  CHTR           81.25               16            2.49              2.70        153.70               119.48         0.796          pass              0.155              0.5                           0.198              -13.52             -1.210            downtrend_blocked_slope           False                  False
 CMCSA           90.32               31            0.26              0.05         25.38                62.19         0.679          pass              0.523             13.3                           0.222               -7.92             -0.802 downtrend_blocked_slope_and_streak           False                  False
  SHOP           85.71               21            2.79              2.16        109.58                82.28         0.614          pass              0.363             25.4                           0.209              -13.53             -1.656            downtrend_blocked_slope           False                  False
  GEHC           74.36               39            0.44              0.20         63.39                57.03         0.580          pass              0.414             54.1                           0.319              -10.34             -0.663                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                                 detail
2026-05-11T09:18:42.943466-04:00 data_refresh data_refresh                                                                                                                                                                          {'saved': 92}
2026-05-08T16:05:06.142170-04:00  manage_1600         exit {"asset_type": "option", "contract_symbol": "TEAM260618C00090000", "fill_price": 9.25, "pnl": 2850.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 19.35, "ticker": "TEAM"}
2026-05-08T16:00:06.094263-04:00  manage_1600 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:55:02.084715-04:00  manage_1600 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:40:02.063692-04:00  manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:35:05.923584-04:00  manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:30:06.082521-04:00  manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:25:06.105856-04:00  manage_1530 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:10:02.102478-04:00   entry_1500 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-08T15:05:03.959571-04:00   entry_1500 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511094049)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511094049)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511094049)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511094049)

</details>
