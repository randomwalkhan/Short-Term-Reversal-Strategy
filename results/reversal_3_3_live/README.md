# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 10:20:04 EDT`
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

- Cash: `$27,896.50`
- Equity: `$27,896.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   WBD           95.00               20            0.52              0.10         26.77                21.87         0.583          pass              0.689             54.7                           0.338                1.64              0.129                      ok            True                  False
  LRCX          100.00               12            4.34             11.90        386.16               101.74         0.542          pass              0.571             34.4                           0.205                0.02              0.370                      ok            True                  False
  AMAT           91.67               12            3.77             17.20        643.54               105.28         0.535          pass              0.569             63.8                           0.335                5.64              1.141                      ok            True                  False
  PCAR           87.10               31            0.63              0.54        121.01                34.47         0.506          pass              0.498             39.3                           0.279                2.67              0.260                      ok            True                  False
  SOXL           89.29               28            2.04              3.11        216.22               253.51         0.936          pass              0.676             71.4                           0.425               -8.87             -1.676 downtrend_blocked_slope           False                  False
    MU           91.43               35            0.11              0.79       1031.94               134.25         0.822          pass              0.846             97.5                           0.521               -1.15             -0.301                      ok           False                  False
  DRAM           90.00               20            2.68              1.24         65.33               129.95         0.790          pass              0.582             56.5                           0.394               -8.37             -1.099 downtrend_blocked_slope           False                  False
  MRVL           96.00               25            2.08              3.96        270.35               126.33         0.736          pass              0.720             48.8                           0.331               -8.00             -0.992 downtrend_blocked_slope           False                  False
   WDC           86.36               22            2.40             10.04        594.07               119.34         0.635          pass              0.462             49.5                           0.322              -17.99             -2.215 downtrend_blocked_slope           False                  False
  ASML           94.12               34            0.37              4.71       1841.02                76.04         0.632          pass              0.878             92.7                           0.533               -1.69             -0.040                      ok           False                  False
   STX           92.86               14            2.77             17.75        907.58                90.35         0.603          pass              0.514             27.9                           0.242              -16.47             -1.940 downtrend_blocked_slope           False                  False
   KDP          100.00               31            0.07              0.02         33.36                28.32         0.550          pass              0.874             93.1                           0.415                8.72              1.105                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                             detail
2026-07-02T10:20:04.785381-04:00 early_entry_1020 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:15:03.634987-04:00 early_entry_1015 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:10:01.761817-04:00 early_entry_1010 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:05:03.731270-04:00 early_entry_1005 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:00:03.571046-04:00 early_entry_1000 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T09:20:05.802169-04:00     data_refresh       data_refresh                                                                                                                                                                      {'saved': 93}
2026-07-01T15:20:08.894033-04:00      manage_1530               exit {"asset_type": "option", "contract_symbol": "GILD260821C00130000", "fill_price": 4.1175, "pnl": -1464.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GILD"}
2026-07-01T15:10:11.143271-04:00       entry_1500       slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-07-01T15:05:07.919397-04:00       entry_1500       slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-07-01T15:00:09.367331-04:00       entry_1500       slot_skipped                                                                                                                                                    {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702102004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702102004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702102004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702102004)

</details>
