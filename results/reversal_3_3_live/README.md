# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 11:30:03 EDT`
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

- Cash: `$19,575.25`
- Equity: `$31,635.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$50.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 12060.0        60.05           60.3       531.8        525.54          bid_ask_mid                       60.3                bid_ask_mid                    True            50.0                   0.42         97.22               36              0.52         54.56           59.91                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           87.88               33            0.85              1.99        331.82                92.16         0.639          pass              0.584             52.2                           0.466               12.10              1.218                                 ok            True                  False
  INTC           94.12               17            3.81              3.29        122.11                91.80         0.571          pass              0.562             27.2                           0.329               -1.48              0.361                                 ok            True                  False
  ISRG           90.91               11            2.54              7.76        433.32                35.34         0.525          pass              0.363              4.4                           0.158               -1.46              0.130                                 ok            True                  False
  ASML           89.66               29            1.68             19.16       1623.82                54.27         0.512          pass              0.568             44.2                           0.491                5.50              0.593                                 ok            True                  False
  INSM           67.86               28            1.88              1.44        108.25               110.60         0.728          pass              0.223             10.1                           0.196               -7.91             -0.885            downtrend_blocked_slope           False                  False
   AEP           78.95               19            0.34              0.31        130.77                25.21         0.599          pass              0.332             70.7                           0.730               -1.12              0.166                                 ok           False                  False
  PAYX           95.83               24            0.13              0.08         94.76                30.13         0.582          pass              0.787             78.6                           0.321                2.33              0.594                                 ok           False                  False
  REGN           87.10               31            0.78              3.47        633.13                48.91         0.582          pass              0.533             48.5                           0.365              -12.83             -1.490 downtrend_blocked_slope_and_streak           False                  False
  FTNT          100.00                3            4.97              4.66        131.96                66.88         0.549          pass              0.504             16.3                           0.136               11.79              1.356                                 ok           False                  False
  ORLY           68.75               16            1.50              0.95         89.46                38.82         0.547          pass              0.140             15.1                           0.280               -3.61             -0.016                                 ok           False                  False
  UPRO           94.44               36            0.28              0.29        145.74                30.88         0.508          pass              0.775             55.3                           0.378                4.24              0.286                                 ok           False                  False
  NVDA           80.00               15            2.27              3.41        213.40                40.94         0.504          pass              0.143             19.9                           0.395               -4.89             -0.699 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-27T11:30:03.642153-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:25:02.657208-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:20:01.673157-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:15:01.657140-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:10:01.701881-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:05:03.689642-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:00:02.698480-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T10:55:01.700501-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T10:50:01.641792-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T10:45:02.652833-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527113003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527113003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527113003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527113003)

</details>
