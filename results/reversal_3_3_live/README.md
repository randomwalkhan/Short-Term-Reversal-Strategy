# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 15:20:07 EDT`
Last processed slot: `manage_1530`

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
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 11420.0        60.05           57.1       531.8        524.71          bid_ask_mid                       57.1                bid_ask_mid                    True          -590.0                  -4.91         97.22               36              0.52         54.56           56.62                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  NXPI           86.67               30            1.12              2.60        331.56                92.16         0.641            pass              0.488             37.6                           0.310               11.80              1.206                      ok            True                  False
  INTC           95.45               22            2.93              2.53        122.43                91.80         0.596            pass              0.671             43.9                           0.478               -0.59              0.402                      ok            True                  False
  PAYX           95.00               20            0.52              0.34         94.65                30.13         0.580            pass              0.621             31.9                           0.412                1.93              0.576                      ok            True                  False
  ASML           88.89               27            1.84             21.01       1623.02                54.27         0.514            pass              0.518             38.8                           0.363                5.33              0.585                      ok            True                  False
  SOXL           85.71               21            4.21              6.66        222.94               148.29         0.512            pass              0.446             56.4                           0.513               25.37              2.101                      ok            True                  False
  LRCX           83.33               30            1.05              2.38        321.66                57.65         0.500            pass              0.451             59.5                           0.450               10.39              0.979                      ok            True                  False
  ORLY           82.76               29            1.10              0.69         89.57                38.82         0.500 below_threshold              0.367             38.9                           0.354               -3.22              0.002                      ok            True                  False
  INSM           67.86               28            1.79              1.37        108.28               110.60         0.728            pass              0.285             30.9                           0.366               -7.83             -0.881 downtrend_blocked_slope           False                  False
   TRI           71.43               14            1.45              0.85         83.36                55.63         0.619            pass              0.103              4.7                           0.158               -4.74              0.161                      ok           False                  False
   AEP           66.67               12            0.95              0.87        130.53                25.21         0.590            pass              0.124             17.3                           0.214               -1.73              0.138                      ok           False                  False
  GEHC           76.92               39            0.25              0.11         64.13                58.90         0.577            pass              0.495             81.2                           0.643                2.78              0.467                      ok           False                  False
  FTNT          100.00                4            4.51              4.23        132.15                66.88         0.572            pass              0.530             24.1                           0.204               12.34              1.378                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-27T15:10:02.000661-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T15:05:04.292282-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T15:00:06.354268-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T14:55:06.489057-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T14:50:01.720844-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T14:50:01.720844-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-27", "training_samples": 5097, "window": 5}
2026-05-27T12:00:02.710964-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:55:06.026706-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:50:03.680135-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:45:03.631384-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527152007)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527152007)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527152007)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527152007)

</details>
