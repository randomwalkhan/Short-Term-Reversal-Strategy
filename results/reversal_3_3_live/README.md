# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 10:30:06 EDT`
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
  INTC           93.94               33            1.09              0.97        126.60               102.61         0.646          pass              0.814             74.7                           0.393                3.74             -0.084                      ok            True                  False
   WBD           94.44               18            0.60              0.11         26.76                21.87         0.591          pass              0.642             48.2                           0.304                1.56              0.126                      ok            True                  False
  ASML           92.86               28            1.62             20.90       1834.08                76.04         0.581          pass              0.724             67.7                           0.378               -2.93             -0.098                      ok            True                  False
  PCAR           84.00               25            0.96              0.82        120.89                34.47         0.521          pass              0.286              9.0                           0.235                2.33              0.245                      ok            True                  False
  SOXL           88.24               17            6.00              9.13        213.64               253.51         0.851          pass              0.400             16.1                           0.150              -12.55             -1.863 downtrend_blocked_slope           False                  False
    MU           89.66               29            1.68             12.15       1027.07               134.25         0.770          pass              0.646             61.7                           0.318               -2.71             -0.373 downtrend_blocked_slope           False                  False
  DRAM           92.86               14            4.30              1.98         65.01               129.95         0.736          pass              0.534             30.2                           0.213               -9.90             -1.176 downtrend_blocked_slope           False                  False
  AVGO           86.84               38            0.00              0.01        369.34                71.90         0.696          pass              0.738             99.7                           0.525               -5.85             -0.841 downtrend_blocked_slope           False                  False
  MCHP           93.10               29            1.06              0.66         88.41                71.75         0.639          pass              0.630             29.9                           0.275               -6.76             -1.200 downtrend_blocked_slope           False                  False
  MRVL          100.00               19            4.24              8.07        268.59               126.33         0.632          pass              0.533              3.1                           0.181              -10.02             -1.093 downtrend_blocked_slope           False                  False
   ADI           91.43               35            0.35              0.97        388.57                61.24         0.610          pass              0.758             75.3                           0.354               -6.48             -1.150 downtrend_blocked_slope           False                  False
   WDC           92.31               13            4.00             16.76        591.19               119.34         0.587          pass              0.454             15.6                           0.133              -19.34             -2.291 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                             detail
2026-07-02T10:30:06.141099-04:00 early_entry_1030 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:25:06.771097-04:00 early_entry_1025 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:20:04.785381-04:00 early_entry_1020 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:15:03.634987-04:00 early_entry_1015 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:10:01.761817-04:00 early_entry_1010 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:05:03.731270-04:00 early_entry_1005 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:00:03.571046-04:00 early_entry_1000 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T09:20:05.802169-04:00     data_refresh       data_refresh                                                                                                                                                                      {'saved': 93}
2026-07-01T15:20:08.894033-04:00      manage_1530               exit {"asset_type": "option", "contract_symbol": "GILD260821C00130000", "fill_price": 4.1175, "pnl": -1464.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GILD"}
2026-07-01T15:10:11.143271-04:00       entry_1500       slot_skipped                                                                                                                                                    {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702103006)

</details>
