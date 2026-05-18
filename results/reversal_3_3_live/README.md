# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 11:55:01 EDT`
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

- Cash: `$15,642.50`
- Equity: `$29,242.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$50.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260618C00250000       2026-05-18                   0     10     13550.0                 13600.0        13.55           13.6      241.03        240.77          bid_ask_mid                       13.6                bid_ask_mid                    True            50.0                   0.37         97.62               42              0.58         61.06           61.62                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-18)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-15         2026-05-18        29.05      26.145 -1452.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               30            1.23              0.94        108.37               115.99         0.698            pass              0.799             65.3                           0.449               12.16              0.749                                 ok            True                  False
  QCOM           90.00               20            1.74              2.46        200.44                99.06         0.669            pass              0.567             55.6                           0.675               17.58              1.176                                 ok            True                  False
  CSCO           88.89               18            1.27              1.05        117.76                49.84         0.623            pass              0.446             31.2                           0.392               26.00              2.711                                 ok            True                  False
  AMGN           86.67               15            0.92              2.10        325.41                26.25         0.536            pass              0.388             41.1                           0.411                0.59              0.112                                 ok            True                  False
  SNPS           94.74               19            2.09              7.36        499.27                42.05         0.533            pass              0.552             15.3                           0.342               -1.12             -0.013                                 ok            True                  False
  AAPL           86.67               15            1.40              2.93        298.97                22.88         0.531            pass              0.311             15.5                           0.285                7.04              0.692                                 ok            True                  False
  NXPI           85.00               40            0.03              0.07        291.47                90.58         0.724            pass              0.691             95.0                           0.523                0.22             -0.037                                 ok           False                  False
   TXN           93.75               32            0.35              0.73        302.42                68.84         0.687            pass              0.802             73.4                           0.605                7.95              0.942                                 ok           False                  False
  INSM           46.67               15            3.35              2.56        108.04               111.34         0.602            pass              0.157             21.1                           0.199              -24.66             -2.308 downtrend_blocked_slope_and_streak           False                  False
  META           73.08               26            1.09              4.70        612.21                37.75         0.514            pass              0.327             56.3                           0.433               -0.48              0.048                                 ok           False                  False
  MCHP           88.10               42            0.36              0.24         93.75                53.01         0.505            pass              0.688             74.0                           0.586               -1.88             -0.524 downtrend_blocked_slope_and_streak           False                  False
  AVGO           91.67               24            1.65              4.91        423.09                43.18         0.494 below_threshold              0.547             31.2                           0.300                0.40              0.086                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                             detail
2026-05-18T11:55:01.697815-04:00 early_entry_1155 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:50:04.542688-04:00 early_entry_1150 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:45:01.537610-04:00 early_entry_1145 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:40:04.531844-04:00 early_entry_1140 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:35:01.580218-04:00 early_entry_1135 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:30:01.530896-04:00 early_entry_1130 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:25:06.197767-04:00 early_entry_1125 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:25:06.197767-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "CDNS260618C00330000", "fill_price": 26.145, "pnl": -1452.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CDNS"}
2026-05-18T11:20:01.549476-04:00 early_entry_1120 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-18T11:15:03.521300-04:00 early_entry_1115 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518115501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518115501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518115501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518115501)

</details>
