# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-24 09:55:04 EDT`
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
- Equity: `$13,133.00`
- Realized PnL: `$2,970.50`
- Unrealized PnL: `$162.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  NVDA     option         option NVDA260618C00200000       2026-04-23                   1      5      6162.5                  6325.0        12.32          12.65      198.79        201.22           162.5                   2.64         95.24               21              1.83          41.3             0.0                  33.17              111167.0         4613.0                0.0                      ok
```

## Today's Closed Trades (2026-04-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   TXN           83.33               12            2.29              4.53        280.29                66.99            True
   WDC           97.44               39            0.57              1.61        402.43                71.37            True
   APP           84.21               38            0.89              2.81        452.96                77.03            True
  DDOG           84.38               32            1.21              1.09        127.39                60.38            True
  CSCO           84.00               25            0.55              0.34         88.44                28.51            True
  SBUX           90.00               20            1.28              0.89         99.16                31.25            True
  PLTR           89.47               38            0.91              0.90        141.18                64.15            True
   ADI           81.25               32            0.71              2.01        403.02                40.58            True
   HON          100.00               14            1.35              2.03        213.47                25.71            True
  AVGO           86.67               15            2.54              7.48        416.74                44.94            True
  ISRG           85.00               20            1.59              5.31        476.54                37.68            True
  CRWD           81.40               43            0.35              1.11        444.92                59.30           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-24T09:55:04.947426-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-24T09:40:04.006761-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-24T09:35:05.002033-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-24T09:30:01.163194-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-24T09:25:04.324323-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T16:10:01.709855-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-23T16:05:01.797986-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-23T16:00:04.974935-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-23T15:55:05.889210-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-23T15:50:06.563469-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260424095504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260424095504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260424095504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260424095504)

</details>
