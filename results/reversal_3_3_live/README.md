# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 11:15:02 EDT`
Last processed slot: `early_entry_1115`

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
- Equity: `$31,024.25`
- Realized PnL: `$20,384.25`
- Unrealized PnL: `$640.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-28                   0      4     12500.0                 13140.0        31.25          32.85      419.65        423.04          bid_ask_mid                      32.85                bid_ask_mid                    True           640.0                   5.12         89.19               37              0.52         51.04            50.7                  36.99                2631.0           27.0               0.06                      ok
```

## Today's Closed Trades (2026-05-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260717C00500000      2          2026-05-27         2026-05-28        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           96.67               30            1.29              1.10        121.30                92.16         0.620            pass              0.810             71.5                           0.854               -0.07              0.770                                 ok            True                   True
    ZS           85.29               34            1.05              0.93        126.01               152.21         0.826            pass              0.586             67.5                           0.689              -17.94             -1.182            downtrend_blocked_slope           False                  False
  CSCO           94.12               34            0.31              0.26        119.56                51.65         0.602            pass              0.831             78.1                           0.654               17.11              0.894                                 ok           False                  False
   XEL          100.00                7            2.01              1.14         80.51                25.49         0.569            pass              0.476              6.3                           0.172               -0.68              0.185                                 ok           False                  False
  ROST           83.33                6            2.53              4.14        231.70                38.54         0.565            pass              0.203             19.2                           0.347                7.46              1.137                                 ok           False                  False
   WMT           93.33               30            0.59              0.49        118.33                34.18         0.529            pass              0.567              8.6                           0.123              -10.36             -1.461 downtrend_blocked_slope_and_streak           False                  False
  REGN           88.24               34            0.61              2.67        626.60                48.81         0.523            pass              0.541             36.3                           0.420              -13.20             -1.309 downtrend_blocked_slope_and_streak           False                  False
  MPWR           94.12               34            0.41              4.65       1618.18                53.62         0.519            pass              0.844             85.3                           0.874               -2.23              0.282           downtrend_blocked_streak           False                  False
  AMGN           90.00               30            0.40              0.93        335.66                27.08         0.511            pass              0.568             38.9                           0.199                0.24              0.216                                 ok           False                  False
   AEP           50.00                4            2.14              1.94        128.74                25.33         0.508            pass              0.111             20.2                           0.141               -0.90              0.168                                 ok           False                  False
   CEG           79.41               34            1.03              2.09        287.79                55.24         0.496 below_threshold              0.414             68.1                           0.514                4.09              0.985                                 ok           False                  False
  NVDA           90.00               40            0.13              0.20        212.52                40.71         0.492 below_threshold              0.791             91.8                           0.602               -5.98             -0.848 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-28T11:15:02.993197-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:10:05.974897-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:05:05.990852-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:00:06.281016-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:55:05.933793-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:50:05.877302-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:45:02.890829-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:40:06.973903-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:35:04.979836-04:00 early_entry_1035 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:30:05.932623-04:00 early_entry_1030 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528111502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528111502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528111502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528111502)

</details>
