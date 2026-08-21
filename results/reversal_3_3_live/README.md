# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-21 15:20:08 EDT`
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
  TEAM           80.65               31            1.73              2.12        174.00               116.76         0.737          pass              0.399             56.2                           0.685               15.30              1.542                                 ok            True                  False
    MU           83.33               36            0.69              4.69        972.32               100.72         0.710          pass              0.508             58.3                           0.491               10.26              1.216                                 ok            True                  False
   WDC           83.87               31            0.62              2.04        468.17               103.26         0.707          pass              0.554             80.2                           0.644                7.33              0.962                                 ok            True                  False
   TRI           91.43               35            0.54              0.40        105.71                73.29         0.636          pass              0.637             34.1                           0.319                4.09              0.186                                 ok            True                  False
   MAR           96.77               31            0.60              1.50        355.96                36.23         0.547          pass              0.715             40.2                           0.248                0.36              0.213                                 ok            True                  False
  AAPL           84.85               33            0.51              1.11        310.83                35.92         0.521          pass              0.335              0.0                             NaN               -1.07              0.139                                 ok            True                  False
  SOXL           83.33               36            1.02              0.88        121.83               166.13         0.806          pass              0.575             77.3                           0.661              -13.75             -1.298            downtrend_blocked_slope           False                  False
  AMAT           91.43               35            0.67              2.32        495.21                84.07         0.666          pass              0.762             74.6                           0.675               -8.48             -0.856            downtrend_blocked_slope           False                  False
   APP           68.42               38            1.51              3.26        307.37                90.16         0.611          pass              0.405             52.3                           0.576              -12.31             -0.986            downtrend_blocked_slope           False                  False
  KLAC           81.82               33            0.81              1.05        185.41                69.68         0.597          pass              0.441             60.0                           0.491               -6.84             -0.767 downtrend_blocked_slope_and_streak           False                  False
  AMZN           76.19               42            0.32              0.58        259.86                59.61         0.583          pass              0.477             72.8                           0.653               -5.54             -0.635 downtrend_blocked_slope_and_streak           False                  False
   KHC           85.29               34            0.06              0.01         25.57                38.96         0.562          pass              0.620             87.5                           0.472                0.93              0.244                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260821152008)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260821152008)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260821152008)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260821152008)

</details>
