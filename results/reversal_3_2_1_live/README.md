# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-22 11:10:04 EDT`
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

- Cash: `$6,100.20`
- Equity: `$12,002.20`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$28.21`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   1     26     5873.79                  5902.0       225.91          227.0      225.91         227.0           28.21                   0.48         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC          100.00               37            0.63              0.29         66.13                73.47            True
   HON          100.00               27            0.61              0.95        221.81                25.07            True
   MAR           88.89               36            0.60              1.58        374.77                30.40            True
  FAST           87.50               24            1.27              0.41         45.53                37.98            True
  ODFL           85.71               35            0.79              1.24        223.89                29.66            True
  PAYX           83.78               37            0.82              0.54         93.45                30.98            True
  GEHC           81.82               33            0.91              0.46         72.06                33.30            True
  WDAY           80.49               41            1.26              1.14        128.67                55.10            True
  CTSH           80.00               25            1.74              0.73         60.14                29.24            True
  TMUS          100.00                1            4.54              6.21        192.73                23.13           False
    EA           95.56               45            0.00              0.01        203.55                 4.87           False
  GILD           91.67               36            0.36              0.33        133.15                20.00           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-22T11:10:04.790392-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-22T11:05:00.789352-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-22T11:00:02.775064-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-22T10:55:04.688826-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-22T10:40:00.720670-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-22T10:35:03.653991-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-22T10:30:00.799409-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-22T10:25:01.815083-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-22T10:10:00.802391-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-22T10:05:03.491496-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260422111004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260422111004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260422111004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260422111004)

</details>
