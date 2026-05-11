# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 10:30:53 EDT`
Last processed slot: `manage_1030`

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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$16,593.50`
- Equity: `$34,443.50`
- Realized PnL: `$22,833.50`
- Unrealized PnL: `$1,610.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG260618C00290000       2026-05-11                   0      7     16240.0                 17850.0         23.2           25.5      301.86        301.38          1610.0                   9.91         89.74               39              0.58         46.89           52.61                  48.41                 991.0           18.0               0.15                      ok
```

## Today's Closed Trades (2026-05-11)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  NXPI           80.00               35            0.76              1.56        294.08                87.07         0.701          pass              0.358             40.5                           0.257               23.49              1.916                      ok            True                  False
  TEAM           83.33               12            5.07              3.25         90.21               114.36         0.618          pass              0.168              1.3                           0.154               25.63              3.272                      ok            True                  False
  GOOG           80.00               10            1.86              5.17        394.83                37.66         0.598          pass              0.094             11.4                           0.124               11.80              1.409                      ok            True                  False
  MSTR           89.74               39            0.57              0.75        187.27                70.10         0.578          pass              0.750             79.7                           0.621               10.24              1.513                      ok            True                   True
    ZS           82.14               28            1.64              1.74        151.38                58.64         0.549          pass              0.244              3.9                           0.085               11.58              1.367                      ok            True                  False
  MRVL          100.00               24            1.61              1.91        169.31                55.66         0.536          pass              0.741             64.7                           0.735                5.81              0.792                      ok            True                  False
   WMT           88.89               18            1.03              0.94        130.03                19.38         0.525          pass              0.443             33.5                           0.330                1.36              0.163                      ok            True                  False
  FAST           92.86               14            1.61              0.50         43.96                33.60         0.521          pass              0.510             29.4                           0.368               -3.51             -0.185                      ok            True                  False
   ADI           81.82               33            0.52              1.51        415.87                36.03         0.515          pass              0.425             57.3                           0.441                5.55              0.755                      ok            True                  False
  CHTR           91.67               36            1.01              1.10        154.39               119.48         0.776          pass              0.781             72.8                           0.877              -12.21             -1.142 downtrend_blocked_slope           False                  False
  INTC          100.00               41            0.19              0.16        124.82               104.20         0.639          pass              0.882             72.8                           0.462               46.68              3.960                      ok           False                  False
  SHOP           92.31               13            4.13              3.20        109.14                82.28         0.585          pass              0.449             14.1                           0.263              -14.72             -1.719 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-05-11T10:30:53.059924-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:24:36.025323-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:18:18.755092-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:12:01.604493-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:05:43.962541-04:00 early_entry_1005         entry {"allocated_cash": 16240.0, "asset_type": "option", "contract_symbol": "CEG260618C00290000", "contracts": 7, "early_entry_score": 0.766, "entry_mode": "early", "entry_option_price": 23.2, "execution_mode": "option", "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 991.0, "option_spread_pct": 14.66, "option_volume": 18.0, "success_rate": 89.74, "ticker": "CEG", "timing_score": 0.357}
2026-05-11T09:18:42.943466-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                    {'saved': 92}
2026-05-08T16:05:06.142170-04:00      manage_1600          exit                                                                                                                                                                                                                                           {"asset_type": "option", "contract_symbol": "TEAM260618C00090000", "fill_price": 9.25, "pnl": 2850.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 19.35, "ticker": "TEAM"}
2026-05-08T16:00:06.094263-04:00      manage_1600  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:55:02.084715-04:00      manage_1600  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:40:02.063692-04:00      manage_1530  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511103053)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511103053)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511103053)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511103053)

</details>
