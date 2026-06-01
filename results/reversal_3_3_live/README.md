# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 12:20:05 EDT`
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

- Cash: `$16,749.25`
- Equity: `$32,149.25`
- Realized PnL: `$20,849.25`
- Unrealized PnL: `$1,300.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 15400.0        35.25           38.5      477.34        487.07          bid_ask_mid                       38.5                bid_ask_mid                    True          1300.0                   9.22         97.22               36              0.69         45.69            44.6                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MRVL     option         option MRVL260717C00200000      5          2026-06-01         2026-06-01         28.3       25.47 -1415.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  LRCX           91.18               34            0.62              1.37        317.59                55.15         0.551          pass              0.761             82.5                           0.718               11.06              1.600                                 ok            True                   True
  MDLZ           92.31               13            1.49              0.64         60.90                14.75         0.501          pass              0.475             25.4                           0.525               -0.30              0.015                                 ok            True                  False
  INSM           58.82               17            3.18              2.38        105.89               110.85         0.715          pass              0.131              4.2                           0.127               -5.15             -0.256            downtrend_blocked_slope           False                  False
  CSCO           94.74               38            0.16              0.13        120.36                51.99         0.582          pass              0.911             91.0                           0.604                1.71              0.283                                 ok           False                  False
  REGN           83.33               18            1.69              7.29        611.66                42.14         0.549          pass              0.253             18.5                           0.282              -13.32             -0.839 downtrend_blocked_slope_and_streak           False                  False
   WMT           75.00               12            1.66              1.35        115.17                32.67         0.545          pass              0.104             12.1                           0.340              -13.41             -1.700 downtrend_blocked_slope_and_streak           False                  False
  KLAC           91.43               35            0.40              5.40       1919.40                50.27         0.539          pass              0.761             78.4                           0.514                6.21              1.082                                 ok           False                  False
   PEP           91.67               12            1.56              1.57        143.52                22.18         0.534          pass              0.424             15.4                           0.385               -4.81             -0.459            downtrend_blocked_slope           False                  False
   AEP           60.00                5            1.89              1.67        125.95                24.34         0.534          pass              0.088             11.6                           0.351               -0.70             -0.066                                 ok           False                  False
  AAPL           85.71                7            1.94              4.23        310.25                17.18         0.530          pass              0.219              4.7                           0.248                1.93              0.438                                 ok           False                  False
   HON           75.00                8            1.84              3.07        236.55                24.41         0.529          pass              0.098             15.1                           0.214                9.49              1.081                                 ok           False                  False
  ROST           66.67                3            3.13              5.08        229.55                40.27         0.527          pass              0.074              7.2                           0.208                5.51              0.960                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601122005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601122005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601122005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601122005)

</details>
