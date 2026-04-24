# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-24 10:10:06 EDT`
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

- Cash: `$6,808.00`
- Equity: `$14,158.00`
- Realized PnL: `$2,970.50`
- Unrealized PnL: `$1,187.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  NVDA     option         option NVDA260618C00200000       2026-04-23                   1      5      6162.5                  7350.0        12.32           14.7      198.79        202.76          1187.5                  19.27         95.24               21              1.83          41.3           42.55                  33.17              111167.0         4613.0                0.0                      ok
```

## Today's Closed Trades (2026-04-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   TXN           83.33               12            2.36              4.66        280.23                66.99            True
  PLTR           89.74               39            0.66              0.65        141.29                64.15            True
  CSCO           84.00               25            0.52              0.33         88.45                28.51            True
   WMT           90.00               20            1.11              1.03        131.59                24.33            True
  FAST           90.62               32            0.79              0.25         45.34                38.70            True
  DDOG           86.21               29            1.77              1.59        127.18                60.38            True
   CSX           88.00               25            0.69              0.22         46.08                27.21            True
   APP           84.38               32            1.73              5.51        451.81                77.03            True
   HON          100.00               12            1.57              2.35        213.33                25.71            True
  MRVL           96.30               27            1.86              2.16        164.64                67.12            True
  MSTR           81.40               43            0.20              0.24        172.37                74.46           False
  CRWD           79.49               39            0.92              2.88        444.15                59.30           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-24T10:10:06.140592-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-24T10:05:05.170858-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-24T10:00:03.243449-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-24T09:55:04.947426-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-24T09:40:04.006761-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-24T09:35:05.002033-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-24T09:30:01.163194-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-24T09:25:04.324323-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T16:10:01.709855-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-23T16:05:01.797986-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260424101006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260424101006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260424101006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260424101006)

</details>
