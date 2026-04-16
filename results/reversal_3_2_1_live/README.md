# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 10:30:06 EDT`
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

- Cash: `$7,327.92`
- Equity: `$15,157.92`
- Realized PnL: `$4,347.92`
- Unrealized PnL: `$810.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   HON     option         option HON260515C00240000       2026-04-15                   1     18      7020.0                  7830.0          3.9           4.35      231.34        230.77           810.0                  11.54         100.0               22              0.82         27.49           31.38                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               35            0.53              2.79        752.73                24.02            True
   HON          100.00               27            0.53              0.87        231.82                23.34            True
   WDC           97.30               37            0.53              1.36        364.42                79.90            True
  MRVL           96.15               26            2.16              2.04        133.73                70.04            True
  ROST           92.59               27            0.61              0.96        223.74                24.88            True
  NVDA           91.67               36            0.68              0.94        198.47                36.33            True
  ISRG           89.47               19            1.63              5.34        466.07                23.09            True
  ALNY           88.89               27            1.82              4.26        331.57                43.40            True
  TSLA           83.87               31            1.39              3.82        390.31                50.86            True
  DASH           83.33               42            0.64              0.81        179.59                53.35            True
  KLAC           83.33               24            1.94             23.74       1737.93                51.26            True
  PYPL           82.35               34            0.70              0.24         49.47                36.71            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-16T10:30:06.538163-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-16T10:25:06.584595-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-16T10:10:06.432406-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-16T10:05:06.442845-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-16T10:00:05.433710-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-16T09:55:01.387641-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-16T09:40:05.435541-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-16T09:35:04.828747-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-16T09:30:06.428916-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-16T09:25:06.428686-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416103006)

</details>
