# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-14 09:40:06 EDT`
Last processed slot: `manage_0930`

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
- Equity: `$13,234.28`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$89.28`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-13                   1      8      5916.0                 6005.28        739.5         750.66       739.5        750.66           89.28                   1.51         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               10            2.47              3.27        187.70                30.53            True
   WDC           96.97               33            1.65              4.05        348.43                85.45            True
  COST           95.45               22            0.90              6.18        978.20                19.04            True
  INTC           94.44               18            3.83              1.75         64.45                75.15            True
   STX           93.94               33            1.79              6.45        510.52                74.84            True
   AEP           91.67               12            0.88              0.83        134.11                18.89            True
  MPWR           90.91               33            1.18             11.35       1367.37                58.48            True
   WMT           90.48               21            1.00              0.87        124.19                26.19            True
  AVGO           89.74               39            0.73              1.95        378.92                46.02            True
  FAST           87.50               24            1.22              0.39         45.63                37.61            True
   KDP           86.36               22            0.67              0.12         25.99                21.11            True
  CSCO           83.33               18            0.83              0.48         82.15                28.38            True
```

## Recent Events

```text
                    timestamp_et           slot   event_type                          detail
2026-04-14T09:40:06.426052-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-14T09:35:06.430444-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-14T09:30:06.428322-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-14T09:25:06.428256-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-14T01:39:11.037721-04:00 share_ext_0135 slot_skipped {"reason": "already_processed"}
2026-04-14T01:38:52.650663-04:00 share_ext_0135 slot_skipped {"reason": "already_processed"}
2026-04-14T00:08:05.269990-04:00 share_ext_0005 slot_skipped {"reason": "already_processed"}
2026-04-13T23:54:15.718712-04:00 share_ext_2350 slot_skipped {"reason": "already_processed"}
2026-04-13T16:00:05.899443-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-13T15:55:05.891523-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260414094006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260414094006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260414094006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260414094006)

</details>
