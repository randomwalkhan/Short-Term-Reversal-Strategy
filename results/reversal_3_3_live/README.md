# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 10:35:03 EDT`
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
  INTC           92.00               25            2.09              1.85        126.23               102.61         0.628          pass              0.638             51.8                           0.271                2.70             -0.130                      ok            True                  False
   WBD           93.33               15            0.63              0.12         26.76                21.87         0.608          pass              0.585             44.9                           0.289                1.52              0.124                      ok            True                  False
  ASML           92.59               27            1.70             21.95       1833.63                76.04         0.582          pass              0.705             66.0                           0.338               -3.01             -0.102                      ok            True                  False
  PCAR           84.62               26            0.92              0.78        120.91                34.47         0.518          pass              0.321             13.1                           0.163                2.38              0.247                      ok            True                  False
  SOXL           86.67               15            7.73             11.77        212.50               253.51         0.769          pass              0.295              2.4                           0.166              -14.17             -1.948 downtrend_blocked_slope           False                  False
    MU           88.00               25            2.24             16.18       1025.35               134.25         0.759          pass              0.536             49.0                           0.243               -3.26             -0.399 downtrend_blocked_slope           False                  False
  DRAM           90.91               11            5.14              2.37         64.84               129.95         0.701          pass              0.418             16.6                           0.128              -10.69             -1.216 downtrend_blocked_slope           False                  False
  MPWR           88.24               34            0.47              4.34       1329.87                89.16         0.678          pass              0.685             79.2                           0.340               -8.33             -1.488 downtrend_blocked_slope           False                  False
  MCHP           91.30               23            1.80              1.12         88.21                71.75         0.621          pass              0.455              1.5                           0.101               -7.46             -1.234 downtrend_blocked_slope           False                  False
  NXPI           91.18               34            0.29              0.56        278.94                63.41         0.613          pass              0.761             80.6                           0.359               -6.33             -1.260 downtrend_blocked_slope           False                  False
  MRVL          100.00               15            4.78              9.10        268.15               126.33         0.611          pass              0.517              7.4                           0.174              -10.53             -1.119 downtrend_blocked_slope           False                  False
   ADI           91.43               35            0.37              0.99        388.55                61.24         0.610          pass              0.756             74.6                           0.332               -6.49             -1.150 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                             detail
2026-07-02T10:35:03.761213-04:00 early_entry_1035 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:30:06.141099-04:00 early_entry_1030 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:25:06.771097-04:00 early_entry_1025 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:20:04.785381-04:00 early_entry_1020 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:15:03.634987-04:00 early_entry_1015 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:10:01.761817-04:00 early_entry_1010 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:05:03.731270-04:00 early_entry_1005 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:00:03.571046-04:00 early_entry_1000 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T09:20:05.802169-04:00     data_refresh       data_refresh                                                                                                                                                                      {'saved': 93}
2026-07-01T15:20:08.894033-04:00      manage_1530               exit {"asset_type": "option", "contract_symbol": "GILD260821C00130000", "fill_price": 4.1175, "pnl": -1464.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GILD"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702103503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702103503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702103503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702103503)

</details>
