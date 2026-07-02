# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 10:00:03 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  KLAC           92.86               14            3.52              6.56        263.38               114.88         0.628            pass              0.468             12.0                           0.145                7.58              1.001                                 ok            True                  False
  LRCX           94.74               19            2.55              6.98        388.27               101.74         0.618            pass              0.699             61.5                           0.306                1.90              0.455                                 ok            True                  False
  AMAT           95.45               22            1.82              8.27        647.36               105.28         0.614            pass              0.789             82.6                           0.407                7.79              1.233                                 ok            True                  False
  PCAR           84.62               26            0.87              0.73        120.93                34.47         0.522            pass              0.328             15.3                           0.227                2.43              0.250                                 ok            True                  False
   APP           85.71               42            0.71              2.82        563.40                73.83         0.507            pass              0.626             74.4                           0.434               16.91              1.776                                 ok            True                  False
  DRAM           92.86               28            0.83              0.38         65.70               129.95         0.842            pass              0.807             86.6                           0.843               -6.63             -1.014            downtrend_blocked_slope           False                  False
   STX           97.22               36            0.12              0.77        914.86                90.35         0.648            pass              0.929             96.9                           0.851              -14.19             -1.818            downtrend_blocked_slope           False                  False
   WBD           96.00               25            0.45              0.08         26.77                21.87         0.554            pass              0.739             61.1                           0.377                1.71              0.133                                 ok           False                  False
  CSCO           96.15               26            1.30              1.06        116.55                39.12         0.508            pass              0.657             33.0                           0.313               -1.57             -0.341 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           50.00                8            1.35              0.22         23.63                36.53         0.486 below_threshold              0.245             65.6                           0.403                4.58              0.848                                 ok           False                  False
  SNPS           88.57               35            0.68              2.17        453.60                30.90         0.444 below_threshold              0.587             49.1                           0.520               -2.23             -0.297 downtrend_blocked_slope_and_streak           False                  False
  FTNT           97.56               41            0.70              0.78        158.65                36.03         0.430 below_threshold              0.811             56.1                           0.506                9.53              1.031                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                 detail
2026-07-02T10:00:03.571046-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T09:20:05.802169-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                          {'saved': 93}
2026-07-01T15:20:08.894033-04:00      manage_1530                    exit                                                                                     {"asset_type": "option", "contract_symbol": "GILD260821C00130000", "fill_price": 4.1175, "pnl": -1464.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GILD"}
2026-07-01T15:10:11.143271-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T15:05:07.919397-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T15:00:09.367331-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:55:05.861766-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:50:09.429141-04:00       entry_1500 entry_candidate_skipped                           {"early_entry_score": 0.643, "option_liquidity_status": "wide_spread", "option_open_interest": 1263.0, "option_spread_pct": 16.22, "option_volume": 24.0, "reason": "no_trade_low_option_liquidity", "ticker": "XEL", "timing_score": 0.571}
2026-07-01T14:50:09.429141-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.275, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 12.0, "option_spread_pct": 31.25, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "EXC", "timing_score": 0.587}
2026-07-01T14:50:09.429141-04:00       entry_1500          timing_overlay                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-01", "training_samples": 5334, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702100003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702100003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702100003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702100003)

</details>
