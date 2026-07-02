# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 10:05:03 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  KLAC           88.24               17            3.29              6.13        263.56               114.88         0.619          pass              0.382             17.8                           0.233                7.84              1.012                                 ok            True                  False
  AMAT           95.24               21            1.91              8.72        647.17               105.28         0.613          pass              0.780             81.6                           0.494                7.68              1.228                                 ok            True                  False
  LRCX           95.45               22            2.38              6.51        388.47               101.74         0.610          pass              0.733             64.1                           0.322                2.08              0.463                                 ok            True                  False
  PCAR           82.61               23            1.01              0.86        120.87                34.47         0.531          pass              0.218              2.8                           0.131                2.28              0.243                                 ok            True                  False
   APP           85.71               42            0.81              3.19        563.24                73.83         0.500          pass              0.616             71.1                           0.401               16.80              1.772                                 ok            True                  False
  DRAM           92.59               27            0.88              0.41         65.69               129.95         0.844          pass              0.791             85.7                           0.866               -6.68             -1.016            downtrend_blocked_slope           False                  False
  MRVL           96.55               29            0.65              1.23        271.52               126.33         0.795          pass              0.858             84.1                           0.818               -6.65             -0.926            downtrend_blocked_slope           False                  False
   WDC           91.89               37            0.17              0.73        598.06               119.34         0.697          pass              0.856             96.3                           0.775              -16.12             -2.113            downtrend_blocked_slope           False                  False
   STX           97.22               36            0.34              2.15        914.27                90.35         0.633          pass              0.910             91.3                           0.844              -14.38             -1.828            downtrend_blocked_slope           False                  False
   WBD           96.43               28            0.41              0.08         26.78                21.87         0.536          pass              0.767             64.4                           0.393                1.75              0.135                                 ok           False                  False
  CSCO           95.45               22            1.35              1.11        116.54                39.12         0.532          pass              0.624             30.4                           0.370               -1.62             -0.344 downtrend_blocked_slope_and_streak           False                  False
  TEAM           86.36               44            0.05              0.03         83.16                59.89         0.510          pass              0.711             96.9                           0.481               -1.49             -0.203                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                 detail
2026-07-02T10:05:03.731270-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T10:00:03.571046-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T09:20:05.802169-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                          {'saved': 93}
2026-07-01T15:20:08.894033-04:00      manage_1530                    exit                                                                                     {"asset_type": "option", "contract_symbol": "GILD260821C00130000", "fill_price": 4.1175, "pnl": -1464.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GILD"}
2026-07-01T15:10:11.143271-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T15:05:07.919397-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T15:00:09.367331-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:55:05.861766-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:50:09.429141-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.275, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 12.0, "option_spread_pct": 31.25, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "EXC", "timing_score": 0.587}
2026-07-01T14:50:09.429141-04:00       entry_1500          timing_overlay                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-01", "training_samples": 5334, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702100503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702100503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702100503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702100503)

</details>
