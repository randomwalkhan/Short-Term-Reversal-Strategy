# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 14:05:01 EDT`
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

- Cash: `$18,164.25`
- Equity: `$33,224.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$960.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 15060.0        35.25          37.65      477.34         476.0          bid_ask_mid                      37.65                bid_ask_mid                    True           960.0                   6.81         97.22               36              0.69         45.69           52.08                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           92.00               25            1.75              2.75        223.45               139.09         0.732            pass              0.599             35.3                           0.312               18.53              3.708                                 ok            True                  False
  INTC           95.24               21            2.88              2.44        119.85                85.20         0.549            pass              0.571             14.3                           0.215                1.28              0.969                                 ok            True                  False
  INSM           72.97               37            0.86              0.65        108.09               111.11         0.773            pass              0.404             48.9                           0.373               -7.07             -0.368            downtrend_blocked_slope           False                  False
  MELI           94.87               39            0.40              4.70       1693.51                61.27         0.615            pass              0.822             56.7                           0.287                5.07              0.809                                 ok           False                  False
   AEP           69.23               13            0.59              0.53        127.53                25.60         0.600            pass              0.164             28.1                           0.245               -1.24              0.105                                 ok           False                  False
  REGN           85.71               28            0.95              4.12        619.76                44.05         0.560            pass              0.357              9.7                           0.154              -13.51             -1.082 downtrend_blocked_slope_and_streak           False                  False
  AMAT           91.43               35            0.26              0.83        449.33                50.48         0.553            pass              0.738             70.4                           0.362                1.93              0.639                                 ok           False                  False
 GOOGL           90.00               10            1.83              5.00        387.99                41.30         0.546            pass              0.401             26.7                           0.460               -4.51             -0.336            downtrend_blocked_slope           False                  False
  KLAC           91.43               35            0.48              6.42       1924.88                52.36         0.532            pass              0.654             43.3                           0.352                1.48              0.899                                 ok           False                  False
  SBUX          100.00                6            1.85              1.30        100.19                16.60         0.525            pass              0.575             41.0                           0.347               -6.51             -0.753            downtrend_blocked_slope           False                  False
  AMGN           91.18               34            0.25              0.58        336.23                27.03         0.500 below_threshold              0.735             75.7                           0.658                0.58              0.284                                 ok           False                  False
  GOOG           88.24               17            1.66              4.49        384.19                41.01         0.499 below_threshold              0.414             32.6                           0.496               -4.40             -0.343            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-29T12:00:03.057178-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:55:04.089378-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:50:02.199680-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:45:01.211344-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:40:05.216205-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:35:06.186769-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:30:03.208249-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:25:01.209372-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:20:01.214678-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:15:06.204511-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529140501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529140501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529140501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529140501)

</details>
