# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 11:45:03 EDT`
Last processed slot: `early_entry_1145`

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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$20,193.50`
- Equity: `$33,273.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-330.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 13080.0         44.7           43.6      510.62        506.08          -330.0                  -2.46         97.14               35               0.5         52.16           55.36                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           83.33               12            5.06              3.01         83.71               115.69         0.597          pass              0.193             10.4                           0.139               14.48              1.316                                 ok            True                  False
  MDLZ           86.67               15            1.27              0.55         61.46                23.07         0.544          pass              0.285              6.5                           0.131               -0.20              0.012                                 ok            True                  False
  SNPS           96.55               29            1.39              4.99        511.07                43.23         0.541          pass              0.662             27.2                           0.404                5.17              0.673                                 ok            True                  False
  FAST           96.43               28            0.55              0.17         43.25                22.09         0.517          pass              0.647             25.0                           0.319               -1.44             -0.327                                 ok            True                  False
  CDNS           97.30               37            0.81              2.03        357.17                38.69         0.502          pass              0.822             63.9                           0.397                7.63              0.891                                 ok            True                  False
  CHTR           76.47               17            2.51              2.60        146.80               118.13         0.782          pass              0.225             33.2                           0.448               -9.11             -1.352            downtrend_blocked_slope           False                  False
 CMCSA           92.86               14            1.08              0.19         24.82                62.10         0.723          pass              0.523             27.0                           0.206               -7.96             -1.026 downtrend_blocked_slope_and_streak           False                  False
  GEHC           70.59               34            0.92              0.40         62.12                57.10         0.564          pass              0.383             55.5                           0.723                3.76              0.360                                 ok           False                  False
  SHOP           78.95               19            2.96              2.07         98.95                84.62         0.555          pass              0.204             29.4                           0.394              -20.11             -2.549 downtrend_blocked_slope_and_streak           False                  False
  MELI           82.35               17            2.20             24.33       1568.35                57.67         0.538          pass              0.339             58.5                           0.814              -12.62             -1.710            downtrend_blocked_slope           False                  False
   ADP          100.00                9            2.70              4.05        212.08                33.54         0.535          pass              0.550             32.1                           0.266               -3.27             -0.122                                 ok           False                  False
   PEP           90.91               11            1.49              1.59        151.17                21.96         0.534          pass              0.386             11.7                           0.277               -3.68             -0.461            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-13T11:45:03.915734-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T11:23:31.678775-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T11:05:05.896760-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T11:00:06.549783-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:55:05.050603-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:50:03.713971-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:45:06.364119-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:40:01.859562-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:35:05.886514-04:00 early_entry_1035 entry_skipped {"reason": "daily_entry_limit"}
2026-05-13T10:30:03.887456-04:00 early_entry_1030 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513114503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513114503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513114503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513114503)

</details>
