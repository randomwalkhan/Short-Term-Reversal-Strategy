# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-14 12:05:06 EDT`
Last processed slot: `manage_1200`

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
- Equity: `$13,269.48`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$124.48`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-13                   1      8      5916.0                 6040.48        739.5         755.06       739.5        755.06          124.48                    2.1         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               16            1.58              2.09        188.20                30.53            True
  INTC           94.44               18            3.78              1.72         64.46                75.15            True
  COST           94.44               18            0.99              6.82        977.93                19.04            True
  MPWR           91.18               34            0.92              8.88       1368.43                58.48            True
  CSCO           82.35               17            0.98              0.56         82.11                28.38            True
  CRWD           81.40               43            0.77              2.16        401.31                60.69            True
  TMUS           81.25               16            1.53              2.07        191.54                20.34            True
  PANW           80.00               40            0.92              1.04        162.09                56.05            True
   HON          100.00               33            0.27              0.43        233.45                23.77           False
   LIN          100.00                4            2.12              7.54        505.64                18.23           False
  FTNT           95.65               46            0.41              0.22         78.64                38.32           False
  VRTX           91.67               48            0.06              0.18        439.97                27.59           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-14T12:05:06.429215-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-14T12:00:03.430403-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-14T11:55:05.428677-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-14T11:40:02.417003-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-14T11:35:06.429798-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-14T11:30:06.437791-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-14T11:25:05.423389-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-14T11:10:06.425817-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-14T11:05:06.519402-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-14T11:00:06.430912-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260414120506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260414120506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260414120506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260414120506)

</details>
