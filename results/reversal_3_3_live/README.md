# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-13 15:45:04 EDT`
Last processed slot: `manual`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
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

- Cash: `$17,620.25`
- Equity: `$27,105.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$110.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   0      2      9375.0                  9485.0        46.88          47.42      660.72        657.15          bid_ask_mid                      47.42                bid_ask_mid                    True           110.0                   1.17         81.82               22              1.27         53.38           56.26                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ADI           82.35               17            2.34              6.47        392.88                55.18         0.572          pass              0.248             27.2                           0.557               -1.37             -0.034                                 ok            True                  False
  UPRO           90.00               10            2.50              2.56        145.06                40.56         0.566          pass              0.350              9.0                           0.190                2.70              0.328                                 ok            True                  False
  CSCO           90.91               11            1.78              1.51        120.66                35.64         0.556          pass              0.494             46.8                           0.322                1.61              0.311                                 ok            True                  False
   LIN          100.00               12            1.22              4.53        527.85                20.88         0.554          pass              0.535             22.1                           0.347                2.40              0.042                                 ok            True                  False
  ROST           84.21               19            1.35              2.11        221.97                30.69         0.535          pass              0.273             15.6                           0.215                5.28              0.649                                 ok            True                  False
  ABNB           93.33               15            2.08              2.16        147.69                37.12         0.527          pass              0.550             36.0                           0.436               -1.11             -0.020                                 ok            True                  False
  GOOG           85.71               28            1.22              3.04        353.73                33.22         0.513          pass              0.344              6.7                           0.183               -0.17             -0.035                                 ok            True                  False
 GOOGL           82.76               29            1.17              2.94        355.92                32.16         0.502          pass              0.267              5.5                           0.168               -0.19             -0.063                                 ok            True                  False
  KLAC           75.00               12            4.15              6.73        228.64               110.61         0.642          pass              0.149             23.9                           0.555              -20.29             -2.597 downtrend_blocked_slope_and_streak           False                  False
    MU           80.00               15            4.74             32.52        965.36               112.95         0.601          pass              0.212             39.4                           0.566              -18.54             -1.880            downtrend_blocked_slope           False                  False
   KDP           81.82               11            1.14              0.25         31.56                34.17         0.598          pass              0.148             11.1                           0.219               -6.54             -0.706 downtrend_blocked_slope_and_streak           False                  False
   WDC           92.31               13            5.69             23.20        572.64               121.29         0.587          pass              0.510             34.3                           0.496              -15.71             -1.361            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-13T15:10:07.483451-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-13T15:05:06.913203-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-13T15:00:09.058779-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-13T14:55:09.246495-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-13T14:50:06.804809-04:00       entry_1500              entry {"allocated_cash": 9375.0, "asset_type": "option", "contract_symbol": "META260821C00660000", "contracts": 2, "early_entry_score": 0.317, "entry_mode": "regular", "entry_option_price": 46.875, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 7322.0, "option_spread_pct": 2.03, "option_volume": 1343.0, "success_rate": 81.82, "ticker": "META", "timing_score": 0.583}
2026-07-13T14:50:06.804809-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-13", "training_samples": 5399, "window": 5}
2026-07-13T12:00:04.108537-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:55:01.971433-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:50:06.106391-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:35:02.081051-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260713154504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260713154504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260713154504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260713154504)

</details>
