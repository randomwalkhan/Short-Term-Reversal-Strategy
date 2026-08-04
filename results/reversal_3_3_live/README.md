# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-04 09:55:03 EDT`
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

- Cash: `$17,739.75`
- Equity: `$34,169.75`
- Realized PnL: `$25,229.75`
- Unrealized PnL: `$-1,060.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00050000       2026-08-03                   1    106     17490.0                 16430.0         1.65           1.55       49.76         49.85          bid_ask_mid                       1.55                bid_ask_mid                    True         -1060.0                  -6.06         100.0               11              1.28         25.54           24.39                  27.78                2866.0          205.0               0.06                      ok
```

## Today's Closed Trades (2026-08-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   KHC           90.00               20            0.59              0.11         26.37                32.72         0.619          pass              0.529             44.6                           0.385                1.84              0.296                      ok            True                  False
  MDLZ           93.33               15            1.17              0.50         61.51                32.17         0.601          pass              0.549             33.3                           0.398                1.92              0.377                      ok            True                  False
   ROP           93.33               30            0.83              2.29        391.59                47.45         0.569          pass              0.731             61.8                           0.500               11.01              1.484                      ok            True                  False
   PEP           86.36               22            0.86              0.84        139.27                26.13         0.551          pass              0.460             51.8                           0.578                2.54              0.381                      ok            True                  False
  MNST           90.00               20            0.84              0.55         93.31                26.29         0.537          pass              0.475             29.5                           0.234               -1.80              0.014                      ok            True                  False
  CTAS           92.59               27            0.86              1.23        203.48                37.98         0.532          pass              0.671             56.1                           0.392                0.92              0.139                      ok            True                  False
  PAYX          100.00               11            1.39              1.15        117.18                35.86         0.530          pass              0.703             81.1                           0.546                4.71              0.767                      ok            True                  False
  ISRG           73.33               15            1.88              4.94        373.29                72.79         0.682          pass              0.138             12.3                           0.203                5.22              0.826                      ok           False                  False
  TMUS           92.31               26            1.01              1.25        176.55                55.96         0.638          pass              0.564             21.8                           0.242               -8.11             -0.669 downtrend_blocked_slope           False                  False
  PYPL           92.86               42            0.29              0.12         57.82                60.15         0.633          pass              0.836             76.7                           0.699                3.31              0.442                      ok           False                  False
  GEHC           95.24               42            0.04              0.02         69.72                58.11         0.616          pass              0.952             96.9                           0.796               12.41              1.659                      ok           False                  False
  AMZN           73.33               15            2.32              4.61        282.04                60.32         0.590          pass              0.182             30.0                           0.348               12.07              1.475                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-08-04T08:05:01.281633-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T08:00:06.156963-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:55:05.413752-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:50:01.172793-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:45:05.958919-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:40:04.165148-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:35:01.120189-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:30:05.395017-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:25:03.273027-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:20:01.112569-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260804095503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260804095503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260804095503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260804095503)

</details>
