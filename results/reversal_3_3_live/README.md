# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 09:55:06 EDT`
Last processed slot: `manage_1000`

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
   TXN     option         option TXN260618C00290000       2026-05-07                   1     10     13100.0                 13080.0         13.1          13.08      283.62        290.02           -20.0                  -0.15         91.67               12              2.01         41.87             0.0                  67.07                1293.0          214.0               0.05                      ok
```

## Today's Closed Trades (2026-05-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  FTNT           94.29               35            0.86              0.65        107.69                73.38         0.622          pass               26.91              2.186                                 ok            True
  MSTR           90.00               40            0.81              1.02        179.40                69.89         0.574          pass                4.31              1.139                                 ok            True
  CRWD           81.82               22            1.85              6.55        502.93                48.11         0.514          pass               10.77              1.071                                 ok            True
  CDNS           97.22               36            1.03              2.58        355.79                51.38         0.506          pass                6.10              0.900                                 ok            True
   ADP           91.67               12            2.55              3.83        212.45                38.09         0.500          pass                6.15              0.637                                 ok            True
  CHTR           84.62               26            1.69              1.90        159.43               119.32         0.787          pass              -12.55             -1.200            downtrend_blocked_slope           False
 CMCSA           90.00               10            1.39              0.26         26.13                61.43         0.719          pass               -6.11             -0.599 downtrend_blocked_slope_and_streak           False
  SHOP           87.50               24            2.41              1.88        110.93                82.33         0.599          pass              -13.34             -1.605 downtrend_blocked_slope_and_streak           False
  SNPS           97.50               40            0.45              1.61        504.50                49.11         0.544          pass                0.41              0.287                                 ok           False
  FAST           96.97               33            0.27              0.08         44.32                33.68         0.537          pass               -0.48             -0.051                                 ok           False
  NFLX           87.88               33            0.94              0.58         88.01                43.15         0.537          pass               -5.42             -0.611            downtrend_blocked_slope           False
  PYPL           92.59               27            1.15              0.37         46.06                42.03         0.531          pass               -9.49             -1.076 downtrend_blocked_slope_and_streak           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-05-08T09:55:06.107419-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-08T09:40:05.918205-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T09:35:06.024595-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T09:30:04.090136-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T09:25:02.109177-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T00:00:05.874567-04:00 data_refresh data_refresh                   {'saved': 92}
2026-05-07T16:10:04.394572-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-05-07T16:05:04.301944-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-05-07T16:00:08.945090-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-05-07T15:55:05.013610-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508095506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508095506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508095506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508095506)

</details>
