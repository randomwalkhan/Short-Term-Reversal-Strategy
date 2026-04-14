# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-14 10:25:06 EDT`
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
- Equity: `$13,227.64`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$82.64`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-13                   1      8      5916.0                 5998.64        739.5         749.83       739.5        749.83           82.64                    1.4         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               11            2.34              3.09        187.77                30.53            True
  INTC           96.00               25            2.85              1.30         64.64                75.15            True
   XEL           91.67               12            0.94              0.53         80.22                20.44            True
  MPWR           91.18               34            1.05             10.11       1367.90                58.48            True
   WMT           90.32               31            0.66              0.57        124.31                26.19            True
  PCAR           90.00               40            0.50              0.45        127.19                27.21            True
  COST           90.00               10            1.19              8.19        977.34                19.04            True
  TMUS           85.19               27            0.77              1.04        191.98                20.34            True
   TXN           84.38               32            0.72              1.10        216.24                31.51            True
  CSCO           83.33               18            0.81              0.47         82.15                28.38            True
  WDAY           81.82               44            0.72              0.60        119.66                50.72            True
  CHTR           81.82               22            2.11              3.35        224.87                32.05            True
```

## Recent Events

```text
                    timestamp_et           slot   event_type                          detail
2026-04-14T10:25:06.434099-04:00    manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-14T10:10:06.430685-04:00    manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-14T10:05:06.431814-04:00    manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-14T10:00:05.413958-04:00    manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-14T09:55:02.016600-04:00    manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-14T09:40:06.426052-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-14T09:35:06.430444-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-14T09:30:06.428322-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-14T09:25:06.428256-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-14T01:39:11.037721-04:00 share_ext_0135 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260414102506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260414102506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260414102506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260414102506)

</details>
