# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 15:35:01 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$4,915.25`
- Equity: `$26,840.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$-155.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL260821C00315000       2026-07-14                   0     11     12705.0                 12980.0        11.55          11.80      315.21        315.38          bid_ask_mid                      11.80                bid_ask_mid                    True           275.0                   2.16         95.83               24              0.66         28.20           28.53                  35.57               11042.0         1070.0               0.02                      ok
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  8945.0        46.88          44.72      660.72        659.12          bid_ask_mid                      44.72                bid_ask_mid                    True          -430.0                  -4.59         81.82               22              1.27         53.38           52.62                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AAPL           96.00               25            0.62              1.37        316.72                35.57         0.586          pass              0.770             70.4                           0.644               11.93              1.125                                 ok            True                  False
  GILD           89.47               19            1.04              0.95        130.99                32.97         0.568          pass              0.463             31.3                           0.207                2.94              0.405                                 ok            True                  False
  AMGN           92.86               14            1.32              3.32        359.03                21.45         0.558          pass              0.477             17.2                           0.256               -1.35             -0.096                                 ok            True                  False
  CSCO           90.00               10            1.88              1.57        118.58                35.64         0.556          pass              0.372             16.5                           0.455               -0.22              0.228                                 ok            True                  False
  PYPL           80.95               21            1.10              0.37         47.49                33.27         0.541          pass              0.324             57.0                           0.628                6.19              0.671                                 ok            True                  False
  PAYX          100.00               24            1.01              0.78        110.41                31.82         0.539          pass              0.768             73.6                           0.517                9.84              0.945                                 ok            True                  False
   KHC           88.89                9            0.73              0.13         25.17                36.18         0.675          pass              0.478             57.8                           0.635                3.53              0.341                                 ok           False                  False
  MDLZ          100.00                3            1.77              0.74         59.54                31.17         0.639          pass              0.497             10.9                           0.328               -1.42              0.006                                 ok           False                  False
   ADP          100.00                7            1.95              3.43        249.58                31.20         0.585          pass              0.591             44.3                           0.434                9.42              0.829                                 ok           False                  False
   PEP           85.71                7            1.95              1.89        137.68                30.22         0.583          pass              0.228              5.9                           0.268               -2.08             -0.145                                 ok           False                  False
   KDP           75.00                4            2.64              0.58         31.00                34.17         0.558          pass              0.075              6.2                           0.315               -9.18             -0.836 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00               26            0.30              0.17         80.41                22.03         0.553          pass              0.739             59.2                           0.490               -2.13             -0.133                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-07-14T15:10:01.456053-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-14T15:05:02.308534-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-14T15:00:04.423415-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-14T14:55:01.276896-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-14T14:50:02.479277-04:00       entry_1500              entry {"allocated_cash": 12705.0, "asset_type": "option", "contract_symbol": "AAPL260821C00315000", "contracts": 11, "early_entry_score": 0.757, "entry_mode": "regular", "entry_option_price": 11.55, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 11042.0, "option_spread_pct": 1.73, "option_volume": 1070.0, "success_rate": 95.83, "ticker": "AAPL", "timing_score": 0.589}
2026-07-14T14:50:02.479277-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-14", "training_samples": 5400, "window": 5}
2026-07-14T12:00:02.352813-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:55:01.322008-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:50:02.227286-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:45:01.430125-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714153501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714153501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714153501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714153501)

</details>
