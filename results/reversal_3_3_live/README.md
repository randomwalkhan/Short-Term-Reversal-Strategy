# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 11:15:04 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$4,051.00`
- Equity: `$31,986.00`
- Realized PnL: `$21,986.00`
- Unrealized PnL: `$0.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 15425.0        29.05          30.85      350.60        349.64          bid_ask_mid                      30.85                bid_ask_mid                    True           900.0                   6.20         97.30               37              0.63         45.67           49.91                  37.94                2023.0           40.0               0.13                      ok
  SNPS     option         option SNPS260618C00490000       2026-05-13                   2      3     13410.0                 12510.0        44.70          41.70      510.62        495.57          bid_ask_mid                      41.70                bid_ask_mid                    True          -900.0                  -6.71         97.14               35              0.50         52.16           63.91                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-14         2026-05-15        32.35      29.115 -1617.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           80.65               31            0.92              1.90        293.36                90.16         0.726          pass              0.443             71.1                           0.661               -1.28              0.031                                 ok            True                  False
   TXN           92.31               26            0.96              2.07        307.28                67.99         0.686          pass              0.724             73.5                           0.618                9.16              1.064                                 ok            True                  False
  SNPS          100.00               12            2.83             10.12        505.68                41.57         0.558          pass              0.514             15.1                           0.197                1.34              0.238                                 ok            True                  False
 GOOGL           86.67               30            0.82              2.30        400.08                40.65         0.548          pass              0.551             61.6                           0.615                3.13              0.332                                 ok            True                  False
  GOOG           87.10               31            0.80              2.21        396.22                40.76         0.547          pass              0.566             60.6                           0.591                2.82              0.321                                 ok            True                  False
   HON           80.00               10            2.10              3.20        216.35                27.08         0.521          pass              0.100             15.8                           0.219                0.31              0.293                                 ok            True                  False
  CDNS           97.14               35            0.91              2.24        351.88                37.94         0.517          pass              0.784             55.3                           0.402                2.55              0.191                                 ok            True                  False
  MCHP           82.35               17            2.93              1.99         96.19                50.84         0.508          pass              0.218             19.4                           0.245                0.26             -0.090                                 ok            True                  False
  CHTR           66.67               12            3.27              3.39        146.55               114.29         0.706          pass              0.175             30.5                           0.223              -16.64             -1.681            downtrend_blocked_slope           False                  False
 CMCSA           90.62               32            0.32              0.06         25.15                60.26         0.666          pass              0.530             11.1                           0.137               -7.72             -0.943 downtrend_blocked_slope_and_streak           False                  False
  GEHC           61.54               26            1.40              0.62         62.41                57.53         0.585          pass              0.299             44.7                           0.350                1.25              0.214                                 ok           False                  False
  MELI           81.82               11            2.67             30.07       1594.48                58.02         0.580          pass              0.132              6.2                           0.237              -15.44             -2.060            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-15T11:15:04.096489-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T11:10:04.211296-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T11:05:04.217696-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T11:00:05.390084-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T10:55:04.100799-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T10:50:04.174954-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T10:45:04.262629-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T10:40:01.261107-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T10:35:04.245705-04:00 early_entry_1035 entry_skipped {"reason": "daily_entry_limit"}
2026-05-15T10:30:01.313959-04:00 early_entry_1030 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515111504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515111504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515111504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515111504)

</details>
