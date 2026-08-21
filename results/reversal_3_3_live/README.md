# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-21 12:18:01 EDT`
Last processed slot: `manage_1230`

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

- Cash: `$57,703.00`
- Equity: `$57,703.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-21)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  ABNB     option         option ABNB261016C00180000     22          2026-08-20         2026-08-21        12.05      14.125 4565.0   17.219917 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           80.65               31            1.84              2.25        173.95               116.76         0.732          pass              0.391             53.5                           0.523               15.18              1.537                                 ok            True                  False
   WDC           83.87               31            0.87              2.86        467.83               103.26         0.694          pass              0.529             72.3                           0.432                7.06              0.951                                 ok            True                  False
    MU           82.86               35            1.13              7.68        971.04               100.72         0.692          pass              0.407             31.7                           0.247                9.78              1.196                                 ok            True                  False
  SOXL           81.82               33            2.75              2.35        121.20               166.13         0.740          pass              0.393             38.9                           0.306              -15.26             -1.378            downtrend_blocked_slope           False                  False
   STX           89.47               38            0.02              0.12        850.19                87.74         0.647          pass              0.801             98.9                           0.629                4.59              0.582                                 ok           False                  False
  AMAT           89.29               28            1.80              6.25        493.53                84.07         0.638          pass              0.527             31.7                           0.307               -9.52             -0.908            downtrend_blocked_slope           False                  False
   APP           67.57               37            1.69              3.65        307.21                90.16         0.605          pass              0.380             46.7                           0.502              -12.47             -0.995            downtrend_blocked_slope           False                  False
  AMZN           75.00               40            0.43              0.78        259.78                59.61         0.587          pass              0.450             63.9                           0.367               -5.64             -0.639 downtrend_blocked_slope_and_streak           False                  False
  KLAC           80.00               30            1.33              1.73        185.12                69.68         0.580          pass              0.294             34.1                           0.281               -7.33             -0.791 downtrend_blocked_slope_and_streak           False                  False
  MCHP           85.71               42            0.67              0.36         75.66                70.29         0.579          pass              0.475             21.5                           0.206              -11.09             -0.928 downtrend_blocked_slope_and_streak           False                  False
  MPWR           84.21               38            0.51              4.68       1308.59                59.09         0.544          pass              0.501             49.3                           0.340               -6.97             -0.811            downtrend_blocked_slope           False                  False
   MAR           94.59               37            0.19              0.46        356.40                36.23         0.534          pass              0.867             81.6                           0.451                0.78              0.232                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                 detail
2026-08-21T12:00:13.505037-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:55:10.146119-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:50:07.256034-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T11:50:07.256034-04:00      manage_1200                    exit                                                                               {"asset_type": "option", "contract_symbol": "ABNB261016C00180000", "fill_price": 14.125, "pnl": 4565.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 17.22, "ticker": "ABNB"}
2026-08-21T11:15:05.200635-04:00 early_entry_1115      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T10:36:48.615754-04:00 early_entry_1035      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T10:18:45.233650-04:00 early_entry_1015      early_entry_shadow                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-21T00:00:05.323227-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                          {'saved': 93}
2026-08-20T14:55:07.817083-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.536, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 8.0, "option_spread_pct": 24.91, "option_volume": 3.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.643}
2026-08-20T14:55:07.817083-04:00       entry_1500          timing_overlay                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-20", "training_samples": 5707, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260821121801)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260821121801)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260821121801)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260821121801)

</details>
