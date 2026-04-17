# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-17 11:40:00 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$6,636.99`
- Equity: `$13,364.67`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$6.75`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   1      9     6720.93                 6727.68       746.77         747.52      746.77        747.52            6.75                    0.1         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FTNT           95.00               40            0.84              0.48         82.19                40.09            True
   LIN           92.31               13            1.38              4.82        497.15                18.78            True
   XEL           91.67               12            0.97              0.55         80.81                23.12            True
  WDAY           80.00               40            1.21              1.06        124.42                54.23            True
  FANG          100.00                1            6.90              9.02        182.79                29.20           False
   EXC          100.00                1            2.96              0.99         47.17                21.57           False
  GILD           90.91               33            0.40              0.39        138.39                20.76           False
   ROP           89.58               48            0.11              0.27        361.76                23.28           False
   AEP           88.89                9            1.24              1.17        134.06                17.62           False
   PEP           86.67               30            0.31              0.35        158.23                20.28           False
  ALNY           85.71                7            3.13              7.01        317.12                45.49           False
   AMD           85.00               40            0.40              0.78        277.92                54.30           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-17T11:40:00.700868-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:35:02.708343-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:30:05.729176-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:25:05.895658-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-17T11:10:00.820702-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-17T11:05:05.725954-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-17T11:00:05.702303-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-17T10:55:03.851293-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-17T10:40:05.810155-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-17T10:35:05.687840-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260417114000)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260417114000)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260417114000)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260417114000)

</details>
