# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-27 10:05:01 EDT`
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
- Equity: `$13,465.50`
- Realized PnL: `$4,045.50`
- Unrealized PnL: `$-580.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260618C00280000       2026-04-24                   1      4      5790.0                  5210.0        14.48          13.02      276.91        271.02          -580.0                 -10.02         80.95               21              1.88         37.37           43.41                  66.99                1259.0          219.0               0.04                      ok
```

## Today's Closed Trades (2026-04-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   KDP           81.25               16            1.44              0.29         29.09                32.43            True
  TEAM           81.25               48            0.70              0.35         71.40                79.96            True
  KLAC           83.33               24            1.84             24.88       1924.34                47.17            True
  AAPL           84.21               19            1.37              2.60        269.94                26.22            True
  SNPS           89.66               29            1.62              5.67        498.39                54.04            True
  SHOP           95.12               41            0.89              0.78        125.49                57.21            True
   MAR           89.29               28            0.98              2.52        366.07                31.82            True
   TXN           78.57               14            2.22              4.31        275.32                67.06           False
  CHTR           92.86               42            0.49              0.62        179.86               113.10           False
  MSTR           83.33               42            0.27              0.32        170.88                71.85           False
  NFLX           93.02               43            0.34              0.22         92.26                45.93           False
  ASML           79.17               24            1.83             18.68       1449.70                51.44           False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-04-27T10:05:01.450003-04:00    manage_1000  slot_skipped             {"reason": "already_processed"}
2026-04-27T10:00:06.086949-04:00    manage_1000  slot_skipped             {"reason": "already_processed"}
2026-04-27T09:55:04.282451-04:00    manage_1000  slot_skipped             {"reason": "already_processed"}
2026-04-27T09:40:04.365918-04:00    manage_0930  slot_skipped             {"reason": "already_processed"}
2026-04-27T09:35:01.383848-04:00    manage_0930  slot_skipped             {"reason": "already_processed"}
2026-04-27T09:30:01.445280-04:00    manage_0930  slot_skipped             {"reason": "already_processed"}
2026-04-27T09:25:03.410352-04:00    manage_0930  slot_skipped             {"reason": "already_processed"}
2026-04-27T02:43:32.046615-04:00 share_ext_0240  slot_skipped             {"reason": "already_processed"}
2026-04-27T02:42:00.592151-04:00   data_refresh  data_refresh                               {'saved': 99}
2026-04-25T02:55:07.078802-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260427100501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260427100501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260427100501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260427100501)

</details>
