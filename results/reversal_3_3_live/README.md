# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 15:55:01 EDT`
Last processed slot: `manage_1600`

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
- Equity: `$27,157.75`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$162.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL260821C00315000       2026-07-14                   0     11     12705.0                 13007.5        11.55          11.82      315.21        314.80          bid_ask_mid                      11.82                bid_ask_mid                    True           302.5                   2.38         95.83               24              0.66         28.20           29.24                  35.57               11042.0         1070.0               0.02                      ok
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  9235.0        46.88          46.18      660.72        659.89          bid_ask_mid                      46.18                bid_ask_mid                    True          -140.0                  -1.49         81.82               22              1.27         53.38           53.88                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   KHC           84.62               13            0.55              0.10         25.19                36.18         0.656          pass              0.413             68.0                           0.684                3.72              0.349                      ok            True                  False
  AAPL           95.45               22            0.83              1.84        316.52                35.57         0.592          pass              0.720             60.3                           0.506               11.69              1.116                      ok            True                  False
  CSCO           91.67               12            1.63              1.36        118.67                35.64         0.561          pass              0.464             27.9                           0.500                0.04              0.240                      ok            True                  False
  AMGN           92.86               14            1.28              3.24        359.06                21.45         0.560          pass              0.483             19.3                           0.274               -1.31             -0.094                      ok            True                  False
  GILD           86.36               22            0.87              0.80        131.06                32.97         0.555          pass              0.432             42.4                           0.381                3.11              0.413                      ok            True                  False
  PAYX          100.00               24            1.07              0.83        110.39                31.82         0.535          pass              0.763             72.0                           0.461                9.77              0.942                      ok            True                  False
  PYPL           86.67               30            0.78              0.26         47.54                33.27         0.509          pass              0.571             69.7                           0.712                6.53              0.686                      ok            True                  False
  MDLZ          100.00                4            1.60              0.67         59.57                31.17         0.642          pass              0.523             19.7                           0.277               -1.25              0.014                      ok           False                  False
   PEP           80.00                5            2.04              1.98        137.64                30.22         0.583          pass              0.075              5.5                           0.222               -2.17             -0.150                      ok           False                  False
   ADP          100.00                9            1.81              3.18        249.69                31.20         0.580          pass              0.603             48.3                           0.487                9.57              0.836                      ok           False                  False
   XEL          100.00               27            0.25              0.14         80.42                22.03         0.549          pass              0.768             66.7                           0.450               -2.07             -0.131                      ok           False                  False
  ORLY           54.55               11            1.83              1.12         86.80                37.04         0.541          pass              0.113             17.5                           0.391               -4.97             -0.716 downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714155501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714155501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714155501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714155501)

</details>
