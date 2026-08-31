# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-31 09:50:01 EDT`
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

- Cash: `$50,178.10`
- Equity: `$50,178.10`
- Realized PnL: `$40,178.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-31)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SHOP     option         option SHOP261016C00155000     29          2026-08-28         2026-08-31          9.0         8.1 -2610.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MNST           84.62               13            1.48              0.49         46.65               551.82         1.000          pass              0.308             21.7                           0.201                1.42              0.011                  ok            True                  False
  ABNB          100.00               14            2.02              2.67        188.28                62.79         0.682          pass              0.505              3.5                           0.196                3.53              0.294                  ok            True                  False
  MELI          100.00               14            1.96             26.91       1954.72                48.83         0.623          pass              0.509              6.8                           0.177                7.84              0.800                  ok            True                  False
   TRI           92.00               25            1.54              1.14        105.73                60.45         0.590          pass              0.683             67.9                           0.519                6.27              0.414                  ok            True                  False
  AMGN          100.00               19            0.78              2.37        431.40                27.94         0.584          pass              0.660             47.3                           0.456                2.90              0.238                  ok            True                  False
  SBUX           92.86               14            1.04              0.78        107.51                22.68         0.559          pass              0.450              8.2                           0.198               -1.10              0.137                  ok            True                  False
  PAYX          100.00               22            0.87              0.77        126.71                24.67         0.557          pass              0.536              0.0                           0.177                6.24              0.605                  ok            True                  False
  VRTX           96.55               29            0.85              3.23        540.31                33.03         0.543          pass              0.735             51.3                           0.463                4.18              0.287                  ok            True                  False
   MAR          100.00               10            1.92              4.71        349.06                33.77         0.541          pass              0.502             16.1                           0.204               -3.23             -0.233                  ok            True                  False
   KDP           82.61               23            1.14              0.26         32.07                30.92         0.531          pass              0.246             12.4                           0.118                5.06              0.482                  ok            True                  False
  IDXX           88.24               17            1.72              6.68        552.13                29.14         0.524          pass              0.380             20.4                           0.185               -0.12             -0.065                  ok            True                  False
 CMCSA           89.47               19            1.29              0.25         26.95                25.33         0.521          pass              0.365              0.0                           0.033                4.46              0.359                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                                                                                                                                                          detail
2026-08-31T09:50:01.420574-04:00    manage_1000          exit {"asset_type": "option", "contract_symbol": "SHOP261016C00155000", "fill_price": 8.1, "pnl": -2610.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SHOP"}
2026-08-31T03:00:02.021557-04:00   data_refresh  data_refresh                                                                                                                                                                   {'saved': 93}
2026-08-29T02:55:05.202083-04:00 share_ext_0255 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:50:05.132580-04:00 share_ext_0250 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:45:01.295429-04:00 share_ext_0245 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:40:01.326395-04:00 share_ext_0240 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:35:05.989284-04:00 share_ext_0235 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:30:05.313779-04:00 share_ext_0230 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:25:01.129841-04:00 share_ext_0225 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:20:04.124730-04:00 share_ext_0220 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260831095001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260831095001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260831095001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260831095001)

</details>
