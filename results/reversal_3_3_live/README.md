# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 09:35:01 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$17,648.00`
- Equity: `$31,448.00`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$375.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX260918C00310000       2026-08-10                   2      5     13425.0                 13800.0        26.85           27.6      307.66        325.55     last_price_stale                        NaN                unavailable                   False           375.0                   2.79          87.1               31              1.19         68.92             0.0                  90.05                1499.0           93.0               0.03                      ok
```

## Today's Closed Trades (2026-08-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           94.12               34            0.51              0.21         58.91                59.96         0.654          pass              0.835             77.8                           0.727                0.60              0.238                  ok            True                   True
 CMCSA           90.00               20            0.88              0.16         25.58                42.38         0.628          pass              0.498             33.8                           0.324                7.41              0.700                  ok            True                  False
  GEHC           95.45               22            1.38              0.70         72.45                54.33         0.626          pass              0.669             42.2                           0.422               -0.22              0.321                  ok            True                  False
  ABNB           96.15               26            1.23              1.60        184.30                64.05         0.610          pass              0.743             58.4                           0.539               19.40              2.317                  ok            True                  False
   ROP          100.00               24            1.08              3.02        398.21                44.32         0.604          pass              0.722             56.1                           0.527                1.53              0.205                  ok            True                  False
  PAYX          100.00               21            0.67              0.57        121.06                33.26         0.587          pass              0.699             55.5                           0.513                3.58              0.408                  ok            True                  False
  MDLZ           90.00               20            1.04              0.45         61.59                29.90         0.568          pass              0.466             25.1                           0.202               -3.08             -0.218                  ok            True                  False
  WDAY           81.25               32            1.51              1.92        180.45                68.78         0.550          pass              0.398             54.4                           0.562                6.26              1.231                  ok            True                  False
   ADP           96.67               30            0.78              1.48        270.45                32.74         0.534          pass              0.731             48.2                           0.400                1.93              0.155                  ok            True                  False
  ADSK           83.33               36            0.56              0.98        251.17                45.76         0.529          pass              0.546             77.1                           0.548                6.48              0.887                  ok            True                  False
  REGN           92.31               26            1.08              6.01        794.42                33.78         0.526          pass              0.580             30.7                           0.281                6.78              0.683                  ok            True                  False
  MELI           92.86               14            2.19             29.69       1927.28                34.10         0.508          pass              0.420              0.0                           0.183                0.63              0.022                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-08-12T09:35:01.769154-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:30:01.771593-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:25:01.593760-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:20:03.729351-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:15:01.696450-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:10:04.748220-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:05:02.776077-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:00:03.695691-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T08:55:02.907270-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T08:50:06.776266-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812093501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812093501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812093501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812093501)

</details>
