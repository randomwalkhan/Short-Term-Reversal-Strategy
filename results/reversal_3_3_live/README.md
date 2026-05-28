# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 12:30:03 EDT`
Last processed slot: `manage_1230`

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

- Cash: `$17,884.25`
- Equity: `$32,154.25`
- Realized PnL: `$20,384.25`
- Unrealized PnL: `$1,770.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-28                   0      4     12500.0                 14270.0        31.25          35.67      419.65        426.12          bid_ask_mid                      35.67                bid_ask_mid                    True          1770.0                  14.16         89.19               37              0.52         51.04           51.65                  36.99                2631.0           27.0               0.06                      ok
```

## Today's Closed Trades (2026-05-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260717C00500000      2          2026-05-27         2026-05-28        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           96.97               33            0.98              0.83        121.41                92.16         0.621            pass              0.850             78.4                           0.619                0.24              0.784                                 ok            True                   True
   XEL           93.75               16            1.51              0.85         80.63                25.49         0.535            pass              0.550             29.9                           0.519               -0.16              0.208                                 ok            True                  False
  CSCO           93.55               31            0.38              0.31        119.54                51.65         0.617            pass              0.784             73.7                           0.616               17.03              0.891                                 ok           False                  False
  ROST           83.33                6            2.41              3.94        231.78                38.54         0.573            pass              0.215             22.9                           0.348                7.59              1.142                                 ok           False                  False
   AEP           75.00               12            1.10              0.99        129.14                25.33         0.558            pass              0.246             59.1                           0.637                0.16              0.217                                 ok           False                  False
   WMT           93.33               30            0.54              0.44        118.35                34.18         0.530            pass              0.684             47.5                           0.555              -10.32             -1.459 downtrend_blocked_slope_and_streak           False                  False
  REGN           88.24               34            0.60              2.65        626.60                48.81         0.524            pass              0.542             36.7                           0.297              -13.20             -1.309 downtrend_blocked_slope_and_streak           False                  False
   CEG           82.93               41            0.30              0.60        288.42                55.24         0.502            pass              0.601             90.8                           0.607                4.87              1.018                                 ok           False                  False
  CHTR           88.89               36            0.79              0.82        146.83                56.79         0.497 below_threshold              0.599             46.3                           0.488                2.06              0.233                                 ok           False                  False
   CSX           85.71                7            2.21              0.73         46.83                21.52         0.496 below_threshold              0.330             42.5                           0.543                3.83              0.292                                 ok           False                  False
  AMGN           91.18               34            0.25              0.60        335.80                27.08         0.495 below_threshold              0.691             61.0                           0.481                0.38              0.222                                 ok           False                  False
  MNST           92.50               40            0.45              0.28         89.12                49.17         0.486 below_threshold              0.785             67.7                           0.700                3.39              0.267                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-28T12:00:05.896854-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:55:02.040011-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:50:05.974356-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:45:05.997889-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:40:03.231101-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:35:03.979729-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:30:01.953912-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:25:06.570222-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:20:04.888168-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:15:02.993197-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528123003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528123003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528123003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528123003)

</details>
