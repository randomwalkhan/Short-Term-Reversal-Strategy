# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-30 10:25:03 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$9,532.50`
- Equity: `$15,897.50`
- Realized PnL: `$6,772.50`
- Unrealized PnL: `$-875.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD260618C00450000       2026-04-29                   1      2      7240.0                  6365.0         36.2          31.83      452.38        439.95          -875.0                 -12.09          85.0               40              0.57         51.94           55.43                   53.3                2047.0          316.0               0.03                      ok
```

## Today's Closed Trades (2026-04-30)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC          100.00               26            2.33              1.55         94.09                91.30            True
  SNPS           96.30               27            1.55              5.23        478.98                50.55            True
  AXON           84.21               38            0.88              2.46        399.49                68.68            True
  CDNS           93.75               16            2.47              5.69        327.51                53.49            True
  ADSK           86.21               29            1.06              1.76        235.12                44.88            True
  TSLA           86.11               36            0.75              1.95        371.96                43.82            True
  NXPI           70.00               20            2.01              4.06        287.51                85.25           False
  WDAY           79.41               34            1.71              1.46        121.80                63.16           False
  INTU           72.22               18            2.88              7.96        391.67                55.07           False
  SHOP           93.55               31            1.39              1.18        120.76                52.79           False
  CRWD           73.33               15            3.22             10.20        448.01                53.11           False
  SBUX           92.68               41            0.22              0.16        105.43                35.05           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-30T10:25:03.253231-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-30T09:30:01.723685-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-30T09:27:16.860657-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-29T16:10:01.130102-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-29T16:05:02.179548-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-29T16:00:04.191833-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-29T15:55:03.440219-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-29T15:40:05.909113-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-29T15:35:01.161957-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-29T15:30:01.150324-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260430102503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260430102503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260430102503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260430102503)

</details>
