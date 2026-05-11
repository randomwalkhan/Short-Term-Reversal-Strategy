# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 09:59:30 EDT`
Last processed slot: `manage_1000`

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
  NXPI           80.56               36            0.73              1.50        294.11                87.07         0.698          pass              0.386             42.7                           0.309               23.53              1.917                                 ok            True                  False
  TEAM           87.88               33            2.49              1.60         90.92               114.36         0.652          pass              0.556             42.6                           0.293               29.04              3.393                                 ok            True                  False
  GOOG           85.19               27            1.05              2.92        395.80                37.66         0.550          pass              0.457             50.0                           0.635               12.73              1.447                                 ok            True                  False
    ZS           83.33               36            1.06              1.13        151.65                58.64         0.540          pass              0.389             24.4                           0.307               12.24              1.393                                 ok            True                  False
   ADP           92.00               25            0.93              1.39        212.40                34.95         0.527          pass              0.632             53.0                           0.320                6.99              0.482                                 ok            True                  False
  FAST           94.74               19            1.19              0.37         44.01                33.60         0.524          pass              0.590             28.1                           0.273               -3.10             -0.165                                 ok            True                  False
   ADI           83.33               30            0.78              2.27        415.55                36.03         0.521          pass              0.381             35.6                           0.276                5.27              0.743                                 ok            True                  False
  ORLY           85.71               28            1.07              0.70         92.66                35.12         0.510          pass              0.471             49.2                           0.495               -0.01              0.037                                 ok            True                  False
  TMUS           86.11               36            0.63              0.85        193.27                36.59         0.508          pass              0.553             55.3                           0.494                5.29              0.281                                 ok            True                  False
  WDAY           80.77               26            2.35              2.10        126.93                62.51         0.503          pass              0.178              0.0                           0.217                5.94              0.656                                 ok            True                  False
  CHTR           80.00               15            2.62              2.84        153.64               119.48         0.784          pass              0.200             29.5                           0.280              -13.64             -1.217            downtrend_blocked_slope           False                  False
 CMCSA           90.62               32            0.24              0.04         25.38                62.19         0.668          pass              0.723             75.5                           0.447               -7.91             -0.801 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511095930)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511095930)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511095930)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511095930)

</details>
