# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 12:45:04 EDT`
Last processed slot: `manual`

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

- Cash: `$16,749.25`
- Equity: `$33,269.25`
- Realized PnL: `$20,849.25`
- Unrealized PnL: `$2,420.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 16520.0        35.25           41.3      477.34         489.4          bid_ask_mid                       41.3                bid_ask_mid                    True          2420.0                  17.16         97.22               36              0.69         45.69           49.55                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MRVL     option         option MRVL260717C00200000      5          2026-06-01         2026-06-01         28.3       25.47 -1415.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           92.31               13            1.31              0.56         60.93                14.75         0.513          pass              0.503             34.4                           0.594               -0.12              0.024                                 ok            True                  False
  INSM           46.15               13            3.58              2.68        105.76               110.85         0.699          pass              0.102              4.0                           0.199               -5.55             -0.275            downtrend_blocked_slope           False                  False
  CSCO           94.59               37            0.22              0.19        120.34                51.99         0.584          pass              0.889             87.3                           0.489                1.64              0.280                                 ok           False                  False
  REGN           78.57               14            1.90              8.19        611.27                42.14         0.557          pass              0.108              8.5                           0.280              -13.50             -0.849 downtrend_blocked_slope_and_streak           False                  False
   WMT           75.00               12            1.56              1.27        115.21                32.67         0.551          pass              0.121             17.4                           0.346              -13.32             -1.695 downtrend_blocked_slope_and_streak           False                  False
   AEP           66.67                6            1.66              1.47        126.04                24.34         0.550          pass              0.122             22.4                           0.515               -0.46             -0.056                                 ok           False                  False
  LRCX           91.89               37            0.49              1.08        317.72                55.15         0.539          pass              0.810             86.2                           0.782               11.21              1.606                                 ok           False                  False
   HON           75.00                8            1.76              2.93        236.60                24.41         0.534          pass              0.110             18.9                           0.253                9.58              1.084                                 ok           False                  False
  AAPL           85.71                7            1.92              4.19        310.26                17.18         0.530          pass              0.232              8.8                           0.299                1.95              0.439                                 ok           False                  False
  COST           62.50                8            1.72             11.52        951.38                27.93         0.525          pass              0.066              4.4                           0.258              -10.40             -1.354 downtrend_blocked_slope_and_streak           False                  False
   PEP           85.71               14            1.46              1.48        143.56                22.18         0.519          pass              0.293             20.7                           0.464               -4.72             -0.454            downtrend_blocked_slope           False                  False
  GOOG           89.47               19            1.42              3.74        374.83                25.35         0.518          pass              0.426             20.5                           0.320               -5.65             -0.411            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-06-01T12:00:03.957402-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:55:05.058620-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:50:02.013615-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:45:04.960036-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:40:03.918897-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:35:04.962377-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:30:03.931988-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:25:04.832152-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:20:01.993474-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-06-01T11:15:04.905942-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601124504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601124504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601124504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601124504)

</details>
