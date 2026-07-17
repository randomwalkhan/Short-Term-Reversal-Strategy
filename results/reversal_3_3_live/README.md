# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 10:05:01 EDT`
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

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   TXN           88.89               18            2.43              4.96        289.09                64.46         0.595          pass              0.472             40.8                           0.687               -3.05             -0.223                      ok            True                  False
  AAPL           95.65               23            0.86              2.00        332.40                36.90         0.581          pass              0.626             27.0                           0.314                7.05              0.697                      ok            True                  False
  MPWR           81.25               32            1.27             11.63       1300.67                74.72         0.578          pass              0.471             77.7                           0.833                0.07              0.084                      ok            True                  False
   ADI           86.36               22            1.97              5.25        378.28                54.65         0.568          pass              0.443             45.5                           0.712               -1.10             -0.027                      ok            True                  False
  ASML           95.24               21            2.85             35.55       1769.64                64.12         0.534          pass              0.640             37.7                           0.689               -1.99             -0.101                      ok            True                  False
  NXPI           86.96               23            1.92              3.64        269.10                54.99         0.533          pass              0.497             57.2                           0.821               -2.89             -0.244                      ok            True                  False
  BKNG           85.71               21            1.81              2.34        183.61                41.98         0.514          pass              0.324             15.6                           0.213               -1.78              0.009                      ok            True                  False
  UPRO           94.44               18            2.10              2.11        142.71                37.18         0.500          pass              0.634             48.6                           0.792               -0.12              0.077                      ok            True                  False
  DRAM           83.87               31            0.14              0.05         52.32               117.20         0.790          pass              0.616             98.0                           0.904              -13.80             -1.726 downtrend_blocked_slope           False                  False
    MU           81.82               33            0.19              1.11        852.72               110.15         0.748          pass              0.567             96.8                           0.885              -12.69             -1.226 downtrend_blocked_slope           False                  False
  PYPL           77.78               18            1.37              0.55         56.50                63.95         0.660          pass              0.262             47.4                           0.278               23.05              2.470                      ok           False                  False
  KLAC           80.00               20            3.17              4.87        217.28               106.93         0.642          pass              0.290             53.0                           0.770               -9.82             -0.550 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                 detail
2026-07-17T10:05:01.944429-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:00:04.999417-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T09:20:02.076532-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                          {'saved': 93}
2026-07-16T15:10:05.118265-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T15:05:04.145038-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T15:00:06.149748-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T14:55:06.750715-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-16T14:50:02.142710-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.428, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.61, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.572}
2026-07-16T14:50:02.142710-04:00       entry_1500 entry_candidate_skipped                            {"early_entry_score": 0.287, "option_liquidity_status": "low_volume", "option_open_interest": 859.0, "option_spread_pct": 12.05, "option_volume": 16.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.591}
2026-07-16T14:50:02.142710-04:00       entry_1500 entry_candidate_skipped              {"early_entry_score": 0.267, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 84.0, "option_spread_pct": 8.5, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.577}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717100501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717100501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717100501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717100501)

</details>
