# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 10:15:03 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMAT           93.75               16            2.59             11.81        645.85               105.28         0.597          pass              0.692             75.2                           0.381                6.94              1.197                                 ok            True                  False
  KLAC           90.00               10            4.24              7.90        262.81               114.88         0.596          pass              0.342              5.4                           0.104                6.78              0.968                                 ok            True                  False
  LRCX           94.12               17            3.13              8.56        387.59               101.74         0.589          pass              0.640             52.8                           0.278                1.30              0.428                                 ok            True                  False
   WBD           95.00               20            0.52              0.10         26.77                21.87         0.583          pass              0.689             54.7                           0.324                1.64              0.129                                 ok            True                  False
  PCAR           87.10               31            0.70              0.60        120.98                34.47         0.501          pass              0.477             32.5                           0.257                2.60              0.257                                 ok            True                  False
  DRAM           91.30               23            1.54              0.71         65.56               129.95         0.831          pass              0.696             75.0                           0.623               -7.30             -1.047            downtrend_blocked_slope           False                  False
  MRVL           96.55               29            0.90              1.72        271.31               126.33         0.782          pass              0.838             77.7                           0.573               -6.89             -0.938            downtrend_blocked_slope           False                  False
   WDC           90.00               30            0.89              3.74        596.77               119.34         0.691          pass              0.713             81.2                           0.476              -16.72             -2.146            downtrend_blocked_slope           False                  False
   STX           96.00               25            1.31              8.40        911.59                90.35         0.636          pass              0.761             65.9                           0.427              -15.22             -1.873            downtrend_blocked_slope           False                  False
   KDP          100.00               29            0.12              0.03         33.36                28.32         0.561          pass              0.848             88.5                           0.431                8.66              1.103                                 ok           False                  False
  CSCO           95.45               22            1.35              1.11        116.54                39.12         0.532          pass              0.624             30.4                           0.338               -1.62             -0.344 downtrend_blocked_slope_and_streak           False                  False
  TEAM           86.36               44            0.06              0.03         83.16                59.89         0.509          pass              0.709             96.1                           0.412               -1.50             -0.203                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                             detail
2026-07-02T10:15:03.634987-04:00 early_entry_1015 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:10:01.761817-04:00 early_entry_1010 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:05:03.731270-04:00 early_entry_1005 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:00:03.571046-04:00 early_entry_1000 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T09:20:05.802169-04:00     data_refresh       data_refresh                                                                                                                                                                      {'saved': 93}
2026-07-01T15:20:08.894033-04:00      manage_1530               exit {"asset_type": "option", "contract_symbol": "GILD260821C00130000", "fill_price": 4.1175, "pnl": -1464.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GILD"}
2026-07-01T15:10:11.143271-04:00       entry_1500       slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-07-01T15:05:07.919397-04:00       entry_1500       slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-07-01T15:00:09.367331-04:00       entry_1500       slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-07-01T14:55:05.861766-04:00       entry_1500       slot_skipped                                                                                                                                                    {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702101503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702101503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702101503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702101503)

</details>
