# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 10:10:01 EDT`
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
  AMAT           93.33               15            2.64             12.03        645.76               105.28         0.600          pass              0.673             74.7                           0.394                6.88              1.194                      ok            True                  False
  LRCX           94.44               18            2.93              8.02        387.82               101.74         0.597          pass              0.666             55.8                           0.290                1.50              0.437                      ok            True                  False
   WBD           95.00               20            0.54              0.10         26.77                21.87         0.582          pass              0.684             53.0                           0.336                1.62              0.129                      ok            True                  False
   APP           85.71               42            0.72              2.85        563.39                73.83         0.507          pass              0.626             74.2                           0.393               16.90              1.776                      ok            True                  False
  PCAR           87.10               31            0.69              0.59        120.99                34.47         0.502          pass              0.479             33.3                           0.293                2.61              0.258                      ok            True                  False
  SOXL           90.62               32            0.09              0.13        217.49               253.51         0.961          pass              0.822             98.8                           0.848               -7.06             -1.586 downtrend_blocked_slope           False                  False
  DRAM           91.67               24            1.46              0.67         65.57               129.95         0.831          pass              0.717             76.4                           0.736               -7.22             -1.043 downtrend_blocked_slope           False                  False
  MRVL           96.55               29            0.93              1.78        271.29               126.33         0.780          pass              0.836             77.0                           0.700               -6.92             -0.939 downtrend_blocked_slope           False                  False
   WDC           90.62               32            0.71              2.98        597.09               119.34         0.691          pass              0.754             85.0                           0.537              -16.57             -2.137 downtrend_blocked_slope           False                  False
   STX           96.55               29            0.95              6.09        912.58                90.35         0.635          pass              0.816             75.3                           0.635              -14.91             -1.856 downtrend_blocked_slope           False                  False
  ASML           94.44               36            0.15              1.95       1842.20                76.04         0.634          pass              0.913             97.0                           0.635               -1.48             -0.031                      ok           False                  False
  KLAC           88.89                9            4.36              8.13        262.71               114.88         0.593          pass              0.304              2.4                           0.154                6.64              0.962                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                 detail
2026-07-02T10:10:01.761817-04:00 early_entry_1010      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:05:03.731270-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:00:03.571046-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T09:20:05.802169-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                          {'saved': 93}
2026-07-01T15:20:08.894033-04:00      manage_1530                    exit                                                                                     {"asset_type": "option", "contract_symbol": "GILD260821C00130000", "fill_price": 4.1175, "pnl": -1464.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GILD"}
2026-07-01T15:10:11.143271-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T15:05:07.919397-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T15:00:09.367331-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:55:05.861766-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:50:09.429141-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.275, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 12.0, "option_spread_pct": 31.25, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "EXC", "timing_score": 0.587}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702101001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702101001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702101001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702101001)

</details>
