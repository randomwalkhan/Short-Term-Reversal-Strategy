# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-27 09:55:04 EDT`
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
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$8,255.50`
- Equity: `$13,815.50`
- Realized PnL: `$4,045.50`
- Unrealized PnL: `$-230.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260618C00280000       2026-04-24                   1      4      5790.0                  5560.0        14.48           13.9      276.91        272.78          -230.0                  -3.97         80.95               21              1.88         37.37            1.56                  66.99                1259.0          219.0               0.04                      ok
```

## Today's Closed Trades (2026-04-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CHTR           92.31               39            0.73              0.92        179.74               113.10            True
   KDP           82.35               17            1.27              0.26         29.11                32.43            True
  TEAM           80.00               45            0.81              0.41         71.38                79.96            True
  KLAC           86.36               22            2.07             28.00       1923.00                47.17            True
  SNPS           86.67               30            1.48              5.18        498.60                54.04            True
  AVGO           91.67               36            0.72              2.12        421.85                42.01            True
   TXN           79.17               24            1.58              3.07        275.85                67.06           False
  UPRO           92.86               42            0.09              0.08        126.96                48.54           False
  NFLX           93.33               45            0.12              0.08         92.32                45.93           False
  SHOP           95.45               44            0.34              0.30        125.70                57.21           False
  ASML           79.17               24            1.97             20.11       1449.08                51.44           False
  CSCO           86.67               30            0.33              0.20         88.92                28.51           False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-04-27T09:55:04.282451-04:00    manage_1000  slot_skipped             {"reason": "already_processed"}
2026-04-27T09:40:04.365918-04:00    manage_0930  slot_skipped             {"reason": "already_processed"}
2026-04-27T09:35:01.383848-04:00    manage_0930  slot_skipped             {"reason": "already_processed"}
2026-04-27T09:30:01.445280-04:00    manage_0930  slot_skipped             {"reason": "already_processed"}
2026-04-27T09:25:03.410352-04:00    manage_0930  slot_skipped             {"reason": "already_processed"}
2026-04-27T02:43:32.046615-04:00 share_ext_0240  slot_skipped             {"reason": "already_processed"}
2026-04-27T02:42:00.592151-04:00   data_refresh  data_refresh                               {'saved': 99}
2026-04-25T02:55:07.078802-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-25T02:50:02.210894-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-04-25T02:45:02.731724-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260427095504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260427095504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260427095504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260427095504)

</details>
