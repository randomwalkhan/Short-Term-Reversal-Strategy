# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 12:05:06 EDT`
Last processed slot: `manage_1200`

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
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$17,884.25`
- Equity: `$31,634.25`
- Realized PnL: `$20,384.25`
- Unrealized PnL: `$1,250.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-28                   0      4     12500.0                 13750.0        31.25          34.38      419.65        425.08          bid_ask_mid                      34.38                bid_ask_mid                    True          1250.0                   10.0         89.19               37              0.52         51.04           50.37                  36.99                2631.0           27.0               0.06                      ok
```

## Today's Closed Trades (2026-05-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260717C00500000      2          2026-05-27         2026-05-28        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           96.67               30            1.19              1.02        121.33                92.16         0.626          pass              0.817             73.6                           0.501                0.02              0.774                                 ok            True                  False
   XEL           90.91               11            1.63              0.92         80.60                25.49         0.557          pass              0.426             24.1                           0.520               -0.29              0.202                                 ok            True                  False
  CHTR           84.62               26            1.48              1.53        146.53                56.79         0.513          pass              0.281              0.0                           0.002                1.36              0.201                                 ok            True                  False
  MNST           91.67               36            0.55              0.34         89.09                49.17         0.506          pass              0.716             60.5                           0.641                3.28              0.263                                 ok            True                   True
  CSCO           94.12               34            0.33              0.27        119.55                51.65         0.601          pass              0.828             77.2                           0.709               17.09              0.893                                 ok           False                  False
  ROST           83.33                6            2.34              3.83        231.83                38.54         0.577          pass              0.222             25.2                           0.411                7.67              1.145                                 ok           False                  False
   AEP           75.00               12            1.09              0.99        129.15                25.33         0.558          pass              0.247             59.4                           0.679                0.16              0.217                                 ok           False                  False
   WMT           92.86               28            0.71              0.59        118.29                34.18         0.531          pass              0.606             30.2                           0.434              -10.48             -1.467 downtrend_blocked_slope_and_streak           False                  False
  REGN           88.89               36            0.48              2.10        626.84                48.81         0.520          pass              0.612             49.9                           0.618              -13.09             -1.303 downtrend_blocked_slope_and_streak           False                  False
  AMGN           90.00               30            0.40              0.95        335.65                27.08         0.511          pass              0.564             37.6                           0.370                0.23              0.215                                 ok           False                  False
   TXN           96.88               32            0.15              0.34        317.30                35.35         0.510          pass              0.871             91.2                           0.426                3.47              0.495                                 ok           False                  False
  KLAC           88.89               36            0.40              5.45       1954.85                51.91         0.501          pass              0.725             88.2                           0.723                5.52              0.853                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-28T12:00:05.896854-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:55:02.040011-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:50:05.974356-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:45:05.997889-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:40:03.231101-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:35:03.979729-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:30:01.953912-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:25:06.570222-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:20:04.888168-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:15:02.993197-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528120506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528120506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528120506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528120506)

</details>
