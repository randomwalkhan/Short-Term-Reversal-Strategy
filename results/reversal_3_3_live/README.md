# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 11:20:04 EDT`
Last processed slot: `manage_1130`

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
- Equity: `$31,054.25`
- Realized PnL: `$20,384.25`
- Unrealized PnL: `$670.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-28                   0      4     12500.0                 13170.0        31.25          32.92      419.65        423.01          bid_ask_mid                      32.92                bid_ask_mid                    True           670.0                   5.36         89.19               37              0.52         51.04            50.0                  36.99                2631.0           27.0               0.06                      ok
```

## Today's Closed Trades (2026-05-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260717C00500000      2          2026-05-27         2026-05-28        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN           88.89               27            0.52              1.23        335.53                27.08         0.522          pass              0.461             19.5                           0.125                0.11              0.210                                 ok            True                  False
  MNST           91.67               36            0.53              0.33         89.10                49.17         0.507          pass              0.720             61.7                           0.536                3.30              0.263                                 ok            True                  False
   CEG           80.56               36            0.76              1.53        288.03                55.24         0.502          pass              0.468             76.7                           0.594                4.39              0.998                                 ok            True                  False
    ZS           85.29               34            1.22              1.08        125.95               152.21         0.820          pass              0.570             62.3                           0.619              -18.08             -1.189            downtrend_blocked_slope           False                  False
  INTC           97.30               37            0.31              0.27        121.66                92.16         0.638          pass              0.923             93.1                           0.922                0.91              0.814                                 ok           False                  False
  CSCO           94.29               35            0.26              0.22        119.58                51.65         0.599          pass              0.853             81.9                           0.687               17.17              0.896                                 ok           False                  False
   XEL          100.00                8            1.84              1.04         80.55                25.49         0.575          pass              0.501             14.4                           0.221               -0.50              0.193                                 ok           False                  False
  ROST           83.33                6            2.39              3.91        231.80                38.54         0.574          pass              0.217             23.7                           0.449                7.62              1.143                                 ok           False                  False
   AEP           66.67                6            1.76              1.60        128.89                25.33         0.542          pass              0.157             34.3                           0.207               -0.52              0.186                                 ok           False                  False
  MPWR           94.12               34            0.13              1.43       1619.56                53.62         0.539          pass              0.877             95.5                           0.939               -1.95              0.294           downtrend_blocked_streak           False                  False
   WMT           92.59               27            0.74              0.61        118.28                34.18         0.538          pass              0.515              4.2                           0.161              -10.50             -1.468 downtrend_blocked_slope_and_streak           False                  False
  REGN           88.24               34            0.61              2.67        626.59                48.81         0.523          pass              0.541             36.2                           0.399              -13.20             -1.309 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-28T11:20:04.888168-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:15:02.993197-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:10:05.974897-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:05:05.990852-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:00:06.281016-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:55:05.933793-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:50:05.877302-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:45:02.890829-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:40:06.973903-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:35:04.979836-04:00 early_entry_1035 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528112004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528112004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528112004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528112004)

</details>
