# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 15:05:03 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$20,193.50`
- Equity: `$33,333.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-270.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 13140.0         44.7           43.8      510.62        506.57          -270.0                  -2.01         97.14               35               0.5         52.16           55.29                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           87.50               16            4.59              2.73         83.83               115.69         0.605          pass              0.357             18.8                           0.369               15.05              1.338                                 ok            True                  False
   ADP          100.00               12            2.17              3.24        212.42                33.54         0.540          pass              0.617             49.9                           0.675               -2.73             -0.097                                 ok            True                  False
  SNPS           96.67               30            1.29              4.65        511.22                43.23         0.537          pass              0.705             39.2                           0.442                5.27              0.677                                 ok            True                  False
  CDNS           96.67               30            1.39              3.47        356.55                38.69         0.513          pass              0.700             38.3                           0.351                7.01              0.865                                 ok            True                  False
  MCHP           81.48               27            1.22              0.83         97.34                50.72         0.510          pass              0.339             44.9                           0.229                7.03              0.734                                 ok            True                  False
  CHTR           63.64               11            3.67              3.80        146.29               118.13         0.743          pass              0.113             10.6                           0.262              -10.18             -1.406            downtrend_blocked_slope           False                  False
  GEHC           75.61               41            0.43              0.19         62.21                57.10         0.557          pass              0.494             79.3                           0.576                4.27              0.382                                 ok           False                  False
  ORLY           75.00               12            1.87              1.20         91.32                35.45         0.539          pass              0.196             43.0                           0.601               -1.71             -0.544 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.00               10            1.58              1.68        151.13                21.96         0.532          pass              0.371             17.1                           0.483               -3.76             -0.464            downtrend_blocked_slope           False                  False
  MELI           88.46               26            1.68             18.52       1570.84                57.67         0.524          pass              0.590             68.4                           0.665              -12.15             -1.686            downtrend_blocked_slope           False                  False
  TMUS           84.62               26            1.18              1.60        192.61                36.44         0.518          pass              0.366             28.2                           0.502               -3.61             -0.290            downtrend_blocked_slope           False                  False
  ADSK           91.67               12            2.21              3.63        233.32                40.44         0.512          pass              0.514             46.0                           0.665               -2.62             -0.264 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-13T15:05:03.914074-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T15:00:02.608671-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T14:55:04.771508-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T14:50:04.762391-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T14:50:04.762391-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-13", "training_samples": 5035, "window": 5}
2026-05-13T12:00:04.870227-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:55:04.850117-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:50:06.013562-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:45:03.915734-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:23:31.678775-04:00 early_entry_1120  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513150503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513150503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513150503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513150503)

</details>
