# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 09:40:05 EDT`
Last processed slot: `manage_0930`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
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

- Cash: `$14,483.50`
- Equity: `$27,563.50`
- Realized PnL: `$17,583.50`
- Unrealized PnL: `$-20.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260618C00290000       2026-05-07                   1     10     13100.0                 13080.0         13.1          13.08      283.62        288.77           -20.0                  -0.15         91.67               12              2.01         41.87             0.2                  67.07                1293.0          214.0               0.05                      ok
```

## Today's Closed Trades (2026-05-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  SNPS           97.37               38            0.52              1.85        504.40                49.11         0.552          pass                0.34              0.283                                 ok            True
   ADP           91.67               12            2.26              3.39        212.64                38.09         0.520          pass                6.47              0.650                                 ok            True
  CDNS           97.37               38            0.74              1.85        356.11                51.38         0.511          pass                6.42              0.913                                 ok            True
  CRWD           81.82               22            2.12              7.52        502.52                48.11         0.504          pass               10.46              1.058                                 ok            True
  CHTR           90.20               51            0.05              0.06        160.21               119.32         0.765          pass              -11.09             -1.125            downtrend_blocked_slope           False
 CMCSA           88.46               26            0.63              0.12         26.19                61.43         0.678          pass               -5.39             -0.564 downtrend_blocked_slope_and_streak           False
  MSTR           90.24               41            0.27              0.34        179.70                69.89         0.599          pass                4.88              1.164                                 ok           False
  SHOP           86.36               22            2.82              2.21        110.79                82.33         0.592          pass              -13.71             -1.624 downtrend_blocked_slope_and_streak           False
  FTNT           95.83               48            0.25              0.19        107.89                73.38         0.583          pass               27.70              2.214                                 ok           False
  FAST           96.67               30            0.41              0.13         44.31                33.68         0.546          pass               -0.61             -0.057                                 ok           False
  TEAM           66.67                6            6.64              4.29         90.53               115.49         0.524          pass               20.52              3.327                                 ok           False
  PYPL           94.29               35            0.56              0.18         46.14                42.03         0.519          pass               -8.95             -1.049 downtrend_blocked_slope_and_streak           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-05-08T09:40:05.918205-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T09:35:06.024595-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T09:30:04.090136-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T09:25:02.109177-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T00:00:05.874567-04:00 data_refresh data_refresh                   {'saved': 92}
2026-05-07T16:10:04.394572-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-05-07T16:05:04.301944-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-05-07T16:00:08.945090-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-05-07T15:55:05.013610-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-05-07T15:40:04.301487-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508094005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508094005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508094005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508094005)

</details>
