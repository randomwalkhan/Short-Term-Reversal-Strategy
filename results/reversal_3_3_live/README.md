# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-18 10:33:08 EDT`
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

- Cash: `$24,658.00`
- Equity: `$46,578.00`
- Realized PnL: `$36,898.00`
- Unrealized PnL: `$-320.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ALNY     option         option ALNY260918C00220000       2026-08-17                   1     16     22240.0                 21920.0         13.9           13.7      224.68        224.76          bid_ask_mid                       13.7                bid_ask_mid                    True          -320.0                  -1.44         84.62               26              1.73         43.62           48.96                 127.87                 332.0           21.0               0.06                      ok
```

## Today's Closed Trades (2026-08-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  UPRO           85.71               21            1.41              1.52        153.75                41.29         0.580            pass              0.368             28.0                           0.535               -1.24              0.020                                 ok            True                  False
  NVDA           86.36               22            2.13              3.35        223.57                39.09         0.510            pass              0.368             22.5                           0.484                3.91              0.322                                 ok            True                  False
    MU           82.61               23            5.50             38.93        995.07               104.10         0.509            pass              0.247             13.3                           0.281                7.11              1.079                                 ok            True                  False
  INSM           86.67               45            0.48              0.43        128.14               109.50         0.740            pass              0.656             68.1                           0.737               29.32              1.817                                 ok           False                  False
   APP           74.47               47            0.00              0.01        311.98                90.76         0.668            pass              0.566             99.7                           0.585              -25.67             -2.869            downtrend_blocked_slope           False                  False
  AMZN           84.44               45            0.02              0.04        261.29                61.74         0.614            pass              0.675             98.5                           0.917               -5.83             -0.654 downtrend_blocked_slope_and_streak           False                  False
  PCAR          100.00               11            1.71              1.57        130.17                28.21         0.571            pass              0.494             10.0                           0.187               -5.16             -0.387            downtrend_blocked_slope           False                  False
   HON           90.32               31            0.41              0.65        229.17                37.29         0.552            pass              0.597             42.2                           0.340               -7.87             -0.860            downtrend_blocked_slope           False                  False
  CSCO           77.78               18            1.63              1.29        112.35                42.21         0.551            pass              0.111              0.8                           0.047               -8.77             -1.023            downtrend_blocked_slope           False                  False
 GOOGL           77.08               48            0.07              0.17        343.93                47.98         0.520            pass              0.533             93.7                           0.817               -8.97             -0.806            downtrend_blocked_slope           False                  False
  MCHP           86.67               15            4.54              2.55         79.17                73.04         0.503            pass              0.299             12.4                           0.354               -5.03             -0.269 downtrend_blocked_slope_and_streak           False                  False
  AMAT           78.57               14            4.93             18.49        527.39                84.57         0.498 below_threshold              0.144             22.6                           0.565               -6.90             -0.580            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-18T10:33:08.530330-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T09:38:41.008763-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T09:20:07.104993-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T09:15:08.426968-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T09:11:00.046303-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:52:52.256088-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:35:07.917262-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:32:57.454440-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:15:02.899134-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-08-18T08:12:27.971020-04:00     data_refresh       data_refresh                                                         {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260818103308)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260818103308)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260818103308)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260818103308)

</details>
