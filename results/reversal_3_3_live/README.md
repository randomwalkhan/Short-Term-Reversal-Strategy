# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 14:20:01 EDT`
Last processed slot: `manage_1430`

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
- Equity: `$30,995.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$-590.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 11420.0        60.05           57.1       531.8        525.24          bid_ask_mid                       57.1                bid_ask_mid                    True          -590.0                  -4.91         97.22               36              0.52         54.56           56.18                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           86.21               29            1.13              2.62        331.55                92.16         0.646          pass              0.468             37.0                           0.289               11.79              1.205                                 ok            True                  False
  INTC           94.74               19            3.48              3.01        122.23                91.80         0.580          pass              0.611             33.5                           0.379               -1.15              0.377                                 ok            True                  False
  ASML           88.89               27            1.85             21.13       1622.97                54.27         0.514          pass              0.517             38.4                           0.461                5.32              0.585                                 ok            True                  False
  INSM           69.70               33            1.41              1.07        108.41               110.60         0.723          pass              0.362             45.6                           0.568               -7.47             -0.863            downtrend_blocked_slope           False                  False
   TRI           78.95               19            0.74              0.43         83.53                55.63         0.642          pass              0.272             49.2                           0.265               -4.06              0.193                                 ok           False                  False
   AEP           66.67               12            0.86              0.79        130.56                25.21         0.596          pass              0.148             25.0                           0.317               -1.64              0.142                                 ok           False                  False
  FTNT          100.00                5            4.28              4.02        132.24                66.88         0.579          pass              0.542             27.9                           0.333               12.60              1.389                                 ok           False                  False
  PAYX           95.83               24            0.27              0.18         94.72                30.13         0.572          pass              0.714             54.4                           0.469                2.18              0.587                                 ok           False                  False
  REGN           88.89               36            0.45              2.01        633.76                48.91         0.572          pass              0.678             70.2                           0.605              -12.54             -1.475 downtrend_blocked_slope_and_streak           False                  False
  GEHC           75.68               37            0.50              0.22         64.08                58.90         0.572          pass              0.424             62.4                           0.574                2.52              0.456                                 ok           False                  False
  SBUX           96.97               33            0.25              0.17        101.35                33.52         0.530          pass              0.849             80.7                           0.459               -4.52             -0.465 downtrend_blocked_slope_and_streak           False                  False
  NVDA           89.29               28            0.97              1.46        214.23                40.94         0.511          pass              0.616             65.6                           0.740               -3.63             -0.639 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-27T12:00:02.710964-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:55:06.026706-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:50:03.680135-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:45:03.631384-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:40:05.644907-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:35:01.763028-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:30:03.642153-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:25:02.657208-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:20:01.673157-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:15:01.657140-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527142001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527142001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527142001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527142001)

</details>
