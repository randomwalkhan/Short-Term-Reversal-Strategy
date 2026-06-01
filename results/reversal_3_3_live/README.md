# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 12:15:06 EDT`
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
- Equity: `$32,029.25`
- Realized PnL: `$20,849.25`
- Unrealized PnL: `$1,180.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 15280.0        35.25           38.2      477.34        485.98          bid_ask_mid                       38.2                bid_ask_mid                    True          1180.0                   8.37         97.22               36              0.69         45.69           46.49                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MRVL     option         option MRVL260717C00200000      5          2026-06-01         2026-06-01         28.3       25.47 -1415.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  LRCX           91.18               34            0.63              1.40        317.58                55.15         0.550          pass              0.759             82.1                           0.756               11.05              1.599                                 ok            True                   True
   HON           80.00               10            1.47              2.44        236.81                24.41         0.545          pass              0.152             32.4                           0.468                9.91              1.098                                 ok            True                  False
  MDLZ           92.31               13            1.48              0.63         60.90                14.75         0.502          pass              0.476             25.8                           0.516               -0.29              0.016                                 ok            True                  False
  INSM           58.82               17            3.04              2.27        105.94               110.85         0.723          pass              0.144              8.3                           0.196               -5.02             -0.249                                 ok           False                  False
  CSCO           94.74               38            0.08              0.07        120.39                51.99         0.587          pass              0.924             95.3                           0.636                1.78              0.287                                 ok           False                  False
   WMT           75.00               12            1.56              1.26        115.21                32.67         0.552          pass              0.122             17.8                           0.420              -13.31             -1.695 downtrend_blocked_slope_and_streak           False                  False
  REGN           78.57               14            1.98              8.52        611.13                42.14         0.552          pass              0.096              4.7                           0.227              -13.57             -0.853 downtrend_blocked_slope_and_streak           False                  False
  KLAC           91.43               35            0.46              6.20       1919.05                50.27         0.535          pass              0.751             75.2                           0.496                6.15              1.079                                 ok           False                  False
   PEP           91.67               12            1.58              1.60        143.51                22.18         0.533          pass              0.421             14.3                           0.392               -4.84             -0.460            downtrend_blocked_slope           False                  False
  AAPL           85.71                7            1.92              4.20        310.26                17.18         0.532          pass              0.206              0.1                           0.255                1.94              0.439                                 ok           False                  False
   AEP           60.00                5            1.94              1.72        125.93                24.34         0.530          pass              0.080              9.1                           0.274               -0.75             -0.069                                 ok           False                  False
  COST           55.56                9            1.50             10.01        952.03                27.93         0.525          pass              0.102             16.4                           0.439              -10.19             -1.343 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601121506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601121506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601121506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601121506)

</details>
