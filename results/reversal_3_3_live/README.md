# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-01 15:30:11 EDT`
Last processed slot: `manage_1530`

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

## Today's Closed Trades (2026-07-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  GILD     option         option GILD260821C00130000     32          2026-06-29         2026-07-01        4.575      4.1175 -1464.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   XEL          100.00               10            1.18              0.67         80.01                19.51         0.605          pass              0.470              3.1                           0.093                0.47              0.402                                 ok            True                  False
   EXC           83.33               12            1.03              0.34         46.48                18.60         0.584          pass              0.199             12.7                           0.250               -0.97              0.178                                 ok            True                  False
  MRVL          100.00               10            6.48             13.52        292.10               157.45         0.519          pass              0.523             23.6                           0.537               -0.03             -0.456                                 ok            True                  False
  AMGN           93.10               29            0.65              1.66        361.41                26.93         0.517          pass              0.660             44.1                           0.361                3.43              0.629                                 ok            True                  False
  GILD           89.29               28            0.58              0.51        126.12                28.09         0.510          pass              0.538             39.9                           0.382               -1.27              0.058                                 ok            True                  False
  FAST           91.30               23            1.01              0.34         47.88                23.97         0.504          pass              0.438              0.0                           0.197                3.25              0.544                                 ok            True                  False
  AVGO           78.26               23            1.52              4.02        376.02                74.76         0.675          pass              0.277             40.8                           0.621               -1.09             -0.587                                 ok           False                  False
  MPWR           86.21               29            1.56             15.08       1375.90                91.02         0.659          pass              0.535             58.8                           0.596               -9.20             -1.363            downtrend_blocked_slope           False                  False
  MCHP           89.66               29            0.99              0.63         90.93                74.43         0.648          pass              0.636             62.3                           0.718               -5.57             -0.959            downtrend_blocked_slope           False                  False
   ADI           89.66               29            0.75              2.08        396.28                64.06         0.628          pass              0.653             68.8                           0.615               -5.24             -0.914            downtrend_blocked_slope           False                  False
  QCOM           89.19               37            0.11              0.15        184.73                83.64         0.626          pass              0.773             95.1                           0.565              -13.78             -1.967 downtrend_blocked_slope_and_streak           False                  False
   WDC          100.00                9            5.54             24.77        628.10               116.88         0.570          pass              0.556             33.1                           0.727              -11.41             -1.714            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et        slot              event_type                                                                                                                                                                                                                                                                 detail
2026-07-01T15:20:08.894033-04:00 manage_1530                    exit                                                                                     {"asset_type": "option", "contract_symbol": "GILD260821C00130000", "fill_price": 4.1175, "pnl": -1464.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "GILD"}
2026-07-01T15:10:11.143271-04:00  entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T15:05:07.919397-04:00  entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T15:00:09.367331-04:00  entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:55:05.861766-04:00  entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-07-01T14:50:09.429141-04:00  entry_1500           entry_skipped                                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-07-01T14:50:09.429141-04:00  entry_1500 entry_candidate_skipped                    {"early_entry_score": 0.2, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 720.0, "option_spread_pct": 17.39, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "AEP", "timing_score": 0.543}
2026-07-01T14:50:09.429141-04:00  entry_1500 entry_candidate_skipped                           {"early_entry_score": 0.643, "option_liquidity_status": "wide_spread", "option_open_interest": 1263.0, "option_spread_pct": 16.22, "option_volume": 24.0, "reason": "no_trade_low_option_liquidity", "ticker": "XEL", "timing_score": 0.571}
2026-07-01T14:50:09.429141-04:00  entry_1500 entry_candidate_skipped {"early_entry_score": 0.275, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 12.0, "option_spread_pct": 31.25, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "EXC", "timing_score": 0.587}
2026-07-01T14:50:09.429141-04:00  entry_1500          timing_overlay                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-01", "training_samples": 5334, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260701153011)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260701153011)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260701153011)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260701153011)

</details>
