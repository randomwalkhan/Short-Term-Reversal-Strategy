# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 11:40:04 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$15,642.50`
- Equity: `$29,142.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$-50.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260618C00250000       2026-05-18                   0     10     13550.0                 13500.0        13.55           13.5      241.03         240.6          bid_ask_mid                       13.5                bid_ask_mid                    True           -50.0                  -0.37         97.62               42              0.58         61.06           61.21                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-18)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-15         2026-05-18        29.05      26.145 -1452.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               30            1.18              0.90        108.39               115.99         0.701            pass              0.804             66.8                           0.355               12.23              0.752                                 ok            True                  False
  QCOM           90.00               20            1.76              2.48        200.43                99.06         0.668            pass              0.566             55.2                           0.627               17.56              1.176                                 ok            True                  False
  CSCO           88.24               17            1.34              1.11        117.74                49.84         0.625            pass              0.411             27.5                           0.326               25.91              2.708                                 ok            True                  False
  AMGN           91.67               12            1.09              2.49        325.24                26.25         0.552            pass              0.470             30.2                           0.259                0.41              0.104                                 ok            True                  False
  SNPS           94.12               17            2.18              7.66        499.14                42.05         0.540            pass              0.513             11.8                           0.251               -1.21             -0.017                                 ok            True                  False
  AAPL           85.71               14            1.47              3.09        298.91                22.88         0.531            pass              0.262              9.9                           0.192                6.96              0.689                                 ok            True                  False
   TXN           93.75               32            0.24              0.51        302.51                68.84         0.693            pass              0.827             81.6                           0.552                8.06              0.947                                 ok           False                  False
  INSM           57.89               19            2.85              2.18        108.21               111.34         0.626            pass              0.221             32.9                           0.300              -24.27             -2.284 downtrend_blocked_slope_and_streak           False                  False
  SBUX           97.22               36            0.05              0.04        106.80                32.79         0.516            pass              0.917             97.4                           0.528                2.31              0.232                                 ok           False                  False
  MCHP           88.37               43            0.19              0.13         93.80                53.01         0.510            pass              0.733             86.2                           0.648               -1.71             -0.516 downtrend_blocked_slope_and_streak           False                  False
  MSFT           84.62               26            0.89              2.64        420.79                29.78         0.498 below_threshold              0.457             59.3                           0.401                1.10              0.027                                 ok           False                  False
  META           75.00               32            0.83              3.57        612.70                37.75         0.495 below_threshold              0.397             66.8                           0.681               -0.21              0.060                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-18T11:40:04.531844-04:00 early_entry_1140 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:35:01.580218-04:00 early_entry_1135 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:30:01.530896-04:00 early_entry_1130 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:25:06.197767-04:00 early_entry_1125 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:25:06.197767-04:00      manage_1130          exit                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "CDNS260618C00330000", "fill_price": 26.145, "pnl": -1452.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CDNS"}
2026-05-18T11:20:01.549476-04:00 early_entry_1120 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:15:03.521300-04:00 early_entry_1115 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:10:02.609364-04:00 early_entry_1110 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-05-18T11:05:05.558676-04:00 early_entry_1105         entry {"allocated_cash": 13550.0, "asset_type": "option", "contract_symbol": "TTWO260618C00250000", "contracts": 10, "early_entry_score": 0.906, "entry_mode": "early", "entry_option_price": 13.55, "execution_mode": "option", "matched_signals": 42, "option_liquidity_status": "ok", "option_open_interest": 3069.0, "option_spread_pct": 11.07, "option_volume": 22.0, "success_rate": 97.62, "ticker": "TTWO", "timing_score": 0.402}
2026-05-18T11:00:09.683441-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518114004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518114004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518114004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518114004)

</details>
