# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 11:35:03 EDT`
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
- Equity: `$31,974.25`
- Realized PnL: `$20,384.25`
- Unrealized PnL: `$1,590.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-28                   0      4     12500.0                 14090.0        31.25          35.22      419.65        424.48          bid_ask_mid                      35.22                bid_ask_mid                    True          1590.0                  12.72         89.19               37              0.52         51.04           52.12                  36.99                2631.0           27.0               0.06                      ok
```

## Today's Closed Trades (2026-05-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260717C00500000      2          2026-05-27         2026-05-28        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           92.86               28            0.53              0.44        119.48                51.65         0.626            pass              0.715             63.2                           0.468               16.85              0.884                                 ok            True                  False
  MNST           89.66               29            0.78              0.49         89.03                49.17         0.537            pass              0.570             44.0                           0.303                3.04              0.252                                 ok            True                  False
   CEG           82.05               39            0.52              1.05        288.23                55.24         0.500 below_threshold              0.550             84.0                           0.748                4.64              1.008                                 ok            True                  False
  INTC           97.50               40            0.17              0.15        121.71                92.16         0.628            pass              0.951             96.2                           0.943                1.06              0.821                                 ok           False                  False
   XEL          100.00                7            2.06              1.17         80.50                25.49         0.566            pass              0.468              4.0                           0.179               -0.73              0.182                                 ok           False                  False
  ROST           83.33                6            2.57              4.21        231.67                38.54         0.562            pass              0.198             17.8                           0.402                7.41              1.135                                 ok           False                  False
   WMT           91.67               24            0.81              0.67        118.25                34.18         0.551            pass              0.521             20.7                           0.220              -10.57             -1.472 downtrend_blocked_slope_and_streak           False                  False
   AEP           66.67                6            1.68              1.53        128.92                25.33         0.548            pass              0.166             37.2                           0.398               -0.44              0.190                                 ok           False                  False
  REGN           88.24               34            0.55              2.42        626.70                48.81         0.527            pass              0.559             42.2                           0.472              -13.15             -1.306 downtrend_blocked_slope_and_streak           False                  False
  AMGN           89.29               28            0.49              1.16        335.56                27.08         0.518            pass              0.491             23.9                           0.151                0.14              0.211                                 ok           False                  False
  KLAC           89.47               38            0.10              1.36       1956.61                51.91         0.509            pass              0.781             97.1                           0.878                5.84              0.867                                 ok           False                  False
  CHTR           88.10               42            0.39              0.40        147.01                56.79         0.487 below_threshold              0.667             67.5                           0.379                2.48              0.251                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-28T11:35:03.979729-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:30:01.953912-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:25:06.570222-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:20:04.888168-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:15:02.993197-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:10:05.974897-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:05:05.990852-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T11:00:06.281016-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:55:05.933793-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-28T10:50:05.877302-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528113503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528113503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528113503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528113503)

</details>
