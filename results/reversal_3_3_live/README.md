# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-17 09:30:06 EDT`
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

- Cash: `$21,608.00`
- Equity: `$42,731.00`
- Realized PnL: `$31,228.00`
- Unrealized PnL: `$1,503.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SOXL     option         option SOXL260918C00140000       2026-08-14                   1      9     19620.0                 21123.0         21.8          23.47      141.95        151.57     last_price_stale                        NaN                unavailable                   False          1503.0                   7.66         82.86               35              2.35        114.04             0.0                 164.53                 831.0          148.0               0.04                      ok
```

## Today's Closed Trades (2026-08-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           80.65               31            1.97              2.24        161.26               128.53         0.789          pass              0.306             23.3                           0.228               53.33              5.040                  ok            True                  False
  SHOP           96.97               33            1.22              1.31        153.76                83.98         0.684          pass              0.791             56.5                           0.532               30.28              2.319                  ok            True                  False
 CMCSA           90.91               22            0.76              0.14         26.12                41.99         0.627          pass              0.461              9.1                           0.156                5.78              0.618                  ok            True                  False
  GEHC           91.67               24            1.19              0.62         73.43                52.52         0.618          pass              0.533             22.1                           0.282                7.04              0.729                  ok            True                  False
  PAYX          100.00               18            1.00              0.85        121.65                35.05         0.589          pass              0.678             55.1                           0.384                2.66              0.394                  ok            True                  False
  DXCM           88.89               36            0.67              0.42         89.57                54.82         0.555          pass              0.707             80.5                           0.433                2.11              0.700                  ok            True                  False
   TRI           91.67               36            1.06              0.77        103.28                75.08         0.553          pass              0.740             66.9                           0.366                0.89              0.120                  ok            True                  False
  MDLZ           89.47               19            1.18              0.52         63.39                26.02         0.550          pass              0.368              0.0                           0.182                1.83              0.182                  ok            True                  False
   MAR           93.33               30            0.78              1.95        355.88                36.45         0.549          pass              0.641             32.3                           0.326                2.05              0.107                  ok            True                  False
   ROP          100.00               18            1.65              4.62        397.36                41.77         0.543          pass              0.508              0.0                           0.168                0.04              0.068                  ok            True                  False
  AMGN          100.00               27            0.77              2.25        414.25                27.10         0.541          pass              0.710             47.5                           0.453                8.74              0.732                  ok            True                  False
  WDAY           85.19               27            2.42              3.37        197.24                90.03         0.528          pass              0.388             27.8                           0.328               17.46              1.852                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-08-17T03:00:01.859006-04:00   data_refresh  data_refresh                               {'saved': 93}
2026-08-15T02:55:03.720107-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:50:05.933577-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:45:06.097367-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:40:01.513034-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:35:02.859847-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:30:02.424773-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:25:41.575248-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:15:46.829792-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:05:48.567191-04:00 share_ext_0205 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260817093006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260817093006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260817093006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260817093006)

</details>
