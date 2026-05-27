# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 14:05:05 EDT`
Last processed slot: `manage_1400`

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
- Equity: `$31,095.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$-490.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 11520.0        60.05           57.6       531.8        523.79          bid_ask_mid                       57.6                bid_ask_mid                    True          -490.0                  -4.08         97.22               36              0.52         54.56            57.9                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           80.00               20            0.53              0.31         83.59                55.63         0.651          pass              0.324             63.9                           0.287               -3.85              0.203                                 ok            True                  False
  NXPI           86.21               29            1.13              2.63        331.54                92.16         0.646          pass              0.467             36.8                           0.317               11.79              1.205                                 ok            True                  False
  INTC           94.44               18            3.55              3.07        122.20                91.80         0.581          pass              0.593             32.0                           0.419               -1.23              0.373                                 ok            True                  False
  ORLY           80.77               26            1.19              0.75         89.55                38.82         0.512          pass              0.280             34.0                           0.540               -3.31             -0.002                                 ok            True                  False
  ASML           88.89               27            1.94             22.14       1622.54                54.27         0.508          pass              0.508             35.5                           0.437                5.22              0.581                                 ok            True                  False
  INSM           69.70               33            1.48              1.13        108.39               110.60         0.719          pass              0.354             42.9                           0.581               -7.53             -0.866            downtrend_blocked_slope           False                  False
   AEP           66.67               12            0.86              0.79        130.56                25.21         0.596          pass              0.147             24.7                           0.272               -1.64              0.142                                 ok           False                  False
  PAYX           95.24               21            0.48              0.32         94.66                30.13         0.578          pass              0.592             20.2                           0.251                1.97              0.578                                 ok           False                  False
  FTNT          100.00                5            4.30              4.03        132.23                66.88         0.578          pass              0.541             27.6                           0.398               12.58              1.388                                 ok           False                  False
  REGN           88.24               34            0.60              2.68        633.47                48.91         0.575          pass              0.618             60.2                           0.503              -12.67             -1.482 downtrend_blocked_slope_and_streak           False                  False
  SBUX           95.65               23            0.66              0.47        101.22                33.52         0.571          pass              0.688             48.1                           0.230               -4.92             -0.484 downtrend_blocked_slope_and_streak           False                  False
  GEHC           74.29               35            0.70              0.32         64.04                58.90         0.570          pass              0.365             47.1                           0.438                2.31              0.447                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527140505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527140505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527140505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527140505)

</details>
