# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-17 10:40:05 EDT`
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

- Cash: `$6,636.99`
- Equity: `$13,375.69`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$17.77`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   1      9     6720.93                  6738.7       746.77         748.74      746.77        748.74           17.77                   0.26         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   LIN           90.00               10            1.54              5.38        496.92                18.78            True
  ALNY           88.89               27            1.74              3.89        318.46                45.49            True
  GILD           88.46               26            0.71              0.69        138.26                20.76            True
   PEP           86.36               22            0.84              0.93        157.98                20.28            True
  FANG          100.00                1            8.41             10.99        181.94                29.20           False
   EXC          100.00                1            3.51              1.17         47.09                21.57           False
   WMT           93.18               44            0.14              0.13        124.77                24.34           False
  COST           91.11               45            0.22              1.54        986.55                18.46           False
  TMUS           88.57               35            0.42              0.58        196.87                22.97           False
   XEL           87.50                8            1.17              0.67         80.76                23.12           False
   WBD           86.05               43            0.11              0.02         27.38                 8.92           False
   CEG           85.71               42            0.49              1.02        298.70                57.36           False
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

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260417104005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260417104005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260417104005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260417104005)

</details>
