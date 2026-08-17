# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-17 09:55:01 EDT`
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

- Cash: `$46,898.00`
- Equity: `$46,898.00`
- Realized PnL: `$36,898.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  SOXL     option         option SOXL260918C00140000      9          2026-08-14         2026-08-17         21.8        28.1 5670.0   28.899083 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  ALNY           81.25               16            2.41              3.85        227.00               127.87         0.835          pass              0.204             15.7                           0.184                1.28              0.268                  ok            True                  False
  SHOP           94.74               19            2.66              2.87        153.09                83.98         0.678          pass              0.555             11.3                           0.215               28.38              2.252                  ok            True                  False
  ABNB           96.88               32            0.89              1.15        183.57                64.74         0.644          pass              0.707             32.0                           0.298               21.10              2.492                  ok            True                  False
  GEHC           95.24               21            1.32              0.68         73.40                52.52         0.634          pass              0.581             14.9                           0.145                6.91              0.724                  ok            True                  False
 CMCSA           88.24               17            1.05              0.19         26.10                41.99         0.630          pass              0.403             24.7                           0.220                5.48              0.605                  ok            True                  False
  MDLZ           90.48               21            1.05              0.47         63.41                26.02         0.547          pass              0.453             15.2                           0.204                1.96              0.188                  ok            True                  False
   ROP          100.00               18            1.65              4.61        397.36                41.77         0.540          pass              0.555             15.8                           0.122                0.05              0.068                  ok            True                  False
  WDAY           85.19               27            2.49              3.46        197.20                90.03         0.525          pass              0.382             25.9                           0.424               17.38              1.849                  ok            True                  False
   XEL          100.00               24            0.76              0.42         78.99                16.04         0.523          pass              0.621             25.0                           0.263                1.13              0.212                  ok            True                  False
  CHTR           88.89               18            2.80              3.02        152.98                52.98         0.522          pass              0.371              9.3                           0.110                4.06              0.213                  ok            True                  False
   TRI           88.46               26            2.51              1.82        102.83                75.08         0.520          pass              0.450             22.0                           0.214               -0.60              0.053                  ok            True                  False
   LIN           85.71               28            0.84              2.83        481.53                26.03         0.511          pass              0.374             16.8                           0.192               -0.37             -0.142                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                                                                                                                                                                detail
2026-08-17T09:50:05.672730-04:00    manage_1000          exit {"asset_type": "option", "contract_symbol": "SOXL260918C00140000", "fill_price": 28.1, "pnl": 5670.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 28.9, "ticker": "SOXL"}
2026-08-17T03:00:01.859006-04:00   data_refresh  data_refresh                                                                                                                                                                         {'saved': 93}
2026-08-15T02:55:03.720107-04:00 share_ext_0255 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:50:05.933577-04:00 share_ext_0250 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:45:06.097367-04:00 share_ext_0245 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:40:01.513034-04:00 share_ext_0240 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:35:02.859847-04:00 share_ext_0235 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:30:02.424773-04:00 share_ext_0230 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:25:41.575248-04:00 share_ext_0225 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:15:46.829792-04:00 share_ext_0215 market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260817095501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260817095501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260817095501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260817095501)

</details>
