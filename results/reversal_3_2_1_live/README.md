# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-14 10:40:06 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$7,229.00`
- Equity: `$13,236.24`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$91.24`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-13                   1      8      5916.0                 6007.24        739.5         750.91       739.5        750.91           91.24                   1.54         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               13            2.15              2.85        187.88                30.53            True
  INTC           95.24               21            3.41              1.56         64.53                75.15            True
  COST           93.33               15            1.05              7.23        977.75                19.04            True
   WMT           93.10               29            0.73              0.64        124.29                26.19            True
  MPWR           91.43               35            0.74              7.08       1369.20                58.48            True
  PCAR           90.00               40            0.57              0.51        127.16                27.21            True
  AMAT           86.84               38            0.52              1.44        395.11                56.21            True
   TXN           85.29               34            0.63              0.96        216.30                31.51            True
  TMUS           83.87               31            0.67              0.90        192.04                20.34            True
  WDAY           82.05               39            1.23              1.04        119.48                50.72            True
  PANW           80.95               42            0.61              0.69        162.24                56.05            True
   BKR           80.77               26            1.01              0.44         62.37                33.24            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-14T10:40:06.436642-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-14T10:35:06.425929-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-14T10:30:06.433815-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-14T10:25:06.434099-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-14T10:10:06.430685-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-14T10:05:06.431814-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-14T10:00:05.413958-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-14T09:55:02.016600-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-14T09:40:06.426052-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-14T09:35:06.430444-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260414104006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260414104006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260414104006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260414104006)

</details>
