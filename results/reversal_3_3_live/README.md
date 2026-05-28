# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 11:05:05 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$30,644.25`
- Realized PnL: `$20,384.25`
- Unrealized PnL: `$260.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-28                   0      4     12500.0                 12760.0        31.25           31.9      419.65        424.95          bid_ask_mid                       31.9                bid_ask_mid                    True           260.0                   2.08         89.19               37              0.52         51.04           46.63                  36.99                2631.0           27.0               0.06                      ok
```

## Today's Closed Trades (2026-05-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260717C00500000      2          2026-05-27         2026-05-28        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           96.67               30            1.34              1.14        121.28                92.16         0.616            pass              0.806             70.3                           0.853               -0.13              0.767                                 ok            True                   True
   LIN           89.47               19            1.19              4.25        506.05                20.85         0.500            pass              0.467             34.7                           0.541               -2.23             -0.043                                 ok            True                  False
    ZS           85.29               34            1.24              1.10        125.94               152.21         0.819            pass              0.568             61.6                           0.766              -18.10             -1.190            downtrend_blocked_slope           False                  False
  CSCO           92.86               28            0.46              0.39        119.50                51.65         0.630            pass              0.729             67.5                           0.569               16.93              0.887                                 ok           False                  False
   XEL          100.00                9            1.81              1.03         80.56                25.49         0.570            pass              0.491             11.4                           0.188               -0.48              0.194                                 ok           False                  False
  ROST           83.33                6            2.74              4.47        231.55                38.54         0.552            pass              0.182             12.6                           0.188                7.23              1.127                                 ok           False                  False
   AEP           66.67                6            1.81              1.64        128.87                25.33         0.539            pass              0.152             32.6                           0.199               -0.56              0.184                                 ok           False                  False
  REGN           88.24               34            0.51              2.24        626.78                48.81         0.530            pass              0.572             46.6                           0.567              -13.11             -1.305 downtrend_blocked_slope_and_streak           False                  False
  LRCX           90.00               40            0.19              0.42        318.75                56.04         0.524            pass              0.801             94.1                           0.834                7.75              1.175                                 ok           False                  False
  MPWR           94.12               34            0.36              4.08       1618.42                53.62         0.523            pass              0.850             87.1                           0.799               -2.18              0.284           downtrend_blocked_streak           False                  False
   WMT           91.43               35            0.42              0.35        118.39                34.18         0.505            pass              0.559             12.3                           0.159              -10.22             -1.454 downtrend_blocked_slope_and_streak           False                  False
  NVDA           90.00               40            0.10              0.14        212.54                40.71         0.494 below_threshold              0.798             94.0                           0.573               -5.95             -0.847 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-28T11:05:05.990852-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:00:06.281016-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:55:05.933793-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:50:05.877302-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:45:02.890829-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:40:06.973903-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:35:04.979836-04:00 early_entry_1035 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:30:05.932623-04:00 early_entry_1030 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:25:06.392243-04:00 early_entry_1025 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:20:03.857163-04:00 early_entry_1020 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528110505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528110505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528110505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528110505)

</details>
