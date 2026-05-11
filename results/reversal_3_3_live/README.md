# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 10:18:18 EDT`
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
- Equity: `$31,468.50`
- Realized PnL: `$22,833.50`
- Unrealized PnL: `$-1,365.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG260618C00290000       2026-05-11                   0      7     16240.0                 14875.0         23.2          21.25      301.86        300.36         -1365.0                  -8.41         89.74               39              0.58         46.89           42.78                  48.41                 991.0           18.0               0.15                      ok
```

## Today's Closed Trades (2026-05-11)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           80.00               35            0.77              1.60        294.07                87.07         0.700          pass              0.354             39.2                           0.209               23.47              1.915                                 ok            True                  False
  TEAM           84.21               19            4.12              2.64         90.47               114.36         0.639          pass              0.251              4.9                           0.070               26.88              3.317                                 ok            True                  False
  GOOG           86.36               22            1.39              3.86        395.39                37.66         0.563          pass              0.407             33.8                           0.390               12.34              1.431                                 ok            True                  False
  TMUS           86.21               29            0.79              1.06        193.17                36.59         0.541          pass              0.479             44.1                           0.552                5.12              0.274                                 ok            True                  False
    ZS           83.33               36            1.03              1.10        151.66                58.64         0.540          pass              0.408             30.5                           0.268               12.27              1.395                                 ok            True                  False
   WMT           84.62               13            1.36              1.25        129.90                19.38         0.533          pass              0.209              4.3                           0.130                1.02              0.148                                 ok            True                  False
  MRVL          100.00               29            1.15              1.37        169.54                55.66         0.532          pass              0.804             74.7                           0.792                6.30              0.814                                 ok            True                  False
   ADP           92.00               25            0.92              1.37        212.41                34.95         0.528          pass              0.634             53.8                           0.354                7.00              0.483                                 ok            True                  False
  ASML           84.62               13            3.26             36.32       1576.46                48.89         0.507          pass              0.224             10.0                           0.219                7.52              1.206                                 ok            True                  False
  CHTR           85.00               20            2.14              2.32        153.87               119.48         0.788          pass              0.406             42.5                           0.729              -13.21             -1.194            downtrend_blocked_slope           False                  False
 CMCSA           92.11               38            0.04              0.01         25.39                62.19         0.649          pass              0.862             95.9                           0.729               -7.72             -0.792 downtrend_blocked_slope_and_streak           False                  False
  FTNT           96.00               50            0.04              0.03        114.06                70.49         0.572          pass              0.952             98.4                           0.651               33.10              3.111                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-05-11T10:18:18.755092-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:12:01.604493-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:05:43.962541-04:00 early_entry_1005         entry {"allocated_cash": 16240.0, "asset_type": "option", "contract_symbol": "CEG260618C00290000", "contracts": 7, "early_entry_score": 0.766, "entry_mode": "early", "entry_option_price": 23.2, "execution_mode": "option", "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 991.0, "option_spread_pct": 14.66, "option_volume": 18.0, "success_rate": 89.74, "ticker": "CEG", "timing_score": 0.357}
2026-05-11T09:18:42.943466-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                    {'saved': 92}
2026-05-08T16:05:06.142170-04:00      manage_1600          exit                                                                                                                                                                                                                                           {"asset_type": "option", "contract_symbol": "TEAM260618C00090000", "fill_price": 9.25, "pnl": 2850.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 19.35, "ticker": "TEAM"}
2026-05-08T16:00:06.094263-04:00      manage_1600  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:55:02.084715-04:00      manage_1600  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:40:02.063692-04:00      manage_1530  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:35:05.923584-04:00      manage_1530  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:30:06.082521-04:00      manage_1530  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511101818)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511101818)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511101818)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511101818)

</details>
