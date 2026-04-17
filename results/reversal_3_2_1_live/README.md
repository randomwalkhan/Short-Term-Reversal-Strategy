# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-17 10:50:05 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$13,395.27`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$37.35`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   1      9     6720.93                 6758.28       746.77         750.92      746.77        750.92           37.35                   0.56         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  ALNY           88.89               27            1.69              3.79        318.51                45.49            True
   LIN           85.71               14            1.31              4.58        497.26                18.78            True
  TEAM           80.56               36            2.49              1.20         68.22                72.52            True
  FANG          100.00                1            8.42             11.00        181.93                29.20           False
   EXC          100.00                1            3.40              1.13         47.10                21.57           False
   WMT           93.62               47            0.05              0.04        124.80                24.34           False
  GILD           91.18               34            0.39              0.38        138.39                20.76           False
  COST           90.91               44            0.29              2.03        986.34                18.46           False
  TMUS           88.24               34            0.47              0.65        196.84                22.97           False
   AEP           87.50                8            1.37              1.29        134.01                17.62           False
   PEP           86.21               29            0.43              0.48        158.18                20.28           False
   CEG           86.05               43            0.44              0.92        298.75                57.36           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-17T10:40:05.810155-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-17T10:35:05.687840-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-17T10:30:01.382561-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-17T10:25:03.697036-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-17T10:10:03.834332-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-17T10:05:00.758906-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-17T10:00:05.566265-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-17T09:55:00.882857-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-17T09:40:05.709924-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-17T09:35:05.702550-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260417105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260417105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260417105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260417105005)

</details>
